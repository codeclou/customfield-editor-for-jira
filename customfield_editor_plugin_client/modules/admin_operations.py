from customfield_editor_plugin_client.helper.print_helper import PrintHelper
from customfield_editor_plugin_client.helper.api_helper import ApiHelper

class AdminOperations:

    def __init__(self, api_helper):
        self._print = PrintHelper()
        self._api = api_helper

    def list_fields(self):
        response_json = self._api.get('/admin/customfields')
        self._print.table(response_json)

    def grant_permission(self, customfield_id, userlist, grouplist):
        # (1) Get current permissions
        permissions = self._api.get('/admin/customfields/{0}'.format(customfield_id))
        print ('  permissions BEFORE: ')
        self._print.table(permissions)
        print ('')

        # (2) join current permission lists with new userlist and grouplist
        if userlist and len(userlist) > 0:
            permissions['userlist'] = permissions['userlist'] + list(set(userlist) - set(permissions['userlist']))
        if grouplist and len(grouplist) > 0:
            permissions['grouplist'] = permissions['grouplist'] + list(set(grouplist) - set(permissions['grouplist']))

        # (3) Save merged permissions
        response_json = self._api.put('/admin/customfields/{0}'.format(customfield_id), permissions)
        print ('  permissions AFTER: ')
        self._print.table(permissions)
        print ('')
