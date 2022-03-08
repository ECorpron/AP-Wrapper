import requests
import generalapiwrapper.apiWrapper as api
import generalapiwrapper.SteamworksWrapper as steamApi

# Only using the Requests package
gameId = 1172470
achRequest = f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={gameId}'

ach = requests.get(achRequest)

print("Using the requests package to get game achievements \n")
print(ach.text)
print("\n")

# Using the APIWrapper class
getAch = {"getGameAch": achRequest}

apiWrap = api.APIWrapper()
apiWrap.updateGetRequests(getAch)

print("Using the apiWrapper class to get game achievements \n")
print(apiWrap.executeGet("getGameAch").text)
print("\n")

# Using the SteamworksWrapper class
steamWrap = steamApi.SteamworksWrapper()

print("Using the SteamworksWrapper class to get game achievements \n")
print(steamWrap.getGameAchievements(gameId))
print("\n")
