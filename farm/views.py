from sre_constants import SUCCESS
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect

from .models import Aduino
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import AduinoSerializer

from .forms import AduinoForm
from django.http import JsonResponse

def index(request,user_id):
    aduino = get_object_or_404(Aduino, useridx=user_id)
    context = {'aduino': aduino}
    return render(request, 'farm/dashboard.html', context)

@csrf_exempt
def aduino_modify(request,user_id):
    obj = Aduino.objects.get(useridx=user_id)
    if request.method == "POST": 
        data = JSONParser().parse(request)
        device = data[0].get("device","")
        if(obj.devicer == device):
        #userid = data[0].get("username","")
        #userpw = data[0].get("userpw","")
        #login_result = authenticate(username=userid, password=userpw)
        #print("userid = " + userid + " result = " + str(login_result))
        #if login_result:
            serializer = AduinoSerializer(obj, data = data[1])
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(status=200)

@csrf_exempt
def aduino_auto(request,user_id):
    if request.method == "GET":
        obj = Aduino.objects.get(useridx=user_id)
        data = {
            "temp":obj.temp,    
            "hum":obj.hum,
            "ilum":obj.illum,
            "waterCycle":obj.waterCycle
        }
        return JsonResponse(data)

@csrf_exempt
def ajax_method(request,user_id):
        obj = Aduino.objects.get(useridx=user_id)
        data = {
            "nowtemp":obj.nowtemp,
            "nowhum":obj.nowhum,
            "nowillum":obj.nowillum,
            "nowwaterCycle":obj.nowwaterCycle
           }

        return JsonResponse(data)

def aduino_insert(request,user_id):
    obj = Aduino.objects.get(useridx=user_id)
    if request.method == "POST":
        form = AduinoForm(request.POST)
        if form.is_valid():
            temp = form.cleaned_data.get('temp')
            hum= form.cleaned_data.get('hum')
            illum = form.cleaned_data.get('illum')
            waterCycle = form.cleaned_data.get('waterCycle')
            obj.temp = temp
            obj.hum = hum
            obj.illum = illum
            obj.waterCycle = waterCycle
            obj.save()
            return redirect('farm:index', user_id=user_id)
    else:
        form = AduinoForm()
    return redirect('farm:index', user_id=user_id)
