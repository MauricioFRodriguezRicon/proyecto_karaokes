from django.contrib import admin
from django.urls import path
import karaoke_generator.views as views 


urlpatterns = [
    path('',views.main_menu,name='main-menu'),
]
