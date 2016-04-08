from django.shortcuts import render
from .serializers import OrderSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer