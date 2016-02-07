import validators
from .user_input_exception import UserInputException

class UserInput:

    def __init__(self, baseurl, username, password):
        self.baseUrl = baseurl
        self.authUserName = username
        self.authPassword = password

    @property
    def baseUrl(self):
        return self.__baseUrl

    @baseUrl.setter
    def baseUrl(self, value):
        if not validators.url(value, require_tld=False):
            raise UserInputException('baseUrl needs to be valid URL.')
        if not value.endswith('/'):
            value = value + '/'

        self.__baseUrl = value
