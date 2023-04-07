from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('new/', views.transaction_new, name='transaction_new'),
    path('<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
]
