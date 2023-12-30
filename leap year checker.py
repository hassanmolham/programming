import os
import subprocess

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls' if os.name == 'nt' else 'echo -e "\\033c"')

clear_terminal()
year= int(input("enter a year u want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"this {year} is a leap year!!")
        else:
            print("this is not a leap year")
    else:
        print(f"this {year} is a leap year!!")
else:
    print("this is not a leap year")