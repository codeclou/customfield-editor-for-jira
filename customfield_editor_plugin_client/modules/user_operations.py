import json
from customfield_editor_plugin_client.helper.print_helper import PrintHelper
from customfield_editor_plugin_client.helper.api_helper import ApiHelper
from customfield_editor_plugin_client.helper.api_helper_exceptions import ApiHelperException

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


    def insert_options(self, customfield_id, context_id, options):
        optionsJson = json.load(options)
        self._print.table(optionsJson)
        if context_id:
            context_infix = context_id
        else:
            context_infix = 'default'

        for option in optionsJson:
            created_option = self._api.post('/user/customfields/{0}/contexts/{1}/options'.format(customfield_id, context_infix),
                                           {
                                               "optionvalue": option['optionvalue']
                                           })
            if created_option and 'id' in created_option:
                self._print.pretty(created_option)
                if 'default' in option:
                    self._api.put('/user/customfields/{0}/contexts/{1}/options/default'.format(customfield_id, context_infix),
                                {
                                    "optionId": created_option['id']
                                })

    def sort_options(self, customfield_id, context_id, order):
        if context_id:
            context_infix = context_id
        else:
            context_infix = 'default'

        self._api.put('/user/customfields/{0}/contexts/{1}/options/sort'.format(customfield_id, context_infix),
                                        {
                                            "order": order,
                                            "locale": "de-DE"
                                        })
