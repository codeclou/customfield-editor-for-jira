import requests
import textwrap
import tabulate
from .api_helper_exception import ApiHelperException
from .print_helper import PrintHelper

class ApiHelper:

    def __init__(self, userInput):
        self.printHelper = PrintHelper()
        self.userInput = userInput
        self._health_check()


    def post(self, urlpart, payload):
        request_url = self._rest_url(urlpart)
        self.printHelper.step('POST ' + request_url)
        response = requests.post(request_url, json=payload, auth=(self.userInput.authUserName, self.userInput.authPassword))
        self._handle_response_errors(response)
        try:
            return response.json()
        except ValueError as ex:
            return {}

    def put(self, urlpart, payload):
        request_url = self._rest_url(urlpart)
        self.printHelper.step('PUT ' + request_url)
        response = requests.put(request_url, json=payload, auth=(self.userInput.authUserName, self.userInput.authPassword))
        self._handle_response_errors(response)
        try:
            return response.json()
        except ValueError as ex:
            return {}

    def get(self, urlpart):
        request_url = self._rest_base_url() + urlpart
        self.printHelper.step('GET ' + request_url)
        response = requests.get(request_url, auth=(self.userInput.authUserName, self.userInput.authPassword))
        self._handle_response_errors(response)
        try:
            return response.json()
        except ValueError as ex:
            return {}



    def _health_check(self):
        health_url = self._rest_base_url() + '/health/status'
        try:
            r = requests.get(health_url)
            if r.status_code != 200:
                raise ApiHelperException('baseUrl does not lead to running JIRA with installed Customfield Editor Plugin. Health check failed with HTTP {0} for URL: {1}'.format(r.status_code, health_url))
        except requests.ConnectionError as ex:
            raise ApiHelperException(ex)

    def _rest_base_url(self):
        return self.userInput.baseUrl + 'rest/jiracustomfieldeditorplugin/1.2'

    def _rest_url(self, url_part):
        return self._rest_base_url() + url_part

    def _handle_response_errors(self, response):
        if response.status_code == 200:
            self.printHelper.success('request successful')
            return
        elif response.status_code == 204:
            self.printHelper.success('request successful')
            return
        elif response.status_code == 401:
            self.printHelper.error('UNAUTHORIZED (401). Authorization failed (wrong or no credentials).')
            raise ApiHelperException(401)
        elif response.status_code == 403:
            self.printHelper.error('FORBIDDEN (403). Insufficient rights - OR - too many failed login attempts. (Log into JIRA in the browser to solve CAPTCHA).')
            raise ApiHelperException(403)
        else:
            self.printHelper.error('request failed with HTTP {0}'.format(response.status_code))
            raise ApiHelperException(response.status_code)
