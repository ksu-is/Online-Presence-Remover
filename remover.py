# Import libraries we may need
import sys, os, time, signal, webbrowser, platform, subprocess, pyfiglet

greeting = pyfiglet.figlet_format("The Remover", font = "big")
print(greeting)

def menu():
    print("1. Email \n2. Username \n")

    OPT = input("Please select which you'd like to search:")

menu()
