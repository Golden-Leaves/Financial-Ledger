import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os
class MALWebScraper:
    def __init__(self):
        self.headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        self.anime_links = []
        self.genre_data = {}
        os.makedirs("data", exist_ok=True) #Creates data folder if it doesnt already exists

            
    def fetch_genres_data(self):
        SAVE_PATH = os.path.join("data","genres.csv")
        genres_page = requests.get("https://myanimelist.net/anime.php").text
        soup = BeautifulSoup(genres_page,"html.parser")
        for link in soup.select("a.genre-name-link"):
            href = link.get("href","") #Get returns a list
            if "genre" in href:
                genre_data = link.text.split(" ")
                genre_name = " ".join([word for word in genre_data if word.isalpha()])
                genre_count = int(genre_data[-1].replace("(","").replace(")","").replace(",",""))
                self.genre_data[genre_name] = genre_count
                df = pd.DataFrame(self.genre_data.items(),columns=["Genre","Count"]) #.items() returns a list of tuples
                df.to_csv(SAVE_PATH,index=False)
        print(self.genre_data)

