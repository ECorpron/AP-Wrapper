  # GeneralAPIWrapper
There are two initial goals for this project. The first is to provide a generic api wrapper class that stores and executes any number of requests and returns a response body. The second is to have a class specifically for the Steamworks API that has built in functions for requests, and is able to extract entries in the response body.
  
** NOTE FOR GRADING

The example code worked when I made the presentation recording. I don't think I made any changes that would break the ability to install and run the
example code, but I have not tested it recently so it is possible it does not work.

## How to Install
To install the GeneralAPIWrapper module use the following command while in the directory the python project is in.
    
    pip install -i https://test.pypi.org/simple/ GeneralAPIWrapper

Then import the apiWrapper and SteamworksApiWrapper with the statements
    
    import generalapiwrapper.apiWrapper
    import generalapiwrapper.SteamworksWrapper

## Key Features
### APIWrapper
The key feature of the ApiWrapper class is the ability to store and execute requests. This is done by storing requests in their corresponding dictionaries with the methods updateGetRequests() and updatePostRequests(), then executing them with the methods executeGet() and executePost() and passing in the corresponding key.

    getRequest = {"key": "an api call"}
    apiWrap = apiWrapper.APIWrapper()
    apiWrap.updateGetRequests(getRequest)
    returnBody = apiWrap.executeGet("getRequest")
    
This then returns the object that comes from the requests package .get() method.

### Steamworks
The key feature of the SteamworksWrapper class is the ability to execute requests without the need to specify the request. Currently the only method is getGameAchievements(), which takes in a game ID for a game on steam, and then returns a json object with the information.

    steamWrap = SteamworksWrapper.SteamworksWrapper()
    returnBody = steamWrap.getGameAchievements(gameId))


## Dependencies
requests
