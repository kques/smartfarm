from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import devicer
from .forms import UserForm
from .forms import AduinoForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form2 = AduinoForm(request.POST)
        if form.is_valid() & form2.is_valid():
            device = form2.cleaned_data.get('devicer')
            if devicer.objects.get(device = device):
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)  # 사용자 인증
                login(request, user) # 로그인 
                aduino = form2.save(commit=False)
                aduino.useridx = request.user.id
                aduino.author = request.user
                aduino.temp = NULL
                aduino.hum = NULL
                aduino.illum = NULL
                aduino.waterCycle = NULL
                aduino.nowtemp = NULL
                aduino.nowhum = NULL
                aduino.nowillum = NULL
                aduino.nowwaterCycle = NULL
                aduino.save()
                return redirect('farm:index', user_id=user.id)
        
            
    else:
        form = UserForm()
        form2 = AduinoForm()
    return render(request, 'common/signup.html', {'form': form,'form2':form2})
