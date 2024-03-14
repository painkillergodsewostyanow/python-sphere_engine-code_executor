import time

import requests

from sphere_engine import CompilersClientV4


class CodeExecutor:
    def __init__(self, token, widget_id, lang_id):
        self.client = CompilersClientV4(token, widget_id)
        self.lang_id = lang_id
        self.response = None
        self._id = None
        self.source_code = None
        self.errors = None
        self.output = None
        self.cmpinfo = None

    def execute(self, source_code, input_data=None, priority=None, time_limit=None, memory_limit=None,
                compiler_version_id=None):

        self._id = self.client.submissions.create(
            source_code, self.lang_id, _input=input_data, priority=priority,
            time_limit=time_limit, memory_limit=memory_limit,
            compiler_version_id=compiler_version_id
        )['id']

        self.update_param()

    def update_param(self):
        self.response = self.client.submissions.get(self._id)
        while self.response['executing']:
            time.sleep(0.4)
            self.response = self.client.submissions.get(self._id)

        result = self.response['result']

        source_code_link = result['streams']['source']['uri'] if result['streams']['source'] else None
        output_link = result['streams']['output']['uri'] if result['streams']['output'] else None
        errors_link = result['streams']['error']['uri'] if result['streams']['error'] else None
        cmpinfo_link = result['streams']['cmpinfo']['uri'] if result['streams']['cmpinfo'] else None

        self.source_code = self.__parse_from_web(source_code_link) if source_code_link else None
        self.output = self.__parse_from_web(output_link) if output_link else None
        self.errors = self.__parse_from_web(errors_link) if errors_link else None
        self.cmpinfo = self.__parse_from_web(cmpinfo_link) if cmpinfo_link else None

    @staticmethod
    def __parse_from_web(link):
        response = requests.get(link, stream=True)
        return response.content.decode()
