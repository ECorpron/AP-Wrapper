import requests
from API-Wrapper.APIWrapper import APIWrapper
from API-Wrapper.SteamworksWrapper import SteamworksWrapper

# Only using the Requests package
gameId = 1172470
achRequest = f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={gameId}'

ach = requests.get(achRequest)
print(ach.text)

# Using the APIWrapper class
getAch = {"getGameAch": achRequest}

apiWrap = APIWrapper()
apiWrap.updateGetRequests(getAch)

apiWrap.executeGet("getGameAch")

# Using the SteamworksWrapper class
steamWrap = SteamworksWrapper()
print(steamWrap.getGameAchievments(gameId))
