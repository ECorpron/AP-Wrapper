import requests
import generalapiwrapper.apiWrapper as api
import generalapiwrapper.SteamworksWrapper as steamApi

# Only using the Requests package
gameId = 1172470
achRequest = f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={gameId}'

ach = requests.get(achRequest)
print(ach.text)

# Using the APIWrapper class
getAch = {"getGameAch": achRequest}

apiWrap = api.APIWrapper()
apiWrap.updateGetRequests(getAch)

print(apiWrap.executeGet("getGameAch").text)

# Using the SteamworksWrapper class
steamWrap = steamApi.SteamworksWrapper()
print(steamWrap.getGameAchievements(gameId))
