import requests

access_token = '2598305919485473-12345678-031820-X-12345678'
site_id = 'MLA'
category = 'MLA1144'

url = f'https://api.mercadolibre.com/sites/{site_id}/search?category={category}'
headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    for item in data['results']:
        print(f"Id: {item['id']}, Title: {item['title']}, Price: {item['price']}")

        id = item['id']
        title = item['title']
        price = item['price']
        currency = item['currency_id']
        date = item['stop_time']
        available_quantity = item['available_quantity']

        print(id)
        print(title)
        print(price)
        print(date)
        print(currency)
        print(available_quantity)
