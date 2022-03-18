import requests
from generalapiwrapper.apiWrapper import APIWrapper

class SteamworksWrapper(APIWrapper):
    '''
    This class provides functionality for accessing the Steamworks API.
    Currently has limited functionality, but will be extended in the future.
    '''
    gameIds = {"ARK": 376030, "Chivalry 2": 1824220}
    __gameAchString = "http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=%d"

    def profileRequests(self):
        '''
        To be implemented in the future. Will return profile information from
        a specified profile.
        '''
        pass

    def gameAchRequests(self):
        '''
        To be implemented in the future. Will return game achievment
        information for a list of games
        '''
        pass

    def getGameAchievements(self, gameId):
        '''
        Executes a get request for a specified game

            Parameters:
                    game ID (int): a game ID for a game on Steam

            Returns:
                    A json object with the information of the game achievements
        '''
        achRequest = self.__gameAchString %gameId
        response = requests.get(achRequest)
        jsonAch = response.json()
        return jsonAch
