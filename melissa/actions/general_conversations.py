import random

# Melissa
from melissa import profile
from melissa.tts import tts

WORDS = {'who_are_you': {'groups': [['who', 'are', 'you']]},
         'toss_coin': {'groups': [['heads', 'tails'],
                                  ['toss', 'coin'], ['flip', 'coin']]},
         'who_am_i': {'groups': [['who', 'am', 'i']]},
         'where_born': {'groups': [['where', 'born']]},
         'how_are_you': {'groups': [['how', 'are', 'you']]},
         'are_you_up': {'groups': [['you', 'up']]},
         'stevens': {'groups': [['stevens'], ['steven'], ['stephen'], ['steve']]},
         'thank_you': {'groups': [['thank', 'you'], ['thanks']]},
         'undefined': {'groups': []}}


def who_are_you(text):
    va_name = profile.data['va_name']
    messages = ['I am ' + va_name + ', Sirs butler.',
                'My name is ' + va_name + ', sir.',
                'I am the head butler, ' + va_name + ', sir.']
    tts(random.choice(messages))


def toss_coin(text):
    outcomes = ['heads', 'tails']
    tts('I just flipped a coin sir. It shows ' + random.choice(outcomes))


def who_am_i(text):
    name = profile.data['name']
    tts('You are ' + name + ', sir.')


def where_born(text):
    tts('I was born in Devonshire, sir.')


def how_are_you(text):
    tts('I am fine, thank you sir.')


def are_you_up(text):
    tts('For you sir, always.')


def stevens(text):
    messages = ['Sir!',
                'Yes sir.',
                'At your service sir.',
                'Here sir.']
    tts(random.choice(messages))

def thank_you(text):
    messages = ['Of course sir.',
                'Any time sir.',
                'You are quite welcome sir.',
                "Don't mention it sir."]
    tts(random.choice(messages))


def undefined(text):
    pass
    #tts('I\'m sorry sir, did you say ' + text + '?')
