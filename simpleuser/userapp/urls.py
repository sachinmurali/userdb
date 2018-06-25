from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.user_list, name='list_users'),
    path('users/<uuid:user_id>/', views.user_detail, name='user_detail'),
]
