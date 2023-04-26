import pywhatkit
import time

eNum = input("Enter the mobile number to message:- ")
eMsg = input("Enter the message to send:- ")

pywhatkit.sendwhatmsg_instantly(eNum, eMsg)
time.sleep(5)
