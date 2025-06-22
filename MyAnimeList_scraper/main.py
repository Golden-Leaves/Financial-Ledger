from mal_web_scraper import MALWebScraper
def main():
    mal_web_scraper = MALWebScraper()
    mal_web_scraper.fetch_genres_data()
if __name__ == "__main__":
    main()