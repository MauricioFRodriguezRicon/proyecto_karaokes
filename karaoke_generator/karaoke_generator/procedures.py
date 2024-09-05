import os
import tempfile

def temp_song(file):
    with tempfile.NamedTemporaryFile(delete=False,suffix=os.path.splitext(file.name)[1]) as temp_file:
        for chunk in file.chunks():
            temp_file.write(chunk)
        return temp_file.name
    

def lyrics_text(text):
    flat_text = text.replace('\n',' ').replace('\r','')
    flat_text = flat_text.upper()
    return flat_text


def split_text(text):
    listed = text.split()
    groups = ()
    group = ()
    for word in listed:
        if len(group) == 4:
            groups.append(group)
            group.clear()
        group.append(word)
    return groups
