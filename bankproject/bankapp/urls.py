from . import views
from django.urls import path,include

app_name='bankapp'

urlpatterns = [
    
    path('',views.demo,name='demo'),
   
]
