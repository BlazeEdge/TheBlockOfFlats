'''
The block of flats
author: blaze_edge
description:
This game is about accumulating resources and building houses
vesion: 0.5
'''
import time
import os
from rich import *
from functions import *
# IMPORTS

banner = banner()
skint = 10
houses = 0
# VARIABLES

try:
    os.system("cls")
except:
    os.system("clear")

time.sleep(1)
print("Welcome!")
load_anim()
try:
    os.system("cls")
except:
    os.system("clear")
print(banner)

while True:
    command = input("\n>>> ").lower()
    if command == "get-skint":
        print(f"You got [bold green]{(0+5)*houses}[/bold green] skints...")
        skint = skint + ((0 + 5) * houses)

    elif command == "balance":
        print(f"The amount of your skint: [bold green]{skint}[/bold green]")

    elif command == "houses":
        print(f"You have [bold green]{houses}[/bold green] houses...")

    elif command == "build-house":

        if skint >= 10:
            skint = skint - 10
            houses = houses + 1
            print("The house was built")

        else:
            print("[bold red]Not enough skint[/bold red]")
    else:
        print("[bold red]Wrong command![/bold red]")
# MAIN CYCLE