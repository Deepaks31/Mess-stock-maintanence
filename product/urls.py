from django.urls import path, include
from  . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('order/',views.order,name='order'),
    path('home/',views.home,name='home'),
    path('',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),

    
]