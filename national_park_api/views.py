from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import NationalParkSerializer, AttractionSerializer
from .models import NationalPark, Attraction


class NationalParkList(generics.ListCreateAPIView):
    queryset = NationalPark.objects.all().order_by('id')
    serializer_class = NationalParkSerializer

class NationalParkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NationalPark.objects.all().order_by('id')
    serializer_class = NationalParkSerializer

class AttractionList(generics.ListCreateAPIView):
    queryset = Attraction.objects.all().order_by('id')
    serializer_class = AttractionSerializer

class AttractionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attraction.objects.all().order_by('id')
    serializer_class = AttractionSerializer
