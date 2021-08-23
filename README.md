# VaronisPythonAssignment
Usage:
1. MagicList:
```
from MagicList import MagicList
m = MagicList()
m[0] = 'hi'
print(m[0])
m[1] = 'by'
print(m[1])
print(m)
m[5] = 'error' (will fail)
```


API:

2.1 Run The API:
```
run the NormilizeAPI.py
```
2.2 request for token:
```
curl -X POST \
  http://127.0.0.1:8000/auth \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 13d7c031-14c4-a614-e3f3-12eb5791f383' \
  -d '{"username": "test", "password": "1234"}'
```
2.3 use the resulted token:
```
curl -X POST \
  http://127.0.0.1:8000/ \
  -H 'authorization: Bearer '<your token here>' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 6676408c-0f50-f343-e5f0-a7d86dea6e89' \
  -d '[{
    "name": "device",
    "strVal": "iPhone",
    "metadata": "not interesting"
},
    {
        "name": "isAuthorized",
        "boolVal": "false",
        "lastSeen": "not interesting"
    }
]'
```