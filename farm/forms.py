from django import forms
from .models import Aduino
from .models import Question
from .models import Answer

class AduinoForm(forms.ModelForm):
    class Meta:
        model = Aduino
        fields = ['temp','hum','illum','waterCycle']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
       
        labels = {
            'subject': '제목',
            'content': '내용',
        }  
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }