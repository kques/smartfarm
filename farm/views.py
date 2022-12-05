from sre_constants import SUCCESS
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect

from .models import Aduino
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import AduinoSerializer

from django.utils import timezone
from .models import Question
from .forms import QuestionForm,AnswerForm
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required

from .forms import AduinoForm
from django.http import JsonResponse

def index(request,user_id):
    aduino = get_object_or_404(Aduino, useridx=user_id)
    
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'aduino':aduino,'question_list': page_obj}
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

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'farm/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('farm:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'farm/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('farm:index', user_id=request.user.id)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'farm/question_form.html', context)