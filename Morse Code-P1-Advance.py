# Dictionary for Morse Code-Advance by me

import winsound
import time

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    ' ': '/',      ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '!': '-.-.--'
}

# Beep settings
DOT_DURATION = 100    # milliseconds
DASH_DURATION = 300
FREQUENCY = 800       # Hz

def play_morse_sound(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(FREQUENCY, DOT_DURATION)
        elif symbol == '-':
            winsound.Beep(FREQUENCY, DASH_DURATION)
        elif symbol == '/':
            time.sleep(0.5)
        time.sleep(0.1)  # pause between symbols

def text_to_morse(text):
    text = text.upper()
    morse_code = ''
    index = 0
    while index < len(text):
        char = text[index]
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '? '
        index += 1
    return morse_code.strip()

# Main loop
if __name__ == "__main__":
    user_input = input("Enter text (or type 'exit' to quit): ")
    
    while user_input.strip().lower() != 'exit':
        morse = text_to_morse(user_input)
        print("Morse Code:", morse)
        print("Playing sound...")
        play_morse_sound(morse)
        user_input = input("\nEnter more text (or type 'exit' to quit): ")
    
    print("Goodbye!")
