from rest_framework import serializers
from .models import NationalPark

class NationalParkSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = NationalPark # tell django which model to use
        fields = ('id', 'description', 'image', 'location', 'admission_fee')
