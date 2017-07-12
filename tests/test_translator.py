#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from papago import Translator


class TestTranslator(unittest.TestCase):
    def setUp(self):
        """
        setup your application client keys
        - https://developers.naver.com/docs/common/apicall/
        """
        self.translator = Translator(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET'])
        pass

    def test_translate(self):
        """
        Test that say hello translate to english
        """
        response = self.translator.translate('안녕하세요')
        self.assertEqual(response.text, 'Hello.')

    def test_translate_with_source(self):
        """
        Test that source language translate to target language
        """
        response = self.translator.translate('안녕하세요', 'ko', 'ja')
        self.assertIsNotNone(response.text)

    def test_translate_invalid_source(self):
        """
        Test that invalid source languages
        """
        self.assertRaises(ValueError, self.translator.translate, 'Hola', 'es', 'en')
