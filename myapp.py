import requests
import json

URL='http://127.0.0.1:8000/studentapi/'


def get_data(id=None):
    #retrives data as a whole or any individual content
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)



def post_data():
    #adds data to the database
    data={
        'name':'sample02',
        'roll':104,
        'city':'city02'
    }

    json_data=json.dumps(data)

    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)



def update_data():
    #make partial or full update of any existing data
    data={
        'id':4,
        'name':'sample08',
        'city':'city08'
    }

    json_data=json.dumps(data)

    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)



def delete_data():
    #delete any data
    data={'id':4}

    json_data=json.dumps(data)

    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)



# uncomment any one of below based on the operation that has to be performed
get_data()
# post_data()
# update_data()
# delete_data()