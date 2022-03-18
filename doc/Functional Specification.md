The GeneralAPIWrapper shall provide developers with a class that allows for the storage and execution of api calls that can be performed on any API. It shall also
provide easy to use classes for specific APIs that handle calls and the response body.

The goal for this project is to be an easy to use way to manage api calls. In my own experience it feels like there is a lot of repeated code when dealing with APIs,
and the purpose here is to decrease the code needed and make it easier to make such calls. The other goal is to provide classes for specific APIs since
different APIs can handle calls and requests much differently from each other.

For this purpose, the classes shall be able to:
- Store api calls in a dictionary and can be referenced by a specified string key
- Execute a stored api call by being given the corresponding key through the requests package
- be able to update and delete api calls from class dictionary
