from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox as mb

# user input
tkinter_root = tk.Tk()
tkinter_root.withdraw()
tkinter_root.geometry('640x380')
username = simpledialog.askstring(title="Kerberos", prompt="UCD Kerberos")
password = simpledialog.askstring(title="Kerberos", show="*", prompt="Kerberos Password")                            
symptoms_exist = mb.askyesno(title="Symptoms or Concerns", message="Do you have current symptoms or concerns regarding COVID?")
if symptoms_exist:
    quit()

# chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://campusready.ucdavis.edu/symptom-survey')

# Campus Ready Webpage
survey_button = driver.find_element_by_xpath('//*[@id="block-affiliatesymptomsurvey"]/section/div/div[2]/p/a')
survey_button.click()

# cas.ucdavis login
username_field = driver.find_element_by_xpath('//*[@id="username"]')
username_field.send_keys(username)
password_field = driver.find_element_by_xpath('//*[@id="password"]')
password_field.send_keys(password)
login_button = driver.find_element_by_xpath('//*[@id="submit"]')
login_button.click()

# Duo
iframe = driver.find_element_by_xpath("//iframe[@id='duo_iframe']")
driver.switch_to.frame(iframe) # switching to Duo iframe
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@class, 'auth-button') and contains(., 'Send Me a Push')]"))).click()
# driver.switch_to.default_content() # switching out of iframe

# Davis HEM
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ctl03']/div[2]/div/a"))).click()
continue_button = driver.find_element_by_xpath("//*[@id='mainbody']/div[2]/div[1]/div/div[2]/a")
continue_button.click()

# Symptom Survey
q1 = driver.find_element_by_xpath("//*[@id='mainbody']/main/form/div[2]/fieldset/div/div[2]/div")
q1.click()
q2 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[3]/fieldset/div/div[2]/div')
q2.click()
q3 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[4]/fieldset/div/div[2]/div')
q3.click()
q4 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[5]/fieldset/div/div[2]/div')
q4.click()
q5 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[6]/fieldset/div/div[2]/div')
q5.click()
q6 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[7]/fieldset/div')
q6.click()
submit_survey = driver.find_element_by_xpath('//*[@id="mainbody"]/footer/div/div[2]/input')
submit_survey.click()

driver.quit() # closing the browser and ends WebDriver session