from django import forms
from django.core.exceptions import ValidationError

def validate_extension(value):
    valid_extension = ['.mp3','.mp4','.wma']

    if not any([value.name.endswith(ext) for ext in valid_extension]):
       raise ValidationError('Solo se permiten archivos .MP3, .MP4 o .WMA')
    


class generate_karaoke_form(forms.Form):
    song=forms.FileField(label='song',validators=[validate_extension])
    lyrics=forms.CharField(label='lyrics',widget=forms.Textarea)
    song.widget.attrs.update({'accept':'.mp3,.mp4,.wma'})
    