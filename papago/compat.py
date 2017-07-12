import sys
try:
    import simplejson as json
except ImportError:
    import json

PY3 = sys.version_info > (3, )

