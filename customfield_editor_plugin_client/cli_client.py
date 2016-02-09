import argparse
import sys
import colorama
import requests
from .helper.api_helper import ApiHelper
from .helper.api_helper_exceptions import ApiHelperException
from .helper.api_helper_exceptions import ValidationErrorsException
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
    print(colorama.Fore.CYAN + '\n~~ REST API Client for Customfield Editor Plugin ~~ v1.2rc1\n')

    #
    # CLI PARAMS
    #
    parser = argparse.ArgumentParser(description='Customfield Editor Plugin REST API CLI Client.')

    parser.add_argument("-a", "--action", help='Which action to execute.', choices=['adminListFields', 'adminGrantPermission', 'userListFields', 'userListOptions', 'userInsertOptions'])
    parser.add_argument("-url", "--baseUrl", help='baseUrl to JIRA instance e.g. http://server:port/jira/')
    parser.add_argument("-user", "--authUsername", help='username for basic auth.')
    parser.add_argument("-pass", "--authPassword", help='password for basic auth.')

    #
    # CLI PARAMS depending on action
    #
    parser.add_argument("-cid", "--customFieldId", type=int, help='The ID of the custom field.')
    parser.add_argument("-ctx", "--contextId", type=int, help='The ID of the custom field context.')
    parser.add_argument("-ulist", "--userList", nargs='+', help='space separated user names to grant permission')
    parser.add_argument("-glist", "--groupList", nargs='+', help='space separated group names to grant permission')
    parser.add_argument("-f", "--payloadFile", help='Payload JSON file.')

    args = parser.parse_args()
    if not args.action:
        printHelper.headline('USAGE')
        printHelper.step('admin operations')
        print ('    list fields:')
        print ('      $> cep-client -a adminListFields -url http://localhost:2990/jira/ -user admin -pass admin')
        print ('')
        print ('    grant permissions:')
        print ('      $> cep-client -a adminGrantPermission --customFieldId 10100 --userList bob steve \ \n'
               '                    -url http://localhost:2990/jira/ -user admin -pass admin')
        print ('      OPTIONAL: --groupList with one or more groupnames')

        printHelper.step('user operations')
        print ('    list fields:')
        print ('      $> cep-client -a userListFields -url http://localhost:2990/jira/ -user admin -pass admin')
        print ('')
        print ('    list options:')
        print ('      $> cep-client -a userListOptions --customFieldId 10001 -url http://localhost:2990/jira/ -user admin -pass admin')
        print ('      OPTIONAL: --contextId specify if you want another context other than default context')
        print ('')
        print ('    insert options:')
        print ('      $> cep-client -a userInsertOptions --customFieldId 10001 -f ./test-data/options-to-insert.json -url http://localhost:2990/jira/ -user admin -pass admin')
        print ('      FILE FORMAT: https://github.com/codeclou/customfield-editor-plugin/tree/cep-client/test-data/options-to-insert.json ')

        sys.exit(1)


    #
    # INITIALIZE HELPERS
    #
    printHelper.step('initializing')
    try:
        userInput = UserInput(args)
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
        #
        if args.action == 'adminListFields':
            adminOperations.list_fields()
        if args.action == 'adminGrantPermission':
            adminOperations.grant_permission(args.customFieldId, args.userList, args.groupList)


        #
        # USER ACTIONS
        #
        if args.action == 'userListFields':
            userOperations.list_fields()
        if args.action == 'userListOptions':
            userOperations.list_options(args.customFieldId, args.contextId)
        if args.action == 'userInsertOptions':
            try:
                with open(args.payloadFile) as payloadFile:
                    userOperations.insert_options(args.customFieldId, args.contextId, payloadFile)
            except FileNotFoundError as ex:
                printHelper.error('payloadFile not found')
                raise ApiHelperException('payloadFile not found')


    except requests.ConnectionError as ex:
        print ('')
        printHelper.error('There seemed to a be problem with your request. Check errors above. EXIT')
        print (ex)
        sys.exit(1)
    except ApiHelperException as ex:
        printHelper.pretty(ex.args[0])
        #if 'details' in ex:
        #    printHelper.pretty(ex.details)
        printHelper.error('There seemed to a be problem with your request. Check errors above. EXIT')
        sys.exit(1)

    #
    # EXIT SUCCESS
    #
    print ('\n')
    printHelper.success('EXIT gracefully')
