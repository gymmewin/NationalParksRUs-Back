from rest_framework import serializers
from .models import NationalPark, Attraction

class NationalParkSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = NationalPark # tell django which model to use
        fields = ('id','name', 'description', 'image', 'location', 'admission_fee', 'top_attractions')

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'park')
