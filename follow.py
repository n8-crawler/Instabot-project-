# from instapy import InstaPy
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
from PIL import ImageFont
import shutil
from PIL import ImageDraw
import time
from instabot import Bot
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def homepage(url,taskname,name=None):

    driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('_ranjan_dash_')
    driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('Rdash@2502')
    driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
    time.sleep(5)
    newurl = url+name
    if name is not None:
        follower_page(url,new_url=newurl)
        return
    else:
        return


def follower_page(url,new_url):
    driver.get(new_url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    driver.find_element(By.XPATH,"//div[contains(text(),Follow)]//preceding::div//preceding::button").click()

    time.sleep(2)
    driver.refresh()
    driver.fullscreen_window()
    time.sleep(3)
    filename = os.path.abspath('screenshots')+task_name+str(random.randint(1,10000))+'.png'
    screenshot = driver.save_screenshot(filename)

    img = Image.open(filename)
 
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('C:\\Users\\System-Pc\\Desktop\\arial.ttf', 100)

    # Add Text to an image
    I1.text((40, 40), task_name,font=myFont, fill=(255, 0, 0))
    
    # Display edited image
    
    # Save the edited image
    img.save(filename)

    scroll_till_end()    

    soup = BeautifulSoup(driver.page_source,'html.parser')
    elements = driver.find_elements(By.CLASS_NAME,'_aabd')
    els = soup.find_all('div',{'class':'_aabd'})
    for e in els:
        url_tag = e.find('a',href=True)
        print(url+url_tag['href'])
        driver.get(url+url_tag['href'])
        driver.fullscreen_window()

        soup = BeautifulSoup(driver.page_source,'html.parser')

        time.sleep(5)
        driver.find_element
        like = driver.find_elements(By.CSS_SELECTOR,"button[class='_abl-']")
        for l in like:
            temp = l.get_attribute('innerHTML')
            inner = BeautifulSoup(temp,'html.parser')
            xxx = inner.find('svg',{'aria-label':'Like'})
            if xxx: 
                l.click()
                screenshot = driver.save_screenshot(os.path.abspath('screenshots')+'\m9_task'+str(random.randint(1,10000))+'.png',)
                break

                  
        time.sleep(2)
    return

        
def scroll_till_end(time_pasuse=5):
        SCROLL_PAUSE_TIME = time_pasuse

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height  


driver=webdriver.Chrome()
url = "https://www.instagram.com/"
username = ''
password = ''

driver.get(url)
driver.fullscreen_window()
time.sleep(3)
options = Options()
options.add_argument('-disable-popup-blocking')
profile_name = 'krishi_mishra'
task_name = "LIKE"
shutil.rmtree(os.path.abspath('screenshots'))
time.sleep(1)
os.mkdir('./screenshots')
if len(username)>0 and len(password)>0:
    homepage(url,task_name,profile_name)
