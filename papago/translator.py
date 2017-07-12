import requests
from papago.response import Response
from papago.contants import PAPAGO_API_URL, DEFAULT_CONTENT_TYPE, LANGUAGES


class Translator:
    """PAPAGO translate API implementation class
    You can create an instance to translate
    :param client_id: client id that to use API 
    :param client_secret: client_secret that to use API
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        pass

    def translate(self, text, source='ko', target='en'):
        """Translate source language to target language
            :param text: source text to translate
            :param source: source language code
            :param target: target language code
            :rtype: Response
        """
        if source not in LANGUAGES:
            raise ValueError('This source languages is not supported')
        payload = {'text': text, 'source': source, 'target': target}
        headers = {'X-Naver-Client-Id': self.client_id,
                   'X-Naver-Client-Secret': self.client_secret,
                   'Content-Type': DEFAULT_CONTENT_TYPE}
        body = requests.post(PAPAGO_API_URL, headers=headers, data=payload)
        if body.status_code != 200:
            raise Exception('HTTP status code is not OK[{}]'.format(body.status_code))
        return Response.parse_json(body.text)
