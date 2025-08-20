from dotenv import load_dotenv
import os
import sys
import requests
os.chdir(os.path.dirname(__file__))
def main():
    VERSION_NUMBER = 10
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(current_directory,".env")
    load_dotenv(env_path)
    discord_token = "Bot " + os.getenv("DISCORD_TOKEN")
    header = {"Authorization": discord_token,
              "Content-Type": "application/json",
              }
    response = requests.get(f"https://discord.com/api/v{VERSION_NUMBER}",)
    
if __name__ == "__main__":
    main()