#Created by: Kevin Wang Ji
#Date 5/10/2020
#This script will alert the user of a delivery slot when one is available. Made for the COVID Quarantine period where everyone is ordering groceries
#This script speciically uses Google Chrome as the browser to crawl

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import tkinter as tk
from tkinter import messagebox
import sys
import time
import winsound


#Define Website to crawl and also the ChromeDriver location in your computer
browser = webdriver.Chrome('C:\\Users\\Kevin Wang\\Downloads\\chromedriver_win32\\chromedriver.exe')
#Smile.Amazon gives a portion of the purchase dollars to a charity of your choice
browser.get("https://smile.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1")

####################################################################
# Helper Functions
def login_alert():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Login", "Please Log in to you Amazon Account and proceed to checkout page")

def getslots():
    today = browser.find_element_by_class_name('ufss-date-select-toggle-text-month-day')
    time_slot = browser.find_elements_by_xpath('//*[@id="20200622"]/div[1]/div/ul/li/span/span/div/div[1]/div[1]/span')
    tomorrow = browser.find_elements_by_xpath('//*[@id="shipoption-select"]/div/div/div/div/div[1]/div[2]/div[2]/div/ul/li[2]/span/span/span/button/div/div[2]')
    time_slot_tom = browser.find_elements_by_xpath('//*[@id="20200622"]/div[2]/div/ul/li[1]/span/span/div/div[1]/div[1]/span')
    
    #Printing Message
    print('The earliest time slot for today:', today.text, 'is', time_slot[0].text)
    print('The earliest time slot for tomorrow:', tomorrow[0].text, 'is', time_slot_tom[0].text)


def check_slots(no_slots):
    while no_slots:
        try:
            availability = browser.find_elements_by_class_name("ufss-date-select-toggle-text-availability")
            time.sleep(2)
            if availability.text == "Not available":
                time.sleep(1)
                browser.refresh()
                print("Not available... refreshing")
            else:
                winsound.Beep(freq, dur)
                print("Available")
                getslots()
                no_slots = False
                print("Loop done")
        except NoSuchElementException:
            pass
        except AttributeError:
            winsound.Beep(freq, dur)
            print("Available")
            getslots()
            no_slots = False
            print("Script done")
##################################################################

# Beep noise frequency is set to 500Hz
freq = 500

# Beep noise duration is set to 100 milliseconds
dur = 1000

#This opens up an alert textbox directing the user to log in and go to the checkout page. If you do not press OK the code does not initiate
login_alert()

#Initial no_slot value
no_slots = True

#gives 1 minute for the user to go through the log in and checkout page
time.sleep(60)

#Refreshes the browser to make sure no error
browser.refresh()
print("First refresh")

#Call check_slots
check_slots(no_slots)

