import argparse
import sys
import colorama
import requests
from .helper.api_helper import ApiHelper
from .helper.api_helper_exception import ApiHelperException
from .helper.print_helper import PrintHelper
from .model.user_input import UserInput
from .model.user_input_exception import UserInputException
from .modules.admin_operations import AdminOperations
from .modules.user_operations import UserOperations

def main():
    #
    # INIT
    #
    colorama.init(autoreset=True)
    printHelper = PrintHelper()
    print(colorama.Fore.CYAN + '\n~~ REST API Client for Customfield Editor Plugin ~~ v1.2rc1')

    #
    # CLI PARAMS
    #
    parser = argparse.ArgumentParser(description='Customfield Editor Plugin REST API CLI Client.')
    parser.add_argument("-cid", "--customFieldId", type=int, help='The ID of the custom field.')
    parser.add_argument("-ulist", "--userList", nargs='+', help='space separated user names to grant permission')
    parser.add_argument("-glist", "--groupList", nargs='+', help='space separated group names to grant permission')
    parser.add_argument("-a", "--action", help='Which action to execute.', choices=['adminListFields', 'adminGrantPermission', 'userListFields'], required=True)
    parser.add_argument("-url", "--baseUrl", help='baseUrl to JIRA instance e.g. http://server:port/jira/', required=True)
    parser.add_argument("-user", "--authUsername", help='username for basic auth.', required=True)
    parser.add_argument("-pass", "--authPassword", help='password for basic auth.', required=True)
    args = parser.parse_args()


    #
    # INITIALIZE HELPERS
    #
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


    #
    # INITIALIZE OPERATIONS
    #
    adminOperations = AdminOperations(apiHelper)
    userOperations = UserOperations(apiHelper)


    #
    # EXECUTE ACTIONS
    #
    try:
        printHelper.action(args.action)

        #
        # ADMIN ACTIONS
        #
        # $> cep-client -a adminListFields -url http://localhost:2990/jira/ -user admin -pass admin
        if args.action == 'adminListFields':

            adminOperations.list_fields()

        #> cep-client -a adminGrantPermission --customFieldId 10100 --userList bob steve  -url http://localhost:2990/jira -user admin -pass admin
        # (optional: --groupList)
        if args.action == 'adminGrantPermission':
            adminOperations.grant_permission(args.customFieldId, args.userList, args.groupList)


        #
        # USER ACTIONS
        #
        if args.action == 'userListFields':
            userOperations.list_fields()



    except requests.ConnectionError as ex:
        print ('')
        printHelper.error('There seemed to a be problem with your request. Check errors above. EXIT')
        print (ex)
        sys.exit(1)
    except ApiHelperException as ex:
        print ('')
        printHelper.error('There seemed to a be problem with your request. Check errors above. EXIT')
        sys.exit(1)

    #
    # EXIT SUCCESS
    #
    print ('\n')
    printHelper.success('EXIT gracefully')
