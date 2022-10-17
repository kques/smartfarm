from django import forms
from .models import Aduino


class AduinoForm(forms.ModelForm):
    class Meta:
        model = Aduino
        fields = ['temp','hum','illum','waterCycle']
        