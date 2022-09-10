import os
import platform


def play_beep_sound():
    system = platform.system()
    if system == 'Darwin':
        os.system("afplay beep.wav")
    else:
        print('play_beep_sound not implemented')
