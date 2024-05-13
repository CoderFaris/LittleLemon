from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('reservations/', views.reservations, name='reservations'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
    
]