import requests
from generalapiwrapper.apiWrapper import APIWrapper

class SteamworksWrapper(APIWrapper):
    __apiKey = None
    __profileId = None
    #profileRequests = profileRequests()
    #gameAchRequests = self.gameAchRequests()
    #__gameAchRequests = {}

    gameIds = {"ARK": 376030, "Chivalry 2": 1824220}
    __gameAchString = "http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=%d"

    """
    def profileRequests(self):
        getProfileString = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.apiKey}={self.profileId}"
        profileRequests = {self.profileId: getProfileString}
        return profileRequests
    """

    """
    def gameAchRequests(self):
        gameAchRequests = {}
        for game in self.gameIds:
            achRequest = self.gameAchString %gameIds[game]
            gameAchRequests.update(game, achRequest)

        return gameAchRequests
        """


    def getGameAchievements(self, gameId):
        achRequest = self.__gameAchString %gameId
        response = requests.get(achRequest)
        jsonAch = response.json()
        return jsonAch

    def setApiKey(self, key):
        self.__apiKey = key

    def setProfileId(self, id):
        self.__profileId = id
