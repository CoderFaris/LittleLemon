from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'), 
    path('menu-edit/', views.MenuItemView.as_view(), name='menu-edit'), #for editing the menu
    path('bookings/', views.bookings, name='bookings'),
    path('menu/<int:pk>', views.menu_item, name='menu_item'),
    path('menu-edit/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item-edit'), #for editing the menu item
    path('book/', views.book, name='book'),
    path('api-token-auth/', obtain_auth_token)
    
]