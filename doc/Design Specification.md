# Design Specification
The project is split into two components, a APIWrapper class and a SteamworksWrapper class. APIWrapper is a parent class to the SteamworksWrapper class.

## Design Details

### APIWrapper Class
The APIWrapper class currently has three dictionaries, one for get requests, one for post requests, and one for keys. It exposes these dictionaries through getters and setters. It also has executeGet() and executePost() methods that take in a key for a corresponding get or post request, executes the request, and returns the response object.

### SteamworksWrapper
The SteamworksWrapper class currently has one non setter method, getGameAchievements(). This takes in a game ID on steam, and returns a json object that has information about the games achievements. It also has an api key field that can be set through setApiKey(), and a profile ID field that can be set with setProfileId().
