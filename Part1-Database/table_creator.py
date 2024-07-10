import os
from dotenv import load_dotenv

import psycopg2

load_dotenv()

POSTGRE_USER = os.environ.get("POSTGRE_USER")
POSTGRE_PASSWORD = os.environ.get("POSTGRE_PASSWORD")


if __name__ == "__main__":
    try:
        db_connect = psycopg2.connect(
            user=POSTGRE_USER,
            password=POSTGRE_PASSWORD,
            host="localhost",
            port=5432,
            database="mydatabase",
        )
        print("Connection successful")
    except Exception as e:
        print(f"Error: {e}")