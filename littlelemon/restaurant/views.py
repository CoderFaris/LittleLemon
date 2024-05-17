from django.shortcuts import render, get_object_or_404
from django.core import serializers as s
from django.http import JsonResponse
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
from django.views.decorators.csrf import csrf_exempt




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

@csrf_exempt
def book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = BookingForm(data)
            if form.is_valid():
                booking = Booking(
                    name=form.cleaned_data['name'],
                    no_of_guests=form.cleaned_data['no_of_guests'],
                    BookingDate=form.cleaned_data['BookingDate']
                )
                booking.save()
                return JsonResponse({'status': 'success'}, status=201)
            else:
                return JsonResponse({'status': 'fail', 'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'errors': 'Invalid JSON'}, status=400)

    form = BookingForm()
    return render(request, 'book.html', {'form': form})

@csrf_exempt
def bookings(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.filter(BookingDate=date)
        else:
            bookings = Booking.objects.all()
        

        bookings_list = list(bookings.values('name', 'no_of_guests', 'BookingDate'))
        
        
        # Check if it is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
            return JsonResponse(bookings_list, safe=False)
        else:
            # Render bookings.html for non-AJAX GET requests
            bookings_list = s.serialize('json', bookings)
            return render(request, "bookings.html", {'bookings_list': bookings_list})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



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
    

