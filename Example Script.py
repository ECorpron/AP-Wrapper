import requests
from src import APIWrapper
from src import SteamworksWrapper

# Only using the Requests package
gameId = 440
achRequest = f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={gameId}'

ach = requests.get(achRequest)
print(ach.text)
