import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def fetch_player_data():
    url = "https://www.whoscored.com/Players"  
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    players = []  
    for player in soup.find_all('div', class_='player-row'):
        name = player.find('a', class_='player-name').text.strip() if player.find('a', class_='player-name') else 'N/A'
        team = player.find('span', class_='team-name').text.strip() if player.find('span', class_='team-name') else 'N/A'
        age = player.find('span', class_='age').text.strip() if player.find('span', class_='age') else 'N/A'
        height = player.find('span', class_='height').text.strip() if player.find('span', class_='height') else 'N/A'
        rating = player.find('span', class_='rating').text.strip() if player.find('span', class_='rating') else 'N/A'
        positions = player.find('span', class_='positions').text.strip() if player.find('span', class_='positions') else 'N/A'
        appearances = player.find('span', class_='appearances').text.strip() if player.find('span', class_='appearances') else 'N/A'
        strengths = player.find('span', class_='strengths').text.strip() if player.find('span', class_='strengths') else 'N/A'
        weaknesses = player.find('span', class_='weaknesses').text.strip() if player.find('span', class_='weaknesses') else 'N/A'
    
        players.append([name, team, age, height, rating, positions, appearances, strengths, weaknesses])
    
    return players
def save_to_csv(players):
    df = pd.DataFrame(players, columns=["Name", "Team", "Age", "Height", "Rating", "Positions", "Appearances", "Strengths", "Weaknesses"])
    
    df.to_csv('whoscored_data.csv', index=False)
    print("Data saved to whoscored_data.csv")
def fetch_and_save_data():
    print("Fetching data...")
    players = fetch_player_data()
    save_to_csv(players)
fetch_and_save_data()
