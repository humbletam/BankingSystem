import os
import funcstr
# Function calls a questioneer for new user


def info():
    print("Some questions about you...")

    name = input("What is your name? ")
    surname = input("What is your surname? ")
    age = int(input("How old are you? "))
    address = input("What is your adress? ")

    print(f'Welcome {name}!')


def bills():
    print("Bills")
    print("You have 1 unnpayed bill")


def account():
    user_name = "Rustam"
    user_surname = "Zaloldinov"
    user_age = "21"
    user_address = "New 21 street, Bali"
    print("Account Details: ")
    print(user_name)
    print(user_surname)
    print(user_age)
    print(user_address)

    def account_details():
        user_info['Edit(1)', 'EasterEgg(2)']
        print(user_info)

        edit = 1
        egg = 2
        user_chs_if = int(input("Choose a value: "))

        if user_chs_if == edit:
            print("Edit your credentials ")
            user_name = input("Your name: ")
            user_surname = input("Your surname: ")
            user_age = int(input("Your age: "))
            user_address = input("Your Address: ")
            print("Your new credentials")
            print(user_name)
            print(user_surname)
            print(user_age)
            print(user_address)
        elif user_chs_if == egg:
            print("( ✌︎'ω')✌︎✌︎('ω')✌︎")
        else:
            print("Nothing to change")


# Function calls login statement
def login():
    user_log = 'sun'
    user_passwd = '1234'
    userlog_name = 'Rustam'

    print("Sing in")
    log = input("Login: ")
    passwd = input("Password: ")

    if log == user_log:
        if passwd == user_passwd:
            print(f'Welcome {userlog_name}!')
        else:
            print("Password incorrect!")
            passwdfail()
    else:
        print("Login or password incorrect!")
        passwdfail()

# Function calls back login() function


def passwdfail():
    user_log = 'sun'
    user_passwd = '1234'
    userlog_name = "Rustam"

    log = input("Login: ")
    passwd = input("Password: ")

    if log == user_log:
        if passwd == user_passwd:
            print(f'Welcome {userlog_name}!')
        else:
            print("Password incorrect!")
            passwdfail()
    else:
        print("Login or password incorrect!")
        passwdfail()
# Function calls register statement


def registration():
    print("Registration")

    reg_log = input("Login: ")
    reg_passwd = int(input("Password: "))
    info()

# Function calls basic login/register statement depends from user choice


def logres():
    print("Sing in(1) or Sing up(2)...")
    startup = int(input("Choose: "))
    if startup == 1:
        login()
        user_choise()
    elif startup == 2:
        registration()
# Use choise function[bills, account, logout] Logout with choise


def user_choise():
    list_of_chs = ['bills', 'account', 'logout']
    print(list_of_chs)

    user_chs = input("Choose an option: ")

    if user_chs == 'bills':
        bills()
        user_choise()
    elif user_chs == 'account':
        account()
        user_choise()
    elif user_chs == 'logout':
        print("Are you sure?")

        logout_chs = input("Yes or No: ")

        if logout_chs == 'Yes':
            print("Logging out...")
        elif logout_chs == 'No':
            user_choise()
        else:
            print("None of options selected :(")

            user_choise()


# StartUp
print("Welcome in Rustam Bank!")
logres()
funcstr()
