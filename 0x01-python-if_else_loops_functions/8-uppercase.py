#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
             uppercase_c += chr(ord(c) - 32)
             print(uppercase_c)
uppercase()
