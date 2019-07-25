# Import libraries we may need
import sys, os, time, signal, webbrowser, platform, subprocess, pyfiglet

#Use pyfiglet to make an easy ASCII logo
greeting = pyfiglet.figlet_format("The Remover", font = "big")
print(greeting)

#Ask the user if they want to search by email or username
def menu():
    print("1. Email \n2. Username \n3. Exit \n")

    opt = input("Please type which you'd like to search (1 or 2) or enter '3' to exit:")
    if opt == "1":
        os.system('cls')
        email()
    elif opt == "2":
        os.system('cls')
        username()
    elif opt == "3":
        exit()
    else:
        os.system('cls')
        print("Please enter a valid input \n")
        menu()

#Ask user for email

def email():
    mail = input("Please enter your email address or type 'r' to return: ")
    if mail == "r":
        os.system('cls')
        menu()
    elif mail == (''):
        print("Invalid input")
        email()
    else:
        webbrowser.open('https://usersearch.org/results_email_basic.php?URL_email=' + mail)
        os.system('cls')
        menu()


#Ask user for username

def username():
    user = input("Please enter your username or type 'r' to return: ")
    if user == "r":
        os.system('cls')
        menu()
    elif user == (''):
        print("Invalid input")
        user()
    else:
        webbrowser.open('https://usersearch.org/results_normal.php?URL_username=' + user)
        os.system('cls')
        menu()

menu()
