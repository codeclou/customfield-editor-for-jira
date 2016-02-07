from customfield_editor_plugin_client.helper.print_helper import PrintHelper
from customfield_editor_plugin_client.helper.api_helper import ApiHelper

class UserOperations:

    def __init__(self, api_helper):
        self._print = PrintHelper()
        self._api = api_helper

    def list_fields(self):
        response_json = self._api.get('/user/customfields')
        self._print.table(response_json)

    def list_options(self, customfield_id, context_id):
        if context_id:
            response_json = self._api.get('/user/customfields/{0}/contexts/{1}/options'.format(customfield_id, context_id))
        else:
            response_json = self._api.get('/user/customfields/{0}/contexts/default/options'.format(customfield_id))

        self._print.table(response_json)
