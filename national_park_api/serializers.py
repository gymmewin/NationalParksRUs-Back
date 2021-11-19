from rest_framework import serializers
from .models import NationalPark, Attraction

class NationalParkSerializerBase(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = NationalPark # tell django which model to use
        fields = ('id','name', 'description', 'image', 'location', 'admission_fee' )

class AttractionSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'attraction_name')

class NationalParkSerializer(NationalParkSerializerBase):
    top_attractions = AttractionSerializerBase(many=True)
    class Meta(NationalParkSerializerBase.Meta):
        fields = NationalParkSerializerBase.Meta.fields + ('top_attractions')

class AttractionSerializer(AttractionSerializerBase):
    park = NationalParkSerializerBase()
    class Meta(AttractionSerializerBase.Meta):
        fields = AttractionSerializerBase.Meta.fields + ('park')
