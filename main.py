# -*- coding: utf-8 -*-
#
#  ____  _____   _____
# |___ \|  __ \ / ____|
#   __) | |  | | (___   _ __  _   _
#  |__ <| |  | |\___ \ | '_ \| | | |
#  ___) | |__| |____) || |_) | |_| |
# |____/|_____/|_____(_) .__/ \__, |
#                      | |     __/ |
#                      |_|    |___/
#
# WELCOME TO 3DS.py!
#
# This is the entrypoint to your cool Python homebrew application!
#
# Just write some code.
# Place this file in the same directory where your 3DS.py
# executable is located and launch the app.
#
import os
import platform

print("Py3DS 1.0 - Powered by 3DS.py")
print("Type ':exit' to quit Py3DS")
lastLine = ""
while 1==1:
    lineofcode = input(">")
    if lineofcode == ":exit":
        exit()
    elif lineofcode == ":clear":
        if platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            os.system("cls")
    elif lineofcode == ":help":
        print(":clear - Clears the screen")
        print(":help - Shows this help screen")
        print(":exit - Closes Py3DS")
        print("Thank you for using Py3DS! - Marko2155")
    else:
        try:
            lastLine = exec(lineofcode)
        except Exception as error:
            print(error)
