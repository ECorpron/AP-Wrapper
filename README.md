  # GeneralAPIWrapper
There are two initial goals for this project. The first is to provide a generic api wrapper class that stores and executes any number of requests and returns a response body. The second is to have a class specifically for the Steamworks API that has built in functions for requests, and is able to extract entries in the response body.
  
## How to Install
To install the GeneralAPIWrapper module use the following command while in the directory the python project is in.
    
    pip install -i https://test.pypi.org/simple/ GeneralAPIWrapper

Then import the apiWrapper and SteamworksApiWrapper with the statements
    
    import generalapiwrapper.apiWrapper
    import generalapiwrapper.SteamworksWrapper
    
## Dependencies
requests
