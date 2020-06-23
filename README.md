# Wholefoods-Delivery-Slot-Alert
A simple python script that alerts when there are available delivery slots. 
This script was created during the peak uncertainty of COVID-19 and the time when grocery deliveries were not being able to keep up with demand. Delivery slots were rare and sporadic leading to time wasted refreshing the checkout page.

# Project Overview 
* A simple script that uses Selenium to automate the google chrome browser to refresh the checkout page at regular intervals
* Script uses windows sound and beep system to make an audio cue when a delivery slot is found to notify the user
* Also prints out the earliest slots today and tomorrow if available on the console
 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** Selenium, tkinter.messagebox, sys, time, winsound 
**Additional Requirements:** Chromedriver that is compatible with your Google Chrome version.
link: https://chromedriver.chromium.org/downloads


## Instructions on how to use
Before using this script, make sure you already have all the items you want in your cart and ready to check out.

* **After initiating the script, you will be redirected to the Amazon main landing page and an Alert will pop up. Make sure to click ok or the script will be paused**



![alt text](https://github.com/kevin7303/Whole-foods-Delivery-Slot-Alert/blob/master/Alert.PNG "alert")

* **Next, you will have 1 minute to login to your Amazon account and proceed to the checkout page**



![alt text](https://github.com/kevin7303/Whole-foods-Delivery-Slot-Alert/blob/master/Whole%20Foods%20Login.png "login")



* **Once at the checkout page, the script will periodically refresh the browser and check for available time slots. If a timeslot is found, a beep noise will alert you and the script will stop running. You do not need to monitor the page, feel free to minimze it.**

![alt text](https://github.com/kevin7303/Whole-foods-Delivery-Slot-Alert/blob/master/Whole%20Foods%20Checkout.png "checkout")
