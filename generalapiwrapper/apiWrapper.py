import requests

class APIWrapper():
    '''
    This class provides dictionaries to store requests and methods to then
    execute the requests. It uses the requests package to handle the execution
    of these requests.
    '''
    __getRequests: dict[str, str] = {}
    __postRequests: dict[str, str] = {}
    __keys: dict[str, str] = {}
    statusCode = None

    def updateKeys(self, dict):
        '''
        updates the keys with the given dictionary of values

            Parameters:
                    dict (dict): A dictionary of keys

            Returns:
                    The updated keys
        '''
        self.__keys.update(dict)
        return self.__keys

    def getKeys(self):
        '''
        Returns the dictionary of keys

            Returns:
                    A dictionary of Keys
        '''
        return self.__keys

    def getKey(self, key):
        '''
        Returns a specific key

            Parameters:
                    key (String): a key for a specific key

            Returns:
                    A specified key
        '''
        return self.__keys[key]

    def deleteKey(self, key):
        '''
        Deletes a specific key value pair

            Parameters:
                    key (String): a key for a specific key

            Returns:
                    The deleted value
        '''
        value = self.__keys.pop(key)
        return value

    def deleteAllKeys(self):
        '''
        Removes all keys
        '''
        self.__keys.clear()

    def updateGetRequests(self, dict):
        '''
        updates the get requests with the given dictionary of requests

            Parameters:
                    dict (dict): A dictionary of get requests

            Returns:
                    The updated get requests
        '''
        self.__getRequests.update(dict)
        return self.__getRequests

    def deleteGetRequest(self, key):
        '''
        Deletes a specific get request

            Parameters:
                    key (String): a key for a specific get request

            Returns:
                    The deleted get request
        '''
        self.__getRequests.remove(key)
        return self.__getRequests

    def deleteAllGetRequests(self):
        '''
        Removes all get requests
        '''
        self.__getRequests.clear()

    def updatePostRequests(self, dict):
        '''
        updates the post requests with the given dictionary of post requests

            Parameters:
                    dict (dict): A dictionary of post requests

            Returns:
                    The updated post requests
        '''
        self.__postRequests.update(dict)
        return self.__postRequests

    def deletePostRequest(self, key):
        '''
        Deletes a specific post request

            Parameters:
                    key (String): a key for a specific post request

            Returns:
                    The deleted post request
        '''
        self.__postRequests.remove(key)
        return self.__postRequests

    def deleteAllPostRequests(self):
        '''
        Removes all post requests
        '''
        self.__postRequests.clear()

    def executeGet(self, key):
        '''
        Executes a specific get request, and returns the requests package
        response body

            Parameters:
                    key (String): a key for a specific get request

            Returns:
                    The requests package response body for the get request
        '''
        response = requests.get(self.__getRequests[key])
        self.statusCode = response.status_code
        return response

    def executePost(self, key):
        '''
        Executes a specific post request, and returns the requests package
        response body

            Parameters:
                    key (String): a key for a specific post request

            Returns:
                    The requests package response body for the post request
        '''
        response = requests.post(self.__getRequests[key])
        self.statusCode = response.status_code
        return response

    def getLastStatus(self):
        '''
        Returns the status code for the last request

            Returns:
                    The status code for the last request
        '''
        return self.statusCode
