import os
from os.path import basename
import signal
import sys
import random
import subprocess

# Melissa
from melissa import profile
from melissa.tts import tts

WORDS = {
    'play_shuffle': {
        'groups': [
            ['party', 'time'],
            ['party', 'mix']
        ]
    },
    'play_random': {
        'groups': [
            ['play', 'music'],
            ['playing', 'music']]
    },
    'play_specific_music': {
        'groups': [['play'], ['playing']]
    },
    'stop_music': {
        'groups': [['stop', 'music']]
    }
}

sox_file_types = ['.wav', '.flac', 'ogg']
music_listing = None

proc = None

def mp3gen():
    """
    This function finds all the mp3 files in a folder
    and it's subfolders and returns a list.
    """
    global music_listing

    if music_listing is not None:
        return

    if sys.platform != 'darwin' \
            and sys.platform != 'win32' \
            and not sys.platform.startswith('linux'):
        print "Music only enabled on darwin, win32, and linux."
        return

    music_listing = []
    for root, dirs, files in os.walk(profile.data['music_path']):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                if sys.platform == 'darwin':
                    music_listing.append([
                        'afplay',
                        os.path.join(root, filename)])
                else:
                    music_listing.append([
                        'mpg123',
                        os.path.join(root, filename)])
            elif os.path.splitext(filename)[1] in sox_file_types:
                if sys.platform != 'darwin':
                    music_listing.append([
                        'play',
                        os.path.join(root, filename)])


def music_player(music_selection):
    """
    This function takes the name of a music file as an argument
    and plays it depending on the OS.
    """
    global proc
    player = music_selection[0] + " '" + music_selection[1] + "'"
    print player
    if proc is not None:
        os.kill(proc.pid, signal.SIGTERM)
    proc = subprocess.Popen(music_selection, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
def stop_music(text):
    global proc
    if proc is not None:
        os.kill(proc.pid, signal.SIGTERM)
        proc = None


def play_random(text):
    try:
        mp3gen()
        music_playing = random.choice(music_listing)
        song_name = os.path.splitext(basename(music_playing[1]))[0]
        tts("Now playing: " + song_name)
        music_player(music_playing)

    except IndexError as e:
        tts('No music files found.')
        print("No music files found: {0}".format(e))


def play_specific_music(speech_text):
    words_of_message = speech_text.split()
    words_of_message = [x for x in words_of_message if x not in ['play', 'playing']]
    cleaned_message = ' '.join(words_of_message)
    print 'Looking for ' + cleaned_message
    mp3gen()

    for i in range(0, len(music_listing)):
        if cleaned_message in music_listing[i][1].lower():
            print 'Playing ' + music_listing[i][1]
            music_player(music_listing[i])
            break


def play_shuffle(text):
    try:
        mp3gen()
        random.shuffle(music_listing)
        for i in range(0, len(music_listing)):
            music_player(music_listing[i])

    except IndexError as e:
        tts('No music files found.')
        print("No music files found: {0}".format(e))
