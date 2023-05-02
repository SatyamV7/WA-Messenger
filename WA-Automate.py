import webbrowser
import pyautogui as PyAutoGUI
import time
PyAutoGUI.FAILSAFE = False
mobNum = input("Enter the mobile number to message:- ")
msgLimit = int(input("Enter the number of messages you want to send:- "))
msgText = input("Enter the message you want to send:- ")
webbrowser.open(f"https://web.whatsapp.com/send?phone={mobNum}")
i = 0
time.sleep(30)
while i < msgLimit:
    PyAutoGUI.write(msgText, interval=0)
    PyAutoGUI.press("enter")
    i += 1
time.sleep(5)
