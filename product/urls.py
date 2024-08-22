from django.urls import path, include
from  . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('order/',views.order,name='order'),
    path('saved_item_list/', views.saved_items_list, name='item_list'),
    path('edit-item/<int:id>/', views.edit_item, name='edit_item'),
    path('home/',views.home,name='home'),
    path('',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),

    
]