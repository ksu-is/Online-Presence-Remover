# Import libraries we may need
import sys, os, time, signal, webbrowser, platform, subprocess, pyfiglet

#Use pyfiglet to make an easy ASCII logo
greeting = pyfiglet.figlet_format("The Remover", font = "big")
print(greeting)

#Ask the user if they want to search by email or username
def menu():
    print("1. Email \n2. Username \n")

    opt = input("Please select which you'd like to search (1 or 2):")
    if opt == "1":
        email()
    elif opt == "2":
        username()
    else:
        print("Please enter a valid input \n")
        opt()

#Ask user for email

def email():
    mail = input("Please enter your email address: ")
    webbrowser.open('https://usersearch.org/results_email_basic.php?URL_email=' + mail)
    menu()

#Ask user for username

def username():
    user = input("Please enter your username: ")
    webbrowser.open('https://usersearch.org/results_normal.php?URL_username=' + user)
    menu()
menu()
