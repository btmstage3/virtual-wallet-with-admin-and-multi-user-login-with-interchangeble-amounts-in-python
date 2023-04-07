from django.urls import path

from users import views

app_name = 'users'

from django.urls import path, include

urlpatterns = [
    path('', include('mywallet.urls')), # include the URLs for the mywallet app
    path('users/', include('users.urls')), # include the URLs for the users app

]
