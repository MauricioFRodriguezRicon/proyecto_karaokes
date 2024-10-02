import os
import tempfile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from moviepy.editor import VideoFileClip

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
    

def save_song(file):
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
    
    filename = fs.save(file.name, file)
    
    file_url = fs.url(filename)
    
    return file_url
 
def split_text(text):
    flat_text = text.replace('\n',' ').replace('\r','')
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
    mp3_file_name = os.path.splitext(file.name)[0] + ".mp3"
    mp3_file_path = os.path.join(settings.MEDIA_ROOT, mp3_file_name)

    
    # Extraer el audio del MP4 y guardarlo como un MP3
    with VideoFileClip(temp_mp4_file_path) as video:
        audio = video.audio
        audio.write_audiofile(mp3_file_path)

    mp3_file_url = os.path.join(settings.MEDIA_URL,mp3_file_name)

    return mp3_file_url # Devolver la ruta del archivo MP3 generado
