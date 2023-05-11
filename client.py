import requests

def create_user(id):
    url='http://127.0.0.1:5000/add_shot'
    data={'id':id}
    response = requests.post(url,json=data)

    if response.status_code ==200:
        print('success')
    else:
        print('fail')

if __name__=='__main__':
    create_user("332288372")        