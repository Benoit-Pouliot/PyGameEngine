import sys
import os

# seek the attribute name in object, if none, pass
def seekAtt(objectLocal, nameAttribute):
    try:
        return getattr(objectLocal, nameAttribute)
    except AttributeError:
        return None

# quit game ( NEVER USE quit() or exit() ), we use sys.exit()
def quitGame():
    sys.exit()

# For each main, do this
def initMain():
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
         os.chdir(sys._MEIPASS)