import requests
import pandas as pd
import psycopg2


def insert_items():
    access_token = '2598305919485473-12345678-031820-X-12345678'
    site_id = 'MLA'
    category = 'MLA1144'

    url = f'https://api.mercadolibre.com/sites/{site_id}/search?category={category}'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)

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

        cursor = conn.cursor()

        for item in data['results']:
            print(f"Id: {item['id']}, Title: {item['title']}, Price: {item['price']}")

            id = item['id']
            title = item['title']

            insert_query = f"""
            BEGIN TRANSACTION;

            CREATE TEMPORARY TABLE items_temporary AS (
            SELECT * FROM public.items LIMIT 0);

            INSERT INTO items_temporary (id, title) VALUES
            ('{id}', '{title}');

            INSERT INTO public.items (SELECT id, title FROM items_temporary it WHERE id NOT IN (SELECT id FROM public.items));

            DROP TABLE items_temporary;

            END TRANSACTION;
            """

            # Execute the query
            cursor.execute(insert_query)
            print('Query executed')

        conn.commit()
        print('Results committed')

        cursor.close()
        conn.close()

    else:
        print('Error:', response.status_code)


