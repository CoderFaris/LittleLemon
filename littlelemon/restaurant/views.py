from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import generics, serializers
from rest_framework import viewsets, permissions
from datetime import datetime
import environ
import requests, json
from .forms import BookingForm


env = environ.Env()
environ.Env.read_env()

# for testing purposes
def get_token():
    url = 'http://127.0.0.1:8000/auth/token/login'
    data = {

        "username" : env('USERNAME'), 
        "password" : env('PASSWORD')

    }
    response = requests.post(url, data=data)
    response_dict = json.loads(response.text)
    return response_dict.get('access')

# views for everyone
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def menu(request):
    
    menu_items = Menu.objects.all()
    context = {
        
        'menu' : menu_items
    }
    return render(request, 'menu.html', context)

def menu_item(request, pk):
    
    menu_item = get_object_or_404(Menu, pk=pk)
    context = {
        
        'menu_item' : menu_item
    }
    return render(request, 'menu_item.html', context)

def bookings(request):
    return render(request, 'bookings.html')

class Book(View):
    form_class = BookingForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'book.html', {'form' : form})



# api views
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

