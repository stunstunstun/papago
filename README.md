[![Build Status](https://travis-ci.org/stunstunstun/papagotrans.svg?branch=master)](https://travis-ci.org/stunstunstun/papagotrans)

# PAPAGO Translate API with Python (Unofficial)

네이버에서 제공하는 파파고 기계 번역 API를 Python을 통해 제공하는 모듈입니다. 파파고는 입력된 텍스트를 다른 나라 언어(영어, 일본어, 중국어)로 번역한 텍스트로 출력해주는 REST API 입니다. 

기계 번역을 애플리케이션에 통합하기 위해서는 네이버 개발자 페이지에서 애플리케이션을 등록하고 Client ID 와 Client Secret 를 발급해야 합니다.

> https://developers.naver.com/docs/labs/translator/

## Install

#### PyPI

```bash
$ pip install papagotrans
```

#### Download and Install

```
$ git clone https://github.com/stunstunstun/papagotrans.git
$ cd papagotrans
$ python setup.py install
```

#### Quick Start

```
export CLIENT_ID='Your application's client id'
export CLIENT_SECRET='Your application's client secret'
```

#### Usage

```bash
>>> from papagotrans import Translator
>>> translator = Translator(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET'])
>>> response = translator.translate('안녕하세요')
>>> response = translator.translate('안녕하세요', 'ko', 'en')
>>> print(response)
Response(code=0, message=None, text=Hello., source=ko)
>>> 
```

#### Languages Code

Code | Desc 
--|--
ko | Korean
en | English
ja | Japanese
zh-CN | Chinese

## License

```
The MIT License (MIT)

Copyright (c) 2017 Minhyeok Jung

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
