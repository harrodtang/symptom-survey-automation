# Symptom Survey Automation

## About
This simple python script automates the process of filling out UC Davis' symptom survey. Typically, one would be redirected through 6 or 7 webpages before reaching the actual symptom survey. Redirecting the user through these pages requires them to login to their UC Davis CAS account, click through multiple buttons, and perform 2FA with Duo.

With this script, all the user needs to do is: enter their Kerberos username and password, indicate whether or not they have any symptoms or concerns (a simple yes/no), and perform 2FA with Duo.

## Required libraries
### selenium
### webdriver-manager
### tkinter

## Running the script
Ensure that you are in the root of the repository. 
Run the command: python src/app.py
From there, a GUI popup will prompt for your Kerberos username, password, and whether or not you have any new symptoms or concerns regarding COVID.

## Things to note/TODO
At the current momemnt, 2FA via Duo appears to be pretty difficult to automate. Running the script multiple times in a short period of time (ie. approximately 1 minute) may not trigger the "Send a Push" button in Duo. To fix this issue, ensure that you "Refresh Passcode" in your Duo application.