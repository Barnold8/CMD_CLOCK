from datetime import datetime
from termcolor import colored
import pyfiglet
import os
import time
import sys
import platform

def getTime():

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

def spacer(string):

    l = []

    for i in range(len(string)):
        l.append(string[i])
        l.append(" ")

    return l

def sysType():

    if(platform.system != "Windows"):
        return "clear"
    else:
        return "cls"

def info():

    cols = ["grey","red","green","yellow","blue","magenta","cyan","white"]

    print("Program usage:\n\n\tCMD_CLOCK [font] [color]\n\tNOTE: The command line args are completly optional, you can just run CMD_CLOCK.py")
    print("\n\nTo see a list of fonts write CMD_CLOCK fonts")
    print("\nDue to the limited usage of the termcolor library used for this app, only basic colours are available for the color option")
    print("\nExamples for the color option are:\n")
    for i in range(len(cols)):
        print(cols[i])
    


def main():

    color = "white"
    if len(sys.argv) == 2 and sys.argv[1].lower() == "help":
        info()
        exit()
    elif len(sys.argv) < 2:
        font = "slant" # default font
    elif len(sys.argv) == 3: # If user defines font and color
        font = sys.argv[1]
        color = sys.argv[2]
    elif sys.argv[1].lower() == "fonts": # if user asks for fonts
        x = pyfiglet.FigletFont.getFonts()
        for i in range(x):
            print(x[i])
        exit()
    else: # set font to first arg
        font = sys.argv[1]

    clear = sysType()

    while(1):
        os.system("clear")
        try:
            print(colored(pyfiglet.figlet_format(spacer(getTime()),font=font),color))
        except Exception as e:
            print("Error: " + str(e) + "\nProgram usage: CMD_CLOCK.py [font] [color]\nCheck color name or font type\nUse 'CMD_CLOCK.py help' for help\nProgram exiting...")
            exit()

        time.sleep(1)

    

        
    


main()
