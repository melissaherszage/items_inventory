import requests
from datetime import datetime, timedelta
from python_files.lib.infra import database_connection
import os
from dotenv import load_dotenv

load_dotenv()

def insert_prices():

    conn = database_connection()

    max_date_query = f"""
                SELECT COALESCE(MAX(date(created_at)), '2024-10-16') FROM "2024_melissa_herszage_schema".l1_item_prices
                """
    
    cursor = conn.cursor()
    cursor.execute(max_date_query)
    results_max_date = cursor.fetchone()

    max_date = results_max_date[0]
    print(max_date)

    # Defino variables de fechas
    ultimo_archivo = max_date
    hoy = datetime.today().date() 

    while ultimo_archivo < hoy:
    
        site_id = 'MLA'
        category = 'MLA1144'
        url = f'https://api.mercadolibre.com/sites/{site_id}/search?category={category}'
        headers = {'Authorization': f'Bearer {os.getenv('API_KEY')}'}

        
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for product in data['results']:

                    item_id = product['id']
                    price = product['price']
                    currency = product['currency_id']
                    available_quantity = product['available_quantity']
                    condition = product['condition']

                    insert_query_prices = f"""
                    INSERT INTO "2024_melissa_herszage_schema".l1_item_prices (item_id, condition, price, currency, available_quantity, created_at) VALUES
                    ('{item_id}', '{condition}', {price}, '{currency}', {available_quantity}, current_timestamp);
                    """

                    # Execute the query
                    print(insert_query_prices)
                    cursor = conn.cursor()
                    cursor.execute(insert_query_prices)
                    print('Query executed')

            conn.commit()
            cursor.close()
            conn.close()

            ultimo_archivo += timedelta(days=1)

        else:
            print('Error:', response.status_code)

    


