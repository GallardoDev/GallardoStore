from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.principal, name='principal'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin')
]
