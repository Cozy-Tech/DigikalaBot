from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from kavenegar import *
import time


class CozyDigi:
    def __init__(self):
        self.browser = webdriver.Edge(r"H:\Jupyter\msedgedriver.exe")      
        
    def offer(self,link):
        browser = self.browser
        browser.get(link)
        
        try:
            offer = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'img[class="c-product-gallery__offer-img"]')))
            #             send_sms()
            prtin("SMS sent!")
        except:
            print("There is no Offer on this product :(")
            
    def send_sms(self):
        myapi = "Your Key here"
        api = KavenegarAPI(myapi)
        params = {'sender': '1000596446', 'receptor': 'your phone number',
                  'message': 'محصولت تخفیف خورده! بدو برو بخر!!! =)))))))'}
        response = api.sms_send(params)
    
        
cozytech = CozyDigi()

if __name__ == "__main__":
    while True:
        cozytech.offer("Drop your link here")
        time.sleep(21600)
