#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        letter_ord = ord(letter)
        if(97 <= letter_ord <= 122):
            letter_ord -= 32
            letter = chr(letter_ord)
        print(letter, end='')
    print()
