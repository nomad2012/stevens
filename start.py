import sys
import subprocess
from datetime import datetime

# Melissa
from melissa.profile_loader import load_profile
from melissa.tts import tts
from melissa.stt import stt
from melissa.brain import query


def main():
    data = load_profile(True)
    hr = datetime.now().time().hour
    if hr < 12:
        period = 'Morning'
    elif hr < 18:
        period = 'Afternoon'
    else:
        period = 'Evening'
        
    tts('Good ' + period + ' sir.  How may I be of service?')

    while True:
        if sys.platform == 'darwin':
            subprocess.call(['afplay', 'data/snowboy_resources/ding.wav'])
        elif sys.platform.startswith('linux') or sys.platform == 'win32':
            pass #subprocess.call(['mpg123', 'data/snowboy_resources/ding.wav'])

        text = stt()
                
        if text is None:
            continue
        else:
            query(text)

if __name__ == "__main__":
    main()
