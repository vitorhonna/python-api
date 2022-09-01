import requests

print()

print(requests.get('http://localhost:8000/my-first-api').text)
print()
print(requests.get('http://localhost:8000/hello').text)
print(requests.get('http://localhost:8000/hello?name=Vitor').text)
