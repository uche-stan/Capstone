from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Menu, Booking
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated



# Create your views here.
        
def index(request):
    return render(request, 'index.html', {})
 

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class BookingViewSet(viewsets.ModelViewSet): 
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    

        