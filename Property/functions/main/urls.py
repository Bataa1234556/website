from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'main'

urlpatterns = [
    path('admin/', views.admin_goods_list, name='admin_goods_list'),
    path('admin/good/new/', views.admin_good_new, name='admin_good_new'),
    path('admin/good/<int:pk>/', views.admin_good_detail, name='admin_good_detail'),
    path('admin/good/<int:pk>/edit/', views.admin_good_edit, name='admin_good_edit'),
    path('admin/good/<int:pk>/delete/', views.admin_good_delete, name='admin_good_delete'),
]
