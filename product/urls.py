from django.urls import path, include
from  . import views

urlpatterns = [
    path('',views.order,name='order'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='login'),
    path('logout/',views.logout,name='logout'),

    
]