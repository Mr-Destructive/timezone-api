from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import Get_Time, Convert_Time

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
        path('<str:timezone>/', Get_Time.as_view()),
        path('convert/<str:t1>/<str:t2>/', Convert_Time.as_view()),
]
