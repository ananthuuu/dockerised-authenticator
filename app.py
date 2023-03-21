import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'

import time
import requests
import pyotp
import subprocess

sitename="https://stockmate.srshti.co.in"

def queryauth():
    url = sitename+"/queryauth"
    
    payload = {}
    r = requests.post(url, data=payload)
    r=r.json()
    # print(r['objarr'])
    return r["objarr"]



class FirstSampleTest():

  
        
    def tearDown(self):
        self.driver.quit()

    def test_demo_site(self):
        # Set up video recording using ffmpeg
        output_file = 'test_video.mp4'
        cmd = ['ffmpeg', '-y', '-f', 'x11grab', '-s', '1920x1080', '-i', ':99', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', '-r', '25', output_file]
        process = subprocess.Popen(cmd)

        # Wait for ffmpeg to start recording
        time.sleep(2)
        self.users=queryauth()
        output_file = 'test_video.mp4'
        for user in self.users:
            try:
                 
                print("Starting web driver")
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument(f'user-agent={user_agent}')
                self.driver = webdriver.Chrome(options=chrome_options)
                self.actions = ActionChains(self.driver)
                self.actions2 = ActionChains(self.driver)
                driver = self.driver
                driver.implicitly_wait(30)
                driver.set_page_load_timeout(30)
                driver.set_window_size(1920, 1080)
    
                # Url
                print('Loading URL')
                driver.get("https://stockmate.srshti.co.in/login")
                driver.save_screenshot('login.png')
                # Let's click on a element
                driver.find_element(By.NAME, "username").send_keys(user["name"])
                driver.find_element(By.NAME, "password").send_keys(user["password"])
            
                location = driver.find_element(By.NAME,"login")
                location.click()
                print("Loading Home Page")
                driver.save_screenshot('homepage.png')
                
                # Wait for the element to be visible
                element_present = EC.presence_of_element_located((By.XPATH, "//h3[text()='Approve Trading for today']"))
                WebDriverWait(driver, 10).until(element_present)
                driver.save_screenshot('homepage1.png')
                location = driver.find_element(By.XPATH, "//h3[text()='Approve Trading for today']")
                location.click()
                time.sleep(10)
                print("Loading Fyers Page")
                driver.save_screenshot('fyerspage.png')
                driver.find_element(By.NAME, "fy_client_id").send_keys(user["username"])
                driver.find_element(By.ID, "clientIdSubmit").click()
                time.sleep(10)
                print("After Fyers Page")
                totp = pyotp.parse_uri(user["totp"])
                print(totp.now())
                totp = str(totp.now())
                self.actions.send_keys(totp)
                self.actions.perform()
                time.sleep(3)
                driver.find_element(By.ID, "confirmOtpSubmit").click()
                
                time.sleep(3)
                self.actions2.send_keys(user["otp"])
                self.actions2.perform()
                driver.find_element(By.ID, "verifyPinSubmit").click()
                time.sleep(10)
                
            except Exception as e:
                print(f"Error occurred for user {user}: {str(e)}")
                
            finally:
                if self.driver is not None:
                    self.driver.quit()
                    print("Quitting web driver")
                
                
                time.sleep(5)
                print("Finished iteration")
                process.stdin.write(b'q\n')

test=FirstSampleTest()
test.test_demo_site()

# docker cp b105f5d1a338:/homepage1.png . 