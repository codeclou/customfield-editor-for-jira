import argparse
import sys
import colorama
import requests
from .api_helper import ApiHelper
from .api_helper_exception import ApiHelperException
from .user_input import UserInput
from .user_input_exception import UserInputException
from .print_helper import PrintHelper

def main():
    colorama.init(autoreset=True)
    printHelper = PrintHelper()

    print(colorama.Fore.CYAN + '\n~~ REST API Client for Customfield Editor Plugin ~~ v1.2rc1')

    parser = argparse.ArgumentParser(description='Customfield Editor Plugin REST API CLI Client.')
    parser.add_argument("-cid", "--customFieldId", type=int, help='The ID of the custom field.')
    parser.add_argument("-a", "--action", help='Which action to execute.', choices=['adminListFields', 'insertOptions','deleteOption'], required=True)
    parser.add_argument("-url", "--baseUrl", help='baseUrl to JIRA instance e.g. http://server:port/jira/', required=True)
    parser.add_argument("-user", "--authUsername", help='username for basic auth.', required=True)
    parser.add_argument("-pass", "--authPassword", help='password for basic auth.', required=True)
    args = parser.parse_args()


    printHelper.step('initializing')
    try:
        userInput = UserInput(args.baseUrl, args.authUsername, args.authPassword)
    except UserInputException as ex:
        printHelper.error('UserInput is invalid.')
        print (ex)
        sys.exit(1)
    printHelper.success('UserInput is valid.')



    try:
        apiHelper = ApiHelper(userInput)
    except ApiHelperException as ex:
        printHelper.error('ApiHelper could not be initialized.')
        print (ex)
        sys.exit(1)
    printHelper.success('ApiHelper initialized.')



    try:


        # $> cep-client -a adminListFields -url http://localhost:2990/jira/ -user admin -pass admin
        if args.action == 'adminListFields':
            apiHelper.get('/admin/customfields')


    except requests.ConnectionError as ex:
        printHelper.error('There seems to a be problem with your request.')
        print (ex)
        sys.exit(1)

    print ('\n')
