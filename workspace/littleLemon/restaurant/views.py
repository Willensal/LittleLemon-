from django.shortcuts import render
from django.core import serializers
from .models import Menu, Booking
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


# Create your views here. 
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
