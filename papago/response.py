from papago.compat import json


class Response:
    """Result that is translated"""
    SUCCESS_CODE = 0

    def __init__(self, code=None, message=None, text=None, source=None):
        self.code = self.SUCCESS_CODE if code is None else code
        self.message = message
        self.text = text
        self.source = source

    @classmethod
    def parse_json(cls, body):
        """
        Get an instance from JSON string
        """
        json_dict = json.loads(body)
        if 'message' in json_dict:
            text = json_dict['message']['result']['translatedText']
            source = json_dict['message']['result']['srcLangType']
            return Response(text=text, source=source)
        else:
            return Response(code=json_dict.get('errorCode'), message=json_dict.get('errorMessage'))

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'Response(code={code}, message={message}, text={text}, source={source})'.format(
            code=self.code, message=self.message, text=self.text, src=self.source)


