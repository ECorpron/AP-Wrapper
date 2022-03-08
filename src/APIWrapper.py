import requests

class APIWrapper():
    getRequests = {}
    postRequests = {}
    keys = {}
    statusCode = None

    def __init__(self):
        pass

    def updateValue(self, dict):
        self.keys.update(dict)
        return keys

    def getKeys(self):
        return self.keys

    def getKey(self, key):
        return self.keys[key]

    def replaceKeys(self, newKeys):
        self.keys = newKeys

    def addKeys(self, dict):
        self.keys.update(dict)
        return self.keys

    def deleteKey(self, key):
        value = self.keys.pop(key)
        return value

    def deleteAllKeys(self):
        self.keys.clear()

    def updateGetRequests(self, dict):
        self.getRequests.update(dict)
        return self.getRequests

    def deleteGetRequest(self, key):
        self.getRequests.remove(key)
        return self.getRequests

    def deleteAllGetRequests(self):
        self.getRequests.clear()

    def updatePostRequests(self, dict):
        self.postRequests.update(dict)
        return self.postRequests

    def deletePostRequest(self, key):
        self.postRequests.remove(key)
        return self.postRequests

    def deleteAllPostRequests(self):
        self.postRequests.clear()

    def executeGet(self, key):
        response = requests.get(self.getRequests[key])
        self.statusCode = response.status_code
        return response

    def executePost(self, key):
        response = requests.post(self.getRequests[key])
        self.statusCode = response.status_code
        return response

    def getLastStatus(self):
        return self.statusCode
