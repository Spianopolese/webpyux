class User:
    def __init__(self, first_name, last_name, picture, access_token) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._picture = picture
        self._access_token = access_token

    def getFirstName(self):
        return self._first_name

    def getLastName(self):
        return self._last_name

    def getPicture(self):
        return self._picture

    def getAccessToken(self):
        return self._access_token
