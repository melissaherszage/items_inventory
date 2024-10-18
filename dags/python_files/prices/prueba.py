import requests
import pandas as pd

access_token = '2598305919485473-12345678-031820-X-12345678'

item_id = 'MLA23240332'  # Replace with the item ID
site_id = 'MLA'
url = f'https://api.mercadolibre.com/items/{item_id}'
print(url)

headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(url, headers=headers)
print(response)

if response.status_code == 200:
    data = response.json()
    #print(f"Item Price: {data['price']}")
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(f"Response text: {response.text}")

