# Symptom Survey Automation

## About
This simple python script automates the process of filling out UC Davis' symptom survey. Typically, one would be redirected through 6 or 7 webpages before reaching the actual symptom survey. Redirecting the user through these pages requires them to login to their UC Davis CAS account, click through multiple buttons, and perform 2FA with Duo.

As one can see, performing this everyday can get redundant and tedious. With this script, all the user needs to do is: enter their Kerberos username and password, indicate whether or not they have any symptoms or concerns (a simple yes/no), and perform 2FA with Duo.

Some may be concerned with the fact that filling out the answers to the symptom survey is being automated and that the users will not see the questions themselves. The script will only automate the survey if the users are not experiencing any new symptoms or concerns. If they are, they will have to fill out the survey manually.

## Required libraries
### selenium
### webdriver-manager
### tkinter

## Running the script
Ensure that you are in the root of the repository. 

Run the command: python src/app.py.

From there, a GUI popup will prompt for your Kerberos username, password, and whether or not you have any new symptoms or concerns regarding COVID.

## Things to note
At the current momemnt, 2FA via Duo appears to be pretty difficult to automate. Running the script multiple times in a short period of time (ie. approximately 1 minute) may not trigger the "Send a Push" button in Duo. To bypass this issue, ensure that you "Refresh Passcode" in your Duo application.