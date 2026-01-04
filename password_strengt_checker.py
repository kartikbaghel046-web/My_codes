''' 
Name = Kartik
Roll no. = 2505317
Group = G8
'''

import re

def password_checker():
    print("---------------Welcome to the Password Strenght Checker---------------")

    while True:
        password = input("Enter your password (or type \"exit\" to quit): ")

        if password.lower() == "exit":
            print("Thank you for using my tool")
            break

        result = check_password_strenght(password)
        print(result)


def check_password_strenght(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters"
    
    elif not any(char.isdigit() for char in password):
        return "Weak: Password must contain a digit"
    
    elif not any(char.isupper() for char in password):
        return "Weak: Password must contain a capital character"
    
    elif not any(char.islower() for char in password):
        return "Weak: Password must contain a lower character"
    
    if not re.search(r'[!@#$%^&*_+-/<>.:\|]', password):
        return "Medium: Password must contain a special character"
    
    return "Strong: Your password is secured!"


password_checker()