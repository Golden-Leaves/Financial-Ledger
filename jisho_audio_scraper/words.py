from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
hiragana_words = [
    "さく", "すし", "い", "あい", "あおい", "かく", "こうこうせい", "かげ",
    "かぎ", "きおく", "えいが", "うえ", "か", "か", "きく", "こえ",
    "おおきい", "ず", "じこ", "ぞう", "おかし", "さけ", "さいご", "そうぞう"]#Avoid cluttering main and this also acts as testing data
class JishoAudioDownloader():
    def __init__(self,words):
        self.words = words
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        self.chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\YourUsername\Downloads\jisho_audio",
})
        self.chrome_options.add_experimental_option("detach", True)


        self.driver = webdriver.Chrome(options=self.chrome_options)
        for word in self.words:
            time.sleep(1.5)
            self.driver.get(f"https://jisho.org/search/{word}")
            audio_element = self.driver.find_elements(By.CSS_SELECTOR,value="source[src$='.mp3']")[0]
            print(audio_element)
            time.sleep(999)
            
        
if __name__ == "__main__":
    pass