import pandas as pd
import numpy as np
import datetime
import smtplib
import schedule
import time
import ssl
import pywhatkit
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
df=pd.read_excel("webApi_database.xlsx")
today=datetime.date.today().strftime("%m-%d")
df['Mobile']='+' + df['Mobile'].astype(str)
df['mod_date']=df['Date'].dt.strftime("%m-%d")
email_id='spo.cocos22@gmail.com'
email_pass='fzkdkipgvkadpcom'
message="Happy Birthday,IIT Kanpur wishes you a very Happy birthday"
fb_id='ciniwey711@soremap.com'
fb_pass='asdf123asdf'
def email_sender(subject, recipients, name):
    receiver = recipients
    sender=email_id
    sender_password=email_pass
    
    msg=MM()
    msg['Subject'] = subject +' '+ str(name) + '!'
    HTML="""
    <html> 
        <body>
        <h1>Happy Birthday </h1></br>
        <p>IIT Kanpur wishes you a very Happy birthday</p>
        </body>
    </html>
    """
    
    MTObj=MT(HTML,"html")
    msg.attach(MTObj)
    
    SSL_context=ssl.create_default_context()
    
    server=smtplib.SMTP_SSL(host="smtp.gmail.com",port=465,context=SSL_context)
    
    server.login(sender,sender_password)
    
    server.sendmail(sender,receiver,msg.as_string())
def whatsapp_sender(number,message):
    t = time.localtime()
    current_time_hrs =int(time.strftime("%H", t)) 
    current_time_min=int(time.strftime("%M", t))
    if(current_time_min<55):
        pywhatkit.sendwhatmsg(number,message,current_time_hrs,current_time_min+2)
    else:
        pywhatkit.sendwhatmsg(number,message,(current_time_hrs+1)%12,current_time_min+2)
    time.sleep(2)  # Wait for 2 seconds
    pyautogui.click(1399, 871,interval=1)  # Perform mouse click at coordinates
    # print('message sent to',name)
def fb_sender(id,message):
    # Provide the path to the ChromeDriver executable
    chromedriver_path = "/Users/siddhant/Coding_Lectures/Vas_Ventures/chromedriver_mac_arm64/chromedriver"

    # Configure Selenium to use Chrome browser with the specified ChromeDriver path
    driver = webdriver.Chrome(executable_path=chromedriver_path)

    # Provide your Facebook credentials
    username = fb_id
    password = fb_pass

    # Provide the friend's profile URL and birthday message
    friend_profile_url = id
    birthday_message = message
    # Log in to Facebook
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("pass").send_keys(Keys.RETURN)

    # Navigate to the friend's profile
    driver.get(friend_profile_url)
    time.sleep(3) 
    # Click on the "Write something on {Friend's Name}'s timeline" section
    write_post_box = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div")
    ActionChains(driver).move_to_element(write_post_box).click().perform()
    time.sleep(2) 
    # Write and post the birthday message
    # post_text_area = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]")
    post_text_area=driver.switch_to_active_element()
    post_text_area.send_keys(birthday_message)
    time.sleep(2)  # Wait for the textarea to adjust its size
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div").click()

    # Close the browser
    driver.quit()

def operation():
    # for i in range(0,len(df)):
    for i in range(0,3):
        bday= df['mod_date'][i]
        if bday==today:
            name= df['Name'][i]
            email= df['Email'][i]
            number= df['Mobile'][i]
            id=df['facebook'][i]
            email_sender(message,email,name)
            fb_sender(id,message) 
            whatsapp_sender(number,message)            
schedule.every(24).hours.do(operation)
while(True):
    schedule.run_pending()
    time.sleep(1)
    