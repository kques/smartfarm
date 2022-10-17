from rest_framework import serializers
from .models import Aduino
from common.models import CustomUser


class AduinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aduino
        fields = ['nowtemp','nowhum', 'nowillum', 'nowwaterCycle']


class AduinoAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aduino
        fields = ['temp','hum', 'illum', 'waterCycle']


class UserSreializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
