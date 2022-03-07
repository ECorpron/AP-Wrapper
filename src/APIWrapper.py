import requests

class APIWrapper():
    keys = {}
    request = {}
    statusCode

    def __init__():
        pass

    def addValue({key, value}):
        keys[key] = value
        return keys

    def updateValue({key, value}):
        keys.update({key, value})
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

    def addRequest({key, value}):
        request[key] = value
        return request

    def updateRequest({key, value}):
        request.update({key, value})
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
