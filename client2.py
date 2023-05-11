import requests

response=requests.get('http://localhost:5000/data')
data=response.json()
print(data)

data_to_insert={'name':'chaya','number':'0527695444'}
response=requests.post('http://localhost:5000/data',json=data_to_insert)
print(response.text)

print("j")