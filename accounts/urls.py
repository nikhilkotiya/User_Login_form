from django.urls import path,include
from . import views

urlpatterns = [
    path('userdashboard' ,views.userdashboard,name = "userdashboard"),
    path('index',views.index,name='index'),
    
]