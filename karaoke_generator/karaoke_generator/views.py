from django.shortcuts import render
from pathlib import Path
import os
base_dir = Path(__file__).resolve().parent.parent

template_dir = os.path.join(base_dir,'templates')

def main_menu(request):
    return render(request,os.path.join(template_dir,'main_menu.html'))

def generate(request):
    return render(request,os.path.join(template_dir,'generate_karaoke.html'))

def view_collection(request):
    return render(request,os.path.join(template_dir,'view_collection.html'))