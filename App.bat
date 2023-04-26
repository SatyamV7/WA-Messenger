@echo off
title WhatsApp Messenger Automation
color 0a
echo Welcome to WhatsApp Messenger Automation
echo This program will send a message to a mobile number instantly
echo Note: Please enter the mobile number with country code. For example: +91 1234567890
echo Note: You must have to be logged in to web.whatsapp.com on your default browser
echo Note: You must have to have Python 3.11 installed on your computer
echo Note: You must have to be connected to the internet
echo Please enter the details below
:execute
%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe .\App.py
goto execute
