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
import numpy as np
import os
import time
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
class MALWebScraper:
    def __init__(self):
        self.headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        self.anime_links = []

        
        os.makedirs("data", exist_ok=True) #Creates data folder if it doesnt already exists

            
    def fetch_genres_data(self):
        """
    Scrapes anime genre data from MyAnimeList and saves it to a CSV file.

    The output CSV contains two columns:
        - Genre (str): Name of the anime genre (e.g. "Action", "Romance")
        - Count (int): Number of anime entries under that genre
    """
        SAVE_PATH = os.path.join("data","genres.csv")
        genre_data = {}
        genres_page = requests.get("https://myanimelist.net/anime.php").text
        soup = BeautifulSoup(genres_page,"html.parser")
        for link in soup.select("a.genre-name-link"):
            href = link.get("href","") #Get returns a list
            if "genre" in href:
                genre_text = link.text.rsplit(" ",1) #Splits ONE time in reverse order(Deal with these: "Reverse Harem (123)")
                genre_name= genre_text[0] 
                genre_count = int(genre_text[1].replace("(","").replace(")","").replace(",",""))
                genre_data[genre_name] = genre_count
                df = pd.DataFrame(genre_data.items(),columns=["Genre","Count"]) #.items() returns a list of tuples
                df.to_csv(SAVE_PATH,index=False)
        print(genre_data)
    def fetch_anime_data(self):
        SAVE_PATH = os.path.join("data","animes.csv")
        columns = ["title_romaji", "title_english", "score", "rank", "popularity_rank", "members", "season", "type", "studio","genres","themes"]
        if not os.path.exists(SAVE_PATH):
            df = pd.DataFrame(columns=columns)
            df.to_csv(SAVE_PATH, index=False)
            
        anime_data = {}
        MAX_LIMT = 50 #Testing limiter :)
       
        limit = 0
        while True:
            anime_list = requests.get(f"https://myanimelist.net/topanime.php?limit={limit}")
            if anime_list.status_code == 404:
                break
            print(anime_list.status_code)

            soup = BeautifulSoup(anime_list.text,"html.parser")
            anime_links = soup.select("td.title.al.va-t.word-break > a[href*='anime']")
            for anime in anime_links:
                time.sleep(1) #MAL will block you if you spam requests
                anime_url = anime.get("href")
                print(anime_url)
                anime_page = requests.get(anime_url,headers=self.headers)
                if anime_page.status_code != 200:
                    print(f"[⛔] Failed to fetch {anime_url}")
                    continue
                soup = BeautifulSoup(anime_page.text, "html.parser")

                anime_name = soup.select_one("h1.title-name.h1_bold_none > strong").text

                anime_english_name = soup.select_one("p.title-english.title-inherit")
                anime_english_name = anime_english_name.text if anime_english_name else np.nan

                anime_score = soup.select_one("div[class~=score-label]")
                anime_score = float(anime_score.text) if anime_score != "N/A" else np.nan

                anime_rank = soup.select_one("span.numbers.ranked > strong")
                anime_rank = int(anime_rank.text.strip("#")) if anime_rank != "N/A" else np.nan

                anime_popularity_rank = soup.select_one("span.numbers.popularity > strong")
                anime_popularity_rank = float(anime_popularity_rank.text.strip("#")) if anime_popularity_rank != "N/A" else np.nan

                anime_members = int(soup.select_one("span.numbers.members > strong").text.replace(",", ""))

                anime_season = soup.select_one("span.information.season > a")
                anime_season = anime_season.text if anime_season else np.nan

                anime_type = soup.select_one("span.information.type > a").text

                anime_studio = soup.select_one("span.information.studio.author > a")
                anime_studio = anime_studio.text if anime_studio else np.nan

                anime_genres = []
                anime_themes = []

                if soup.select("a[href*='/anime/genre/']"):
                    anime_genres_themes = soup.select("a[href*='/anime/genre/']")
                    for genre in anime_genres_themes:
                        href = genre.get("href", "").split("/")
                        genre_id = int(href[3])
                        if 1 <= genre_id <= 49:
                            anime_genres.append(href[4])
                        elif 50 <= genre_id <= 99:
                            anime_themes.append(href[4])
                        else:
                            continue

                anime_genres = ",".join([anime_genre for anime_genre in anime_genres if anime_genres])
                anime_themes = ",".join([anime_theme for anime_theme in anime_themes if anime_themes])

                anime_data = [anime_name, anime_english_name, anime_score, anime_rank, anime_popularity_rank, anime_members,
                              anime_season,
                              anime_type,
                              anime_studio, anime_genres, anime_themes]

                anime_df = pd.DataFrame([anime_data], columns=columns)
                anime_df.drop_duplicates(subset=["title_romaji"],inplace=True)
                anime_df.to_csv(SAVE_PATH, index=False, mode="a", header=None)
            if limit == MAX_LIMT:
                break
            limit += 50
        print("Finished fetching animes.")
        
        
        
        
        
    