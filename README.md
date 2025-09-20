Morse Code – Advanced Edition

This is a Python program that converts text into Morse code and plays it as audible beeps using the winsound module (Windows only). It supports letters, digits, and some punctuation.

⚡ Features

Text-to-Morse conversion for:

A–Z letters

0–9 digits

Space (represented as /)

Basic punctuation: , . ? !

Sound playback using system beeps:

Dot (.) → short beep (100ms)

Dash (-) → long beep (300ms)

Word gap (/) → pause (0.5s)

Prints Morse code on screen and plays sound simultaneously.

Interactive input loop: keep entering text until typing exit.

🕹️ How It Works

Dictionary (MORSE_CODE_DICT)

Maps each supported character to its Morse code equivalent.

Conversion (text_to_morse)

Converts user input into a Morse code string.

Unknown characters are replaced with ?.

Playback (play_morse_sound)

Loops through the Morse code symbols.

Plays a beep for . and -, pauses for spaces (/).

Main Loop

Prompts the user for input.

Displays and plays the Morse code.

Runs until the user types exit.

📂 Example

Input:

Hello World


Output:

Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Playing sound...


And you’ll hear beeps:

Short beeps for dots

Long beeps for dashes

Pause between words

🔧 Requirements

Python 3.8+

winsound (only available on Windows)

time (standard library)

▶️ Run the Morse Code-P1-Advance.py                                                                            
----------------------------------------
Morse Code – Intermediate Edition

This is a Python program that converts text into Morse Code using a dictionary lookup. It works in the console and supports letters, digits, and some punctuation.

⚡ Features

Text-to-Morse conversion for:

Letters A–Z

Digits 0–9

Space ( → /)

Punctuation: , . ? !

Unknown characters are replaced with ?.

Interactive loop: keep converting text until typing exit.

🕹️ How It Works

Dictionary (MORSE_CODE_DICT)

Maps each supported character to its Morse Code representation.

Conversion Function (text_to_morse)

Converts user input into Morse Code.

Automatically converts all text to uppercase before translation.

Adds spaces between Morse symbols for readability.

Main Program

Continuously asks for input.

Prints the converted Morse Code.

Ends when the user types exit.

📂 Example

Input:

Hello, World!


Output:

Morse Code: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- 

🔧 Requirements

Python 3.8+ (no external libraries needed).

▶️ Run the Morse Code-P1-Intermediate.py
----------------------------------
Morse Code – Basic Edition

This is the Basic version of a Python Morse Code translator.
It converts plain text into Morse Code and prints the result in the console.

⚡ Features

Converts text to Morse Code for:

Letters A–Z

Digits 0–9

Space ( → /)

Punctuation: , . ? !

Unknown characters are replaced with ?.

Works in a single run: enter text once, get the Morse translation.

🕹️ How It Works

Dictionary (MORSE_CODE_DICT)

Maps letters, digits, and symbols to Morse Code.

Conversion (text_to_morse)

Converts input text to uppercase.

Iterates through each character and looks it up in the dictionary.

Joins Morse symbols with spaces.

Main Program

Prompts the user for text input.

Prints the Morse Code equivalent.

📂 Example

Input:

SOS


Output:

Morse Code: ... --- ...

🔧 Requirements

Python 3.8+ (no external libraries required).

▶️ Run the Morse Code-P1-basic.py
--------------------------------------------
