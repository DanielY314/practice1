import requests

URL = 'https://w3schools.com/python/demopage.htm'

res = requests.get(URL)

print(res.status_code)
print(res.ok)
print(res.headers)
print(res.history)
print(res.content)
print(res.cookies)
print(res.text)
print(res.url)
print(res.encoding)
