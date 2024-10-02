from django.shortcuts import render,redirect
from pathlib import Path
import os
from .procedures import split_text,process_song
from .forms import generate_karaoke_form
from django.contrib import messages

base_dir = Path(__file__).resolve().parent.parent

template_dir = os.path.join(base_dir,'templates')

def main_menu(request):
    return render(request,os.path.join(template_dir,'main_menu.html'))



def generate_karaoke(request):
    if request.method == 'POST':
        form =generate_karaoke_form(request.POST,request.FILES)
        if form.is_valid():
            song_file = form.cleaned_data['song']
            lyrics_text = form.cleaned_data['lyrics']
            song_path=process_song(song_file)
            print(song_path)
            return synchronize(request,song_path,lyrics_text)
    else:
        form = generate_karaoke_form()
    return render(request,'generate_karaoke.html',{'form':form})


def synchronize(request,song_path,lyrics):
    words = split_text(lyrics)
    return render(request,'synchronize.html',{'song':song_path,'lyrics':words})




def view_collection(request):
    return render(request,'view_collection.html')