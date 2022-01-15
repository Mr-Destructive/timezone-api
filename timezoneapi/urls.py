from django.contrib import admin
from django.urls import path,re_path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.documentation import include_docs_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Timezone API",
        default_version='v1',
        description="Timezone API Docs",
        terms_of_service="https://www.herokuapp.com/timezoneapi",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'), 
    path('api/', include('api.urls')),
]
