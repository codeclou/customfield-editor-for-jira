import requests
import pprint
import tabulate
from .api_helper_exception import ApiHelperException
from .print_helper import PrintHelper

class ApiHelper:

    def __init__(self, userInput):
        self.printHelper = PrintHelper()
        self.userInput = userInput
        healthUrl = self.restBaseUrl() + '/health/status'
        r = requests.get(healthUrl)
        if r.status_code != 200:
            raise ApiHelperException('baseUrl does not lead to running JIRA with installed Customfield Editor Plugin. Health check failed with HTTP {0} for URL: {1}'.format(r.status_code, healthUrl))

    def restBaseUrl(self):
        return self.userInput.baseUrl + 'rest/jiracustomfieldeditorplugin/1.2'

    def post(self, urlpart, payload):
        r = requests.post(self.restBaseUrl() + urlpart, json=payload, auth=(self.userInput.authUserName, self.userInput.authPassword))
        if r.status_code == 200:
            print ('SUCCESS')
        else:
            print ('ERROR')
            print (r.status_code)

    def get(self, urlpart):
        pp = pprint.PrettyPrinter(width=41, compact=True)
        url = self.restBaseUrl() + urlpart
        print ('GET ' + url)
        r = requests.get(url, auth=(self.userInput.authUserName, self.userInput.authPassword))
        if r.status_code == 200:
            self.printHelper.success('Request returns 200')
            print (tabulate.tabulate(r.json(), headers="keys"))
            #pp.pprint(r.json())
        else:
            print ('ERROR')
            print (r.status_code)


