from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from account import jwt_views
from .views import index

schema_view = get_schema_view(
   openapi.Info(
      title="毕方(Bifang)自动化部署平台 API",
      default_version='v1',
      description="毕方(Bifang)自动化部署平台，引导你进入devops开发的领域。",
      terms_of_service="https://github.com/aguncn/bifang",
      contact=openapi.Contact(email="aguncn@163.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('jwt_auth/', jwt_views.obtain_jwt_token),
    path('refresh_jwt_auth/', jwt_views.refresh_jwt_token),
    path('verify_jwt_auth/', jwt_views.verity_jwt_token),
]

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$',
           schema_view.without_ui(cache_timeout=0),
           name='schema-json'),
   path('swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
   path('redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]

urlpatterns += [
    path('account/', include('account.urls')),
    path('app/', include('app.urls')),
    path('project/', include('project.urls')),
    path('cmdb/', include('cmdb.urls')),
    path('deploy/', include('deploy.urls')),
    path('env/', include('env.urls')),
    path('gitapp/', include('gitapp.urls')),
    path('history/', include('history.urls')),
    path('release/', include('release.urls')),
    path('server/', include('server.urls')),
    path('permission/', include('permission.urls')),
    path('stats/', include('stats.urls')),
]