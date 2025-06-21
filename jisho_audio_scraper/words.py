from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import os
hiragana_words = {
    "かさ": ["umbrella"],
    "おす": ["to push"],
    "きし": ["knight"],
    "すぐ": ["immediately"],
    "すき": ["like"],
    "けす": ["to erase"],
    "くじ": ["lottery"],
    "しお": ["salt"],
    "いしき": ["consciousness"],
    "しぐさ": ["gesture", "mannerism"],
    "さそう": ["to invite"],
    "おこす": ["to wake someone up", "to cause to happen"],
    "すこし": ["a little"],
    "さがす": ["to search"],
    "しかく": ["square"],
    "かえす": ["to return"],
    "うさぎ": ["rabbit"],
    "さいせい": ["playback"],
    "おかしい": ["strange"],
    "がくせい": ["student"]
}#Avoid cluttering main and this also acts as testing data
class JishoAudioDownloader():
    def __init__(self,words):
        os.makedirs("audio", exist_ok=True)
        self.words = words
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        self.chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\YourUsername\Downloads\jisho_audio",
})
        self.chrome_options.add_experimental_option("detach", True)


        self.driver = webdriver.Chrome(options=self.chrome_options)
    def download_audio(self,*args):
        for word in self.words:
            time.sleep(1.5)
            self.driver.get(f"https://jisho.org/search/{word}")
            word_blocks = self.driver.find_elements(By.CSS_SELECTOR,value=".concept_light.clearfix")
            for word_block in word_blocks:
                try:
                    if self.words[word][0] in word_block.find_element(By.CSS_SELECTOR,".meaning-meaning").text:
                        audio_element = word_block.find_element(By.CSS_SELECTOR,value="source[src$='.mp3']") #only first mp3 audio for now
                        audio_link = audio_element.get_attribute("src")
                        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }          
                        parameters = {"downloadformat": "mp3"}
                        audio_file = requests.get(audio_link,params=parameters,headers=headers)
                        audio_file.raise_for_status()
                        print(audio_file)
                        download_path = os.path.join("audio",word + ".mp3")
                        with open(download_path,"wb") as f:
                            f.write(audio_file.content)
                        break #Stops after finding the desired audio
                    
                    else:
                        continue

                except Exception as e:
                    print(f"❌ Error while processing '{word}': {e}")
                    continue
            
        
if __name__ == "__main__":
    pass