import argparse
import sys
import colorama
from .api_helper import ApiHelper
from .api_helper_exception import ApiHelperException
from .user_input import UserInput
from .user_input_exception import UserInputException


def main():
    colorama.init(autoreset=True)

    print(colorama.Fore.CYAN + '\n~~ REST API Client for Customfield Editor Plugin ~~\n')

    parser = argparse.ArgumentParser(description='Customfield Editor Plugin REST API CLI Client.')
    parser.add_argument("-cid", "--customFieldId", type=int, help='The ID of the custom field.')
    parser.add_argument("-a", "--action", help='Which action to execute.', choices=['adminListFields', 'insertOptions','deleteOption'], required=True)
    parser.add_argument("-url", "--baseUrl", help='baseUrl to JIRA instance e.g. http://server:port/jira/', required=True)
    parser.add_argument("-user", "--authUsername", help='username for basic auth.', required=True)
    parser.add_argument("-pass", "--authPassword", help='password for basic auth.', required=True)
    args = parser.parse_args()



    try:
        userInput = UserInput(args.baseUrl, args.authUsername, args.authPassword)
    except UserInputException as ex:
        print(colorama.Fore.RED + 'ERROR   - UserInput is invalid.', ex)
        sys.exit(1)
    print(colorama.Fore.GREEN + 'SUCCESS - UserInput is valid.')



    try:
        apiHelper = ApiHelper(userInput)
    except ApiHelperException as ex:
        print(colorama.Fore.RED + 'ERROR   - ApiHelper could not be initialized.', ex)
        sys.exit(1)
    print(colorama.Fore.GREEN + 'SUCCESS - ApiHelper initialized.')



    #  cep-client -a adminListFields -url http://localhost:2990/jira/ -user admin -pass admin
    if args.action == 'adminListFields':
        apiHelper
        apiHelper.get('/admin/customfields')


