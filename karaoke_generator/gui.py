import os
import time
import webview
import subprocess


def start_webview():
    window = webview.create_window(
        'Karaoke-Generator', 'http://localhost:8000/', confirm_close=True, width=900, height=600)
    webview.start()
    window.closed = os._exit(0)


def start_server():
    # Ejecuta el servidor Django
    os.chdir('_internal')
    command = ['python', 'manage.py', 'runserver'] if os.name == 'nt' else [
        'python3', 'manage.py', 'runserver']
    server_process = subprocess.Popen(command)
    return server_process


if __name__ == '__main__':
    server_processes = start_server()
    time.sleep(3)
    start_webview()
