import validators
from .user_input_exception import UserInputException

class UserInput:

    def __init__(self, cli_args):
        self.baseUrl = cli_args.baseUrl
        self.authUserName = cli_args.authUsername
        self.authPassword = cli_args.authPassword
        self.validate_cli_args(cli_args)

    @property
    def authUserName(self):
        return self._auth_username
    @authUserName.setter
    def authUserName(self, value):
        if not value:
            raise UserInputException('authUserName needs to be set.')
        self._auth_username = value

    @property
    def authPassword(self):
        return self._auth_password
    @authPassword.setter
    def authPassword(self, value):
        if not value:
            raise UserInputException('authPassword needs to be set.')
        self._auth_password = value

    @property
    def baseUrl(self):
        return self._base_url
    @baseUrl.setter
    def baseUrl(self, value):
        if not validators.url(value, require_tld=False):
            raise UserInputException('baseUrl needs to be valid URL.')
        if not value.endswith('/'):
            value = value + '/'
        self._base_url = value


    def validate_cli_args(self, cli_args):
        if cli_args.action == 'adminGrantPermission':
            self._validate_customfield_id(cli_args.customFieldId)

        if cli_args.action == 'userListOptions':
            self._validate_customfield_id(cli_args.customFieldId)

    def _validate_customfield_id(self, id):
        if id <= 0:
            raise UserInputException('customFieldId needs to be positive integer.')
