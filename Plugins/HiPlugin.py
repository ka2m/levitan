from template import PluginTemplate


class HiPlugin(PluginTemplate):
    """
    HiPlugin - simplest plugin to check that Levitan is running.
    It responds 'hello' to 'hello' from user
    """
    def __init__(self, config):
        PluginTemplate.__init__(self, config)
        self.requests = ["^\s*hello\s*$"]

    # def plugin_process_request(self, skype_message):
    #     """
    #     It doesn't override template version
    #     """
    #     return PluginTemplate.plugin_process_request(self, skype_message)

    def process(self, skype_message):
        return "hello"

    def check_plugin_config(self):
        return {'status': True, 'errorMessage': None}

    def hello(self):
        return "HiPlugin"