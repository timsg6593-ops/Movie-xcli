import subprocess

def play_stream(url):
    subprocess.run(['vlc', url, '--fullscreen'])
