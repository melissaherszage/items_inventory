from pendulum import today
import requests
import pandas as pd
import psycopg2
from datetime import datetime

def insert_prices():

    conn_params = {
            'host': 'redshift-pda-cluster.cnuimntownzt.us-east-2.redshift.amazonaws.com',
            'dbname': 'pda',
            'user': '2024_melissa_herszage',
            'password': 'K6@L2^!9x$Rw',
            'port': 5439
        }

    conn = psycopg2.connect(
            host=conn_params['host'],
            dbname=conn_params['dbname'],
            user=conn_params['user'],
            password=conn_params['password'],
            port=conn_params['port']
        )

    max_date_query = f"""
                SELECT MAX(date(created_at)) FROM public.item_prices
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
        access_token = '2598305919485473-12345678-031820-X-12345678'
        url = f'https://api.mercadolibre.com/sites/{site_id}/search?category={category}'
        headers = {'Authorization': f'Bearer {access_token}'}

        
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for product in data['results']:

                    item_id = product['id']
                    price = product['price']
                    currency = product['currency_id']
                    available_quantity = product['available_quantity']

                    insert_query_prices = f"""
                    INSERT INTO public.item_prices (item_id, price, currency, available_quantity, created_at) VALUES
                    ('{item_id}', {price}, '{currency}', {available_quantity}, current_timestamp);
                    """

                    # Execute the query
                    print(insert_query_prices)
                    cursor = conn.cursor()
                    cursor.execute(insert_query_prices)
                    print('Query executed')

            conn.commit()
            cursor.close()
            conn.close()

        else:
            print('Error:', response.status_code)

    


