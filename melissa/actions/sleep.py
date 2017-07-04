import random

# Melissa
from melissa import profile
from melissa.tts import tts

WORDS = {'go_to_sleep': {'groups': [
    ['good', 'night', 'stevens'],
    ['good', 'bye', 'stevens'],
    ['that', 'will', 'be', 'all', 'stevens']]}}


def go_to_sleep(text):
    replies = ['Of course, sir.  Good night!',
               'Very good, sir.  Have a good night!',
               'As you wish, sir.  Good night!',
               'And to you as well, sir!',
               'Good night, sir.']
    tts(random.choice(replies))

    if profile.data['hotword_detection'] == 'on':
        print('\nListening for Keyword...')
        print('Press Ctrl+C to exit')

    quit()
