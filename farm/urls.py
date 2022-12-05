from django.urls import path

from . import views

app_name ='farm'

urlpatterns = [
    path('farm/<int:user_id>/', views.index, name='index'),
    path('farm/modify/<int:user_id>', views.aduino_modify, name='aduino_modify'),
    path('farm/auto/<int:user_id>', views.aduino_auto, name='aduino_auto'),
    path('farm/insert/<int:user_id>', views.aduino_insert, name='aduino_insert'),
    path('farm/ajax/<int:user_id>',views.ajax_method, name='ajax_method'),
    path('farm/detail/<int:question_id>/', views.detail, name='detail'),
    path('farm/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('farm/question/create/', views.question_create, name='question_create'),
    
]
