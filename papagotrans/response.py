from papagotrans.compat import json


class Response:
    """Result that is translated"""
    SUCCESS_CODE = 0

    def __init__(self, code=None, message=None, text=None, src=None):
        self.code = self.SUCCESS_CODE if code is None else code
        self.message = message
        self.text = text
        self.src = src

    @classmethod
    def parse_json(cls, body):
        """
        Get an instance from JSON string
        """
        json_dict = json.loads(body)
        if 'message' in json_dict:
            text = json_dict['message']['result']['translatedText']
            src = json_dict['message']['result']['srcLangType']
            return Response(text=text, src=src)
        else:
            return Response(code=json_dict.get('errorCode'), message=json_dict.get('errorMessage'))

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'Response(code={code}, message={message}, text={text}, src={src})'.format(
            code=self.code, message=self.message, text=self.text, src=self.src)


