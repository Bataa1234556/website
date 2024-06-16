from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.user_goods_list, name='user_goods_list'),
    path('good/<int:pk>/', views.user_good_detail, name='user_good_detail'),
]
