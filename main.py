from morsecode import letters_numbers_punctuation, morseCode
import keyboard
import time
import winsound
import os
from art import *

is_typing = True
morsecodeConverted = ""
morseCharacters = []
inputText = ""

def playMorseCode(morsecodeConvertedSymbols):
    for character in morsecodeConvertedSymbols:
        if character == '•':
            winsound.Beep(1000,300)
        elif character == '-':
            winsound.Beep(1000,600)
        elif character == ' ':
            time.sleep(0.5)
        time.sleep(0.1)

def TextToMorseCode(text):
    morsecodeConverted = ""
    for character in text:
        morsecodeConverted += letters_numbers_punctuation[f"{character.upper()}"]
    print(morsecodeConverted + '\n')
    playMorseCode(morsecodeConverted)

def MorseCodeToText(text):
    morseCharacters = []
    morsecodeConverted = ""
    morseCharacters = text.split(" ")
    for code in morseCharacters:
        morsecodeConverted += morseCode[f"{code}"]
    print(morsecodeConverted + '\n')
    playMorseCode(text)

def PrintOptions():
    print("--OPTIONS--")
    print("a. Enter 1 to translate from text to morse code.")
    print("b. Enter 2 to translate from morse code to text.")
    print("c. Press 3 to exit the program.")

def EnterInput(message):
    time.sleep(0.5)
    text = input(message)
    # text = text[1:]
    return text

tprint("MORSE CODE TRANSLATOR")
PrintOptions()

while is_typing:

    if keyboard.is_pressed("1"):
        input()
        os.system('cls')
        while not inputText:
            inputText = EnterInput("\nPlease type a text: ")
        TextToMorseCode(inputText)
        PrintOptions()

    if keyboard.is_pressed("2"):
        input()
        os.system('cls')
        while not inputText:
            inputText = EnterInput("\nType Morse code using '•','-', using a spaces between letters and '/' between words : ")
        MorseCodeToText(inputText)
        PrintOptions()

    if keyboard.is_pressed('3'):
        is_typing = False

    inputText = ""