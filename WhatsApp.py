import pywhatkit
import time

print("Welcome to WhatsApp Messenger Automation")
print("This program will send a message to a mobile number instantly")
print("Note: Please enter the mobile number with country code. For example: +91 1234567890")
print("Note: You must have to be logged in to web.whatsapp.com on your default browser")
print("Note: You must have to have Python 3.11 installed on your computer")
print("Note: You must have to be connected to the internet")
print("Please enter the details below")

while (0 == 0):
    eNum = input("Enter the mobile number to message:- ")
    eMsg = input("Enter the message to send:- ")
    pywhatkit.sendwhatmsg_instantly(eNum, eMsg)
    time.sleep(5)
