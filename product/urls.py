from django.urls import path, include
from  . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('order/',views.order,name='order'),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),

    
]