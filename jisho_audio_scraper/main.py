from words import JishoAudioDownloader,hiragana_words
import requests
from selenium import webdriver


def main():
    jisho_audio_downloader = JishoAudioDownloader(hiragana_words)
    jisho_audio_downloader.download_audio()
if __name__ == "__main__":
    main()