import json
from manim import *
import os

from moviepy.editor import AudioFileClip, VideoFileClip
from .procedures import process_json
from .settings import BASE_DIR
from shutil import move as mv



def mover_y_renombrar_archivo(ruta_actual, nuevo_nombre, ruta_destino):
    # Asegúrate de que la carpeta destino existe; si no, créala
    os.makedirs(ruta_destino, exist_ok=True)

    # Construye la nueva ruta completa con el nuevo nombre en la ubicación de destino
    nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)

    # Mueve y renombra el archivo
    mv(ruta_actual, nueva_ruta)

    print(f'Archivo movido y renombrado a: {nueva_ruta}')
    return nueva_ruta


def create_karaoke_video(music_path,lyrics,video_outpath):

    print("====================")
    print(music_path)
    print("====================")

    class KaraokeScene(Scene):
        def __init__(self, audio_duration, **kwargs):
            super().__init__(**kwargs)
            self.audio_duration = audio_duration

        def construct(self):

            #background = ImageMobject("ruta/a/tu/fondo.png").scale(2)
            #self.add(background)
            passed = 0

            for i in range(0,len(lyrics)):
                texto = Text(
                    lyrics[i][0],
                    font_size=70,
                    color=WHITE
                )
                if i == 0:
                    #Espera para aparecer
                    self.wait(lyrics[i][1]-passed)
                    self.play(FadeIn(texto,shift=DOWN, scale=1), run_time=0.1)
                    passed = lyrics[i][1]
                    self.wait(lyrics[i+1][1]-passed)
                    self.play(FadeOut(texto,shift=DOWN * 2, scale=1),run_time=0.1)
                elif i < len(lyrics)-1:
                    passed = lyrics[i][1]
                    self.play(FadeIn(texto,shift=DOWN * 2, scale=1),run_time=0.1)
                    self.wait(lyrics[i+1][1]-passed) 
                    self.play(FadeOut(texto,shift=DOWN * 2, scale=1),run_time=0.1)
                else:
                    self.play(FadeIn(texto,shift=DOWN * 2, scale=1),run_time=0.1)
                    passed = lyrics[i][1]
                    self.wait(audio_duration-passed)


    name = os.path.basename(music_path)

    media_folder = os.path.join(BASE_DIR,'media')


    audio_path = os.path.join(media_folder,name)


    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    
    scene = KaraokeScene(audio_duration=audio_duration)
    scene.render()

    
    name = os.path.splitext(name)[0] + ".mp4"
    video_path = os.path.join(media_folder,'videos/1080p60/KaraokeScene.mp4')

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

# Ajusta la duración del audio al tiempo del video
    audio_subclip = audio_clip.subclip(0,min(audio_clip.duration,video_clip.duration))

# Añade el audio al video
    video_with_audio = video_clip.set_audio(audio_subclip)

# Exporta el video final con el audio añadido
    video_with_audio.write_videofile(os.path.join(video_outpath,name), codec="libx264", audio_codec="aac",fps=24)



    #video_clip = VideoFileClip(video_path).set_audio(audio_clip)
    #video_clip.write_videofile(os.path.join(video_outpath,name), fps=24)

    #os.rename(video_path,os.path.join(video_outpath,name))
    #mv(os.path.join(video_path,name),os.path.join(video_outpath,name))











