from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/', views.product_list, name='product_list_by_category'),
    path('details/', views.product_detail, name='product_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)