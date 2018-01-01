[![Build Status](https://travis-ci.org/stunstunstun/papago.svg?branch=master)](https://travis-ci.org/stunstunstun/papago)

# Papago API with Python

Unofficial Papago translation API with Python

- https://developers.naver.com/docs/nmt/reference/

## Install

#### PyPI

```bash
$ pip install papago
```

#### Download and Installing manually

```
$ git clone https://github.com/stunstunstun/papago.git
$ cd papago
$ python setup.py install
```

## Usage

#### Prerequisite

```
export CLIENT_ID='Your application's client id'
export CLIENT_SECRET='Your application's client secret'
```

#### Basic Usage

```
>>> from papago import Translator
>>> translator = Translator(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET'])
>>> response = translator.translate('안녕하세요')
>>> response = translator.translate('안녕하세요', 'ko', 'en')
>>> print(response)
Response(code=0, message=None, text=Hello., source=ko)
```


## Test

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r test-requirements.txt
```

```bash
$ python -m unittest
```

#### Languages Code

Code | Desc 
--|--
ko | Korean
en | English
ja | Japanese
zh-CN | Chinese
zh-TW | Chinese traditional
es | Spanish
fr | French
vi | Vietnamese
th | Thai
id | Indonesia

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
