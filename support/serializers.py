from rest_framework import serializers
from .models import *

class DriverFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverFields
        fields = ('id', 'name', 'verified')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDetails
        fields = ('id','first_name','last_name','email','street_address_1','street_address_2','city','state','driving_lisence','aadhar_card','driver_photo','verified')