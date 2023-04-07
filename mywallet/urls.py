from django.urls import path
from django.contrib import admin

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),

]
