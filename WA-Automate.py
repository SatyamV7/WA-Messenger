import webbrowser
import pyautogui as pyAutoGUI
import time
mobNum = input("Enter the mobile number to message:- ")
msgLimit = int(input("Enter the number of messages you want to send:- "))
msgText = input("Enter the message you want to send:- ")
webbrowser.open(f"https://web.whatsapp.com/send?phone={mobNum}")
i = 0
time.sleep(30)
while i < msgLimit:
    pyAutoGUI.write(msgText, interval=0)
    pyAutoGUI.press("enter")
    i += 1
time.sleep(5)