from django.urls import path

from . import views

app_name ='farm'

urlpatterns = [
    path('farm/<int:user_id>/', views.index, name='index'),
    path('farm/modify/<int:user_id>', views.aduino_modify, name='aduino_modify'),
    path('farm/auto/<int:user_id>', views.aduino_auto, name='aduino_auto'),
    path('farm/insert/<int:user_id>', views.aduino_insert, name='aduino_insert')
]