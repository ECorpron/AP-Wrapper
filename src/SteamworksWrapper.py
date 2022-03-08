import requests
from src.APIWrapper import APIWrapper

class SteamworksWrapper(APIWrapper):
    apiKey = None
    profileId = None
    #profileRequests = profileRequests()
    #gameAchRequests = self.gameAchRequests()
    gameAchRequests = {}

    gameIds = {"ARK": 376030, "Chivalry 2": 1824220}
    gameAchString = "http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=%d"

    """
        def profileRequests(self):
            getProfileString = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.apiKey}={self.profileId}"
            profileRequests = {self.profileId: getProfileString}
            return profileRequests
    """

    def gameAchRequests(self):
        gameAchRequests = {}
        for game in self.gameIds:
            achRequest = self.gameAchString %gameIds[game]
            gameAchRequests.update(game, achRequest)

        return gameAchRequests

    def getGameAchievments(self, gameId):
        achRequest = self.gameAchString %gameId

        response = requests.get(achRequest)
        jsonAch = response.json()
        return jsonAch
