    #-*- coding: utf-8 -*-
import os
os.system("sudo apt-get install figlet toilet")
try:
    class col:
        violet = '\033[95m'
        blue = '\033[94m'
        green = '\033[32m'
        orange = '\033[93m'
        red = '\033[91m'
        reset = '\033[0m'
        bold = '\033[1m'
        underlined = '\033[4m'
    os.system("figlet YourShell")
    print("█▓▒▒░░░YourShell░░░▒▒▓█")
    print(" ")
    wait = input("Enter to start")
    os.system("clear")
    while True:
        color = input("Enter the color you want or type 'show colors' to show a list of colors -» ")
        if color == "show colors":
            print(col.violet + "Violet" + col.reset)
            print(" ")
            print(col.blue + "Blue" + col.reset)
            print(" ")
            print(col.green + "Green" + col.reset)
            print(" ")
            print(col.orange + "Orange" + col.reset)
            print(" ")
            print(col.red + "Red" + col.reset)
            print(" ")
            print(col.bold + "Bold" + col.reset)
            print(" ")
            print(col.underlined + "Underlined" + col.reset)
            print(" ")
            print(col.reset + "Reset (to reset the font col)" + col.reset)
            print(" ")

        elif str(color) == "Violet":
            print(col.violet + " ")
            break
        elif str(color) == "Blue":
            print(col.blue + " ")
            break
        elif str(color) == "Green":
            print(col.green + " ")
            break
        elif str(color) == "Orange":
            print(col.orange + " ")
            break
        elif str(color) == "Red":
            print(col.red + " ")
            break
        elif str(color) == "Violet":
            print(col.violet + " ")
            break
        elif str(color) == "Bold":
            print(col.bold + " ")
            break
        elif str(color) == "Underlined":
            print(" " + col.underlined)
            break
        elif str(color) == "Reset":
            print(" " + col.reset)
            break
        else:
            print("Oh no! Something went wrong!")

    #Part 2
    print("Next up: Set up your prefix: ")
    while True:
        pre = input("New Prefix: ")
        if pre == "":
            print("Enter something!")
        else:
            print("Prefix set!")
            break
    while True:
        print("Do you want a root shell? (Y/n)")
        root = input("Choose: ")
        sudo = ""
        if root == "Y":
            sudo = "sudo "
            break
        elif root == "n":
            sudo = ""
            break
        else:
            print("Something went wrong :(")
    print("Done! Enjoy your personalized Shell!")
    print(str(sudo))
    while True:
        shell = input(str(pre))
        os.system(str(sudo) + str(shell))
        shell = ""
except Exception as e:
    print(str(e))
