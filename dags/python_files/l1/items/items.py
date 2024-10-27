import requests
from python_files.lib.infra import database_connection
import os
from dotenv import load_dotenv
import os

load_dotenv()

def insert_items():
    
    site_id = 'MLA'
    category = 'MLA1144'

    url = f'https://api.mercadolibre.com/sites/{site_id}/search?category={category}'
    headers = {'Authorization': f'Bearer {os.getenv('API_KEY')}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)

        conn = database_connection() 

        cursor = conn.cursor()

        for item in data['results']:
            print(f"Id: {item['id']}, Title: {item['title']}, Price: {item['price']}")

            id = item['id']
            title = item['title']

            insert_query = f"""
            BEGIN TRANSACTION;

            CREATE TEMPORARY TABLE items_temporary AS (
            SELECT * FROM "2024_melissa_herszage_schema".l1_items LIMIT 0);

            INSERT INTO items_temporary (id, title, created_at) VALUES
            ('{id}', '{title}', current_timestamp);

            INSERT INTO "2024_melissa_herszage_schema".l1_items 
            (SELECT id, title, created_at FROM items_temporary it WHERE id NOT IN 
            (SELECT id FROM "2024_melissa_herszage_schema".l1_items)
            );

            DROP TABLE items_temporary;

            END TRANSACTION;
            """

            # Ejecutar la query
            cursor.execute(insert_query)
            print('Query executed')

        conn.commit()
        print('Results committed')

        cursor.close()
        conn.close()

    else:
        print('Error:', response.status_code)