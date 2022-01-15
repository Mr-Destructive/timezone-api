from django.urls import path
from .views import Get_Time, Convert_Time

urlpatterns = [
        path('<str:timezone>/', Get_Time.as_view()),
        path('convert/<str:t1>/<str:t2>/', Convert_Time.as_view()),
]
