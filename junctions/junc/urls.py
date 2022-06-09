from django.urls import path
from . import views
from .views import JuncCreate, JuncDetail, JuncList, JuncUpdate

app_name = 'junc'

urlpatterns = [
    path('', views.JuncList.as_view(), name='all'),
    path('<int:pk>/', views.JuncDetail.as_view(), name='detail'),
    path('create/', views.JuncCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.JuncUpdate.as_view(), name='update'),
    path('alldet', views.JuncAlldet.as_view(), name='alldet')
]
