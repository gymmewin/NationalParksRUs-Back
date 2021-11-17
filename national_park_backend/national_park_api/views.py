from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import NationalParkSerializer
from .models import NationalPark


class NationalParkList(generics.ListCreateAPIView):
    queryset = NationalPark.objects.all().order_by('id')
    serializer_class = NationalParkSerializer

class NationalParkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NationalPark.objects.all().order_by('id')
    serializer_class = NationalParkSerializer
