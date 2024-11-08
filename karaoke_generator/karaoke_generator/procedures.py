import os
import tempfile
import json
from manim import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from moviepy.editor import VideoFileClip
import shutil

def process_song(file):
    extension = os.path.splitext(file.name)
    extension = extension[1].lower()

    if extension == ".mp4":
        path = audio_extract(file)
    elif extension == ".mp3" or extension == ".wma":
        path = save_song(file)
    else:
        raise ValueError("Only .mp3, .mp4 or .wma accepted")
    return path
    
def process_json(string):
    print(string)
    data=[]
    print(string)
    words = string.replace('{', '')
    words = words.replace('}', '')
    words = words.replace('[', '')
    words = words.replace(']', '')
    words = words.replace('"','')
    words= words.split(',')
    
    items = []
    for word in words:
            item = word.split(':')
            items.append(item[1])

    for i in range(0, len(items)-1,2):
        new = [items[i],float(items[i+1])]
        data.append(new)

    return data

def save_song(file):
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
    
    filename = fs.save(file.name.replace(' ',''), file)
    
    file_url = fs.url(filename)
    
    return file_url
 
def split_text(text):
    flat_text = text.replace('\n',' ').replace('\r','').replace(',','')
    flat_text = flat_text.upper()
    listed = flat_text.split()
    # Crea sublistas de "tamaño" elementos (4 en este caso)
    return [listed[i:i + 4] for i in range(0, len(listed), 4)]

def audio_extract(file):
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_mp4_file:
        for chunk in file.chunks():
            temp_mp4_file.write(chunk)

        temp_mp4_file_path = temp_mp4_file.name  # Ruta del archivo MP4 temporal

    # Extraer el audio del archivo MP4 y guardarlo como un MP3 en la carpeta media
    mp3_file_name = os.path.splitext(file.name)[0].replace(' ','') + ".mp3"
    mp3_file_path = os.path.join(settings.MEDIA_ROOT, mp3_file_name)

    
    # Extraer el audio del MP4 y guardarlo como un MP3
    with VideoFileClip(temp_mp4_file_path) as video:
        audio = video.audio
        audio.write_audiofile(mp3_file_path)

    mp3_file_url = os.path.join(settings.MEDIA_URL,mp3_file_name)

    return mp3_file_url # Devolver la ruta del archivo MP3 generado


def verify():
    desktop=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    base = settings.BASE_DIR
    json_folder = os.path.join(base, 'static/json')
    videos=os.path.join(json_folder,"configuration.json")
    if not(os.path.exists(videos)):
        with open(videos,'w') as arch:
            content={'videos':desktop}
            json.dump(content,arch)

def act_config(new_path):
    print("Entro",new_path)
    json_folder = os.path.join(settings.BASE_DIR, '/static/json')
    videos=os.path.join(json_folder,"configuration.json")
    if os.path.exists(videos):
        with open(videos,"w") as arch:
            content={'videos':new_path}
            json.dump(content,arch)
    else:
        verify()

def load_config():
    base = settings.BASE_DIR
    json_folder = os.path.join(base, 'static/json')
    videos=os.path.join(json_folder,"configuration.json")
    with open(videos) as f:
        config = json.load(f)
        return config
    return config

def transform_to_strings(list_of_lyrics):
    new_list = []
    for listed in list_of_lyrics:
        phrase=""
        for word in listed:
            phrase+=word+" "
        new_list.append(phrase)

    return new_list


def delete_all_media_files():
    media_folder = settings.MEDIA_ROOT
        # Elimina todos los archivos y carpetas dentro de la carpeta de media
    for filename in os.listdir(media_folder):
        file_path = os.path.join(media_folder, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)  # Elimina archivos o enlaces simbólicos
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)  # Elimina carpetas y subcarpetas
