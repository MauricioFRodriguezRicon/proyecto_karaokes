from django.shortcuts import render, redirect
from pathlib import Path
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import json
from manim import *
from .procedures import split_text, process_song, verify, transform_to_strings, load_config, process_json,save_image, delete_all_media_files
from .manim_utils import create_karaoke_video as create
from .forms import generate_karaoke_form
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage


base_dir = Path(__file__).resolve().parent.parent

template_dir = os.path.join(base_dir, 'templates')


def main_menu(request):
    verify()
    return render(request, os.path.join(template_dir, 'main_menu.html'))


def generate_karaoke(request):
    if request.method == 'POST':
        form = generate_karaoke_form(request.POST, request.FILES)
        if form.is_valid():
            song_file = form.cleaned_data['song']
            lyrics_text = form.cleaned_data['lyrics']
            image = form.cleaned_data['image']
            print(image)
            image_path=save_image(image)
            print(image_path)
            song_path = process_song(song_file)

            return synchronize(request, song_path, lyrics_text,image_path)
    else:
        form = generate_karaoke_form()
    return render(request, 'generate_karaoke.html', {'form': form})


def synchronize(request, song_path, lyrics,image_path):
    words = split_text(lyrics)
    list_of_lyrics = transform_to_strings(words)
    return render(request, 'synchronize.html', {'song': song_path, 'lyrics': list_of_lyrics,'image_path':image_path})


def finished(request):
    delete_all_media_files()
    return redirect(main_menu)


def generating_karaoke(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        musica = data.get('musica')
        palabras = (data.get('lyrics'))
        image_path = data.get('image')
        lyrics = process_json(palabras)
        config = load_config()
        videos = config.get('videos')
        create_karaoke_video(musica, lyrics,image_path, videos)
        # Redirigir a la página de carga
        return JsonResponse({"status": "success", "message": "The video was generated successfully"})
    return JsonResponse({"status": "error", "message": "Try again"})


def create_karaoke_video(music_path, lyrics_data,image_path, output_path):
    create(music_path, lyrics_data,image_path, output_path)


def add_audio_to_video(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_path, fps=24)
