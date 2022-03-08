import requests

class APIWrapper():
    __getRequests = {}
    __postRequests = {}
    __keys = {}
    statusCode = None

    def __init__(self):
        pass

    def updateValue(self, dict):
        self.__keys.update(dict)
        return self.__keys

    def getKeys(self):
        return self.__keys

    def getKey(self, key):
        return self.__keys[key]

    def replaceKeys(self, newKeys):
        self.__keys = newKeys

    def addKeys(self, dict):
        self.__keys.update(dict)
        return self.__keys

    def deleteKey(self, key):
        value = self.__keys.pop(key)
        return value

    def deleteAllKeys(self):
        self.__keys.clear()

    def updateGetRequests(self, dict):
        self.__getRequests.update(dict)
        return self.__getRequests

    def deleteGetRequest(self, key):
        self.__getRequests.remove(key)
        return self.__getRequests

    def deleteAllGetRequests(self):
        self.__getRequests.clear()

    def updatePostRequests(self, dict):
        self.__postRequests.update(dict)
        return self.__postRequests

    def deletePostRequest(self, key):
        self.__postRequests.remove(key)
        return self.__postRequests

    def deleteAllPostRequests(self):
        self.__postRequests.clear()

    def executeGet(self, key):
        response = requests.get(self.__getRequests[key])
        self.statusCode = response.status_code
        return response

    def executePost(self, key):
        response = requests.post(self.__getRequests[key])
        self.statusCode = response.status_code
        return response

    def getLastStatus(self):
        return self.statusCode
