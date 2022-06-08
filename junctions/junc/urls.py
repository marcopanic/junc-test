from django.urls import path
from . import views

app_name = 'junc'

urlpatterns = [
    path('', views.JuncList.as_view(), name='all'),
    path('<int:pk>/', views.JuncDetail.as_view(), name='detail'),
]
