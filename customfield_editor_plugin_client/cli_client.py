import argparse
from .api_helper import ApiHelper


def main():
    parser = argparse.ArgumentParser(description='Customfield Editor Plugin REST API CLI Client.')

    parser.add_argument("-cid", "--customFieldId", type=int, help='The ID of the custom field.')

    parser.add_argument("-a", "--action", help='Which action to execute.', choices=['adminListFields', 'insertOptions','deleteOption'], required=True)

    parser.add_argument("-url", "--baseUrl", help='baseUrl to JIRA instance e.g. http://server:port/jira/', required=True)

    parser.add_argument("-user", "--authUsername", help='username for basic auth.', required=True)

    parser.add_argument("-pass", "--authPassword", help='password for basic auth.', required=True)

    # https://docs.python.org/3/howto/argparse.html
    args = parser.parse_args()

    #  cep-client -a adminListFields -url http://localhost:2990/jira/ -user admin -pass admin
    if args.action == 'adminListFields':
        helper = ApiHelper(args.baseUrl, args.authUsername, args.authPassword)
        helper.get('/admin/customfields')

