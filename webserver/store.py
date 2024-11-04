import requests

API_BASE_URL = 'https://api.escuelajs.co/api/v1'

def get_categories():
    r = requests.get(API_BASE_URL + '/categories')
    print(f'Status code: {r.status_code}')
    
    categories = r.json()
    for category in categories:
        print(category['name'])