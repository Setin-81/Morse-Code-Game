# Dictionary for Morse Code-Basic by me
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

def text_to_morse(text):
    text = text.upper()  # Convert to uppercase
    morse_code = ''
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '? '  # Unknown character
    return morse_code.strip()

# --- Main Program ---
if __name__ == "__main__":
    user_input = input("Enter text to convert to Morse Code: ")
    result = text_to_morse(user_input)
    print("Morse Code:", result)