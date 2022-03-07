import requests
from src import APIWrapper

class SteamworksWrapper(APIWrapper):
    gameIds = {"ARK": 376030, "Chivalry 2": 1824220}
    gameAchString = "http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=%d"


    def __init__(self, key=None, profileId = None):
        self.apiKey = key
        self.profileId = profileId
        self.profileRequests = profileRequests()
        self.gameAchRequests = gameAchRequests()

    def profileRequests():
        getProfileString = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.apiKey}={self.profileId}"
        profileRequests = {self.profileId: getProfileString}
        return profileRequests

    def gameAchRequests():
        gameAchRequests = {}
        for game in self.gameIds:
            achRequest = self.gameAchString %gameIds[game]
            gameAchRequests.update(game, achRequest)

        return gameAchRequests

    def getGameAchievments(gameId):
        achRequest = self.gameAchString %gameId

        response = requsts.get(achRequest)
        jsonAch = response.json()
        return jsonAch
