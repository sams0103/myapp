from django.contrib import admin
from django.urls import path,include
from amor import views

urlpatterns = [
   path('',views.home,name='home'),
   path('no.html',views.no,name='no'),
   path('yes.html',views.yes,name='yes')
]