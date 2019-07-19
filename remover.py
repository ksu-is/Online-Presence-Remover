# Import libraries we may need
import sys, os, time, signal, webbrowser, platform, subprocess, pyfiglet

#Use pyfiglet to make an easy ASCII logo
greeting = pyfiglet.figlet_format("The Remover", font = "big")
print(greeting)

#Ask the user if they want to search by email or username
def menu():
    print("1. Email \n2. Username \n")

    OPT = input("Please select which you'd like to search:")

menu()
