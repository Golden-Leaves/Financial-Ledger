from words import JishoAudioDownloader,hiragana_words
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException

def main():
    jisho_audio_downloader = JishoAudioDownloader(hiragana_words)
    jisho_audio_downloader.download_audio()
if __name__ == "__main__":
    main()