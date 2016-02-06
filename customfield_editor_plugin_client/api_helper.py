import requests
import pprint

class ApiHelper:

    def __init__(self, baseurl, username, password):
        self.baseUrl = baseurl + 'rest/jiracustomfieldeditorplugin/1.2'
        self.authUserName = username
        self.authPassword = password

    def post(self, urlpart, payload):
        r = requests.post(self.baseUrl + urlpart, json=payload, auth=(self.authUserName, self.authPassword))
        if r.status_code == 200:
            print ('SUCCESS')
        else:
            print ('ERROR')
            print (r.status_code)

    def get(self, urlpart):
        pp = pprint.PrettyPrinter(width=41, compact=True)
        url = self.baseUrl + urlpart
        print ('GET ' + url)
        r = requests.get(url, auth=(self.authUserName, self.authPassword))
        if r.status_code == 200:
            print ('SUCCESS')
            pp.pprint(r.json())
        else:
            print ('ERROR')
            print (r.status_code)


