from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv
import os
import requests
class ZillowHouseSearch:
    def __init__(self):
        # Class attributes for the configuration
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.parent_directory = os.path.abspath(os.path.join(self.current_directory,".."))
        self.env_path = self.parent_directory + r"\.env"
        load_dotenv(self.env_path)
        self.email = os.getenv("EMAIL")
        self.account_password = os.getenv("ACCOUNT_PASSWORD")
        self.phone_number = os.getenv("PHONE_NUMBER")
        self.account_username = os.getenv("ACCOUNT_USERNAME")
        self.sheety_email = os.getenv("SHEETY_EMAIL")
        self.page_load_wait = 4  # Default PAGE_LOAD_WAIT
        self.google_spreadsheet_link = r"https://docs.google.com/spreadsheets/d/1JB6F0aqS1Fcx9-FaxAeEBBQmOsxcaSKGI7qDH1H8x0A/edit?resourcekey=&gid=730862298#gid=730862298"
        self.google_form_link  = r"https://docs.google.com/forms/d/e/1FAIpQLScc-iHfBN9fLAZ8hvdXOaDBHRGcnntoNMxwCX9z73jPBy8AjA/viewform?usp=sharing"
        self.addresses = []
        self.prices  = []
        self.links = []
        self.info_list = []
        
        response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
        self.soup = BeautifulSoup(response.text,"html.parser")
        
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://appbrewery.github.io/Zillow-Clone/")
    def login(self):
        time.sleep(self.page_load_wait)
        while True:
            try:
                time.sleep(1.5)
                input_email = self.driver.find_element(By.CSS_SELECTOR,value="input[id='reg-login-email']")
                input_email.send_keys(self.email)
                input_password = self.driver.find_element(By.CSS_SELECTOR,value="input[id='inputs-password']")
                input_password.send_keys(self.account_password)
                submit = self.driver.find_element(By.CSS_SELECTOR,value="input[type='submit']")
                submit.click()
                
                
                break
            except NoSuchElementException:
                continue_program = input("Unexpected pop-up/verfication popped up, close/resolve them then type anything to retry.")
                continue
    def get_buildings_info(self):
        time.sleep(1)
        
        
        

        all_building_listings = self.soup.find_all("article")
        for building_listing in all_building_listings:
            building_address = building_listing.address.string
            building_price = building_listing.find("span",attrs = {"data-test":"property-card-price"}).string.split("/")[0]
            #There are some with "+"s like $2,875+/mo   
            if "+" in building_price:
                building_price = building_price.split("+")[0]
                
            building_link = building_listing.a["href"]
            print(building_address,building_price,building_link)
            self.addresses.append(building_address)
            self.prices.append(building_price)
            self.links.append(building_link)
            current_info_dictionairy = {"address": building_address,
                                        "price": building_price,
                                        "link": building_link,}
            self.info_list.append(current_info_dictionairy)
        for listing in self.info_list:
            print(listing["address"],listing["price"],listing["link"])
    def fill_in_form(self):
        self.driver.get(self.google_form_link)
        counter = 1
        for listing in self.info_list:
            print(listing["address"],listing["price"],listing["link"])
            print(f"Loop {counter}")
            self.driver.get(self.google_form_link)
            time.sleep(2)
            all_boxes = WebDriverWait(self.driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".whsOnd.zHQkBf"))
)
            address_box = all_boxes[0]
            address_box.send_keys(listing["address"])
            price_box = all_boxes[1]
            price_box.send_keys(listing["price"])
            link_box = all_boxes[2]
            link_box.send_keys(listing["link"])
            submit_button = self.driver.find_element(By.XPATH,value="//span[contains(text(),'Gửi')]")
            submit_button.click()
            time.sleep(1)
            self.driver.close()
            counter +=  1
            self.driver = webdriver.Chrome(options=self.chrome_options)
        
    def open_sheet(self):
        self.driver.get(self.google_spreadsheet_link)
        exit_confirmation = input("Type anything to exit...")
        self.driver.close()
        return

        

            
            

   
                

