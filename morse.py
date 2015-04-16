import pygame

'''
@TODO: The better way to handle this will be by lower casing all
characters that are between [az] right? :)
that will lessen this huge library...
'''

# global constants
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 60 # how often to check if playback has finished

morsetab = {
    'A': '.- ',
    'a': '.- ',
    'B': '-... ',
    'b': '-... ',
    'C': '-.-. ',
    'c': '-.-. ',
    'D': '-.. ',
    'd': '-.. ',
    'E': '. ',
    'e': '. ',
    'F': '..-. ',
    'f': '..-. ',
    'G': '--. ',
    'g': '--. ',
    'H': '.... ',
    'h': '.... ',
    'I': '.. ',
    'i': '.. ',
    'J': '.--- ',
    'j': '.--- ',
    'K': '-.- ',
    'k': '-.- ',
    'L': '.-.. ',
    'l': '.-.. ',
    'M': '-- ',
    'm': '-- ',
    'N': '-. ',
    'n': '-. ',
    'O': '--- ',
    'o': '--- ',
    'P': '.--. ',
    'p': '.--. ',
    'Q': '--.- ',
    'q': '--.- ',
    'R': '.-. ',
    'r': '.-. ',
    'S': '... ',
    's': '... ',
    'T': '- ',
    't': '- ',
    'U': '..- ',
    'u': '..- ',
    'V': '...- ',
    'v': '...- ',
    'W': '.-- ',
    'w': '.-- ',
    'X': '-..- ',
    'x': '-..- ',
    'Y': '-.-- ',
    'y': '-.-- ',
    'Z': '--.. ',
    'z': '--.. ',
    '0': '----- ',
     ',': '--..-- ',
    '1': '.---- ',
    '.': '.-.-.- ',
    '2': '..--- ',
    '?': '..--.. ',
    '3': '...-- ',
    ';': '-.-.-. ',
    '4': '....- ',
    ':': '---... ',
    '5': '..... ',
    "'": '.----. ',
    '6': '-.... ',
    '-': '-....- ',
    '7': '--... ',
    '/': '-..-. ',
    '8': '---.. ',
    '(': '-.--.- ',
    '9': '----. ',
    ')': '-.--.- ',
    ' ': '|',
    '_': '..--.- ',
}

morse_sound = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    ' ': 'short_silence.ogg',
    '*': 'very_short_silence.ogg',
    '|': 'long_silence.ogg',
}

pygame.init()
pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)


def main():
    convert_string = 'SOS'
    # print(string_to_code(convert_string))

    play_morse_sound(code_to_sound_code(string_to_code(convert_string)))
    print(string_to_code(convert_string).replace('|', '  '))


def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.

    This will load the whole sound into memory before playback
    """
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)


def play_morse_sound(code):
    for channel_id, dip in enumerate(code):
        try:
            sound = pygame.mixer.Sound(morse_sound[dip])
        except KeyError:
            sound = pygame.mixer.Sound(morse_sound[' '])
        playsound(sound)


def code_to_sound_code(code):
    res = code.replace('..', '.*.') \
              .replace('--', '-*-') \
              .replace('.-', '.*-') \
              .replace('-.', '-*.') \
              .replace('..', '.*.') \
              .replace('--', '-*-') \
              .replace('.-', '.*-') \
              .replace('-.', '-*.')
    return res


def string_to_code(convert_string):
    res = ''
    for c in convert_string:
        try:
            res += morsetab[c]
        except KeyError:
            pass
    return res


if __name__ == '__main__':
    main()
