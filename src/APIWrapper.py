import requests

class APIWrapper():

    def __init__(self, keys = None, request = None):
        self.keys = keys
        self.request = request
        statusCode = None

    def updateValue(dict):
        keys.update(dict)
        return keys

    def getKeys():
        return keys

    def getKey(key):
        return keys[key]

    def replaceKeys(newKeys):
        keys = newKeys

    def addKeys(dict):
        keys.update(dict)
        return keys

    def deleteKey(key):
        value = keys.pop(key)
        return value

    def deleteAllKeys():
        keys.clear()

    def updateRequest(dict):
        request.update(dict)
        return request

    def addRequests(dict):
        request.update(dict)
        return request

    def executeGet(key):
        response = requests.get(request[key])
        statusCode = response.status_code
        return response

    def executePost(key):
        response = requests.post(request[key])
        statusCode = response.status_code
        return response

    def getLastStatus():
        return statusCode
