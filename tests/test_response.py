#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from tests.compat import json
from papago.response import Response


class TestResponse(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse_json(self):
        body = json.dumps({'message': {'result': {'translatedText': 'Hello', 'srcLangType': 'ko'}}})
        response = Response.parse_json(body)
        self.assertEqual(response.code, Response.SUCCESS_CODE)

    def test_parse_failed_json(self):
        body = json.dumps({'errorCode': 405, 'errorMessage': 'Not Found Resources'})
        response = Response.parse_json(body)
        self.assertNotEqual(response.code, Response.SUCCESS_CODE)
