import os

import psycopg
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = (
    f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)
table = "currency_exchange_cache_table"


class Command(BaseCommand):
    def handle(self, *args, **options):
        conn = psycopg.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM {table} LIMIT 1;")
        if not cur.fetchone():
            print(f"Table {table} does not exist. Start to create...")
            cur.execute(
                f"CREATE TABLE {table} (cache_key varchar(255) PRIMARY KEY,"
                f" value text NOT NULL, expires timestamp NOT NULL);"
            )
            conn.commit()
        else:
            print(f"Table {table} already exist.")
        cur.close()
        conn.close()
