from pygame import mixer

morsetab = {
    'A': '.-',
    'a': '.-',
    'B': '-...',
    'b': '-...',
    'C': '-.-.',
    'c': '-.-.',
    'D': '-..',
    'd': '-..',
    'E': '.',
    'e': '.',
    'F': '..-.',
    'f': '..-.',
    'G': '--.',
    'g': '--.',
    'H': '....',
    'h': '....',
    'I': '..',
    'i': '..',
    'J': '.---',
    'j': '.---',
    'K': '-.-',
    'k': '-.-',
    'L': '.-..',
    'l': '.-..',
    'M': '--',
    'm': '--',
    'N': '-.',
    'n': '-.',
    'O': '---',
    'o': '---',
    'P': '.--.',
    'p': '.--.',
    'Q': '--.-',
    'q': '--.-',
    'R': '.-.',
    'r': '.-.',
    'S': '...',
    's': '...',
    'T': '-',
    't': '-',
    'U': '..-',
    'u': '..-',
    'V': '...-',
    'v': '...-',
    'W': '.--',
    'w': '.--',
    'X': '-..-',
    'x': '-..-',
    'Y': '-.--',
    'y': '-.--',
    'Z': '--..',
    'z': '--..',
    '0': '-----',
    ',': '--..--',
    '1': '.----',
    '.': '.-.-.-',
    '2': '..---',
    '?': '..--..',
    '3': '...--',
    ';': '-.-.-.',
    '4': '....-',
    ':': '---...',
    '5': '.....',
    "'": '.----.',
    '6': '-....',
    '-': '-....-',
    '7': '--...',
    '/': '-..-.',
    '8': '---..',
    '(': '-.--.-',
    '9': '----.',
    ')': '-.--.-',
    ' ': ' ',
    '_': '..--.-',
}

morse_sound = {'.': 'dot.ogg', '-': 'dash.ogg', ' ': 'silence.ogg'}


def main():
    convert_string = 'Hello World'
    print(string_to_code(convert_string))
    play_morse_sound(string_to_code(convert_string))


def play_morse_sound(code):
    sounds = {}
    mixer.init()
    channel = mixer.find_channel()
    for channel_id, dip in enumerate(code):
        try:
            sounds[channel_id] = mixer.Sound(morse_sound[dip])
            # this isn't working need to check this out later
            channel.queue(sounds[channel_id])
        except KeyError:
            print(dip)


def string_to_code(convert_string):
    res = ''
    for c in convert_string:
        try:
            res += morsetab[c] + '\001'
        except KeyError:
            pass
    return res


if __name__ == '__main__':
    main()
