import requests

res =requests.get('http://textfiles.com/computers/mrdos1000.txt')
try:
    res.raise_for_status()
    print("Status code:", res.status_code)
    print("Length of the text:",len(res.text))
    print(res.text[:100])
except Exception as exc:
    print("Oh No: %s" %(exc))
