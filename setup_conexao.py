# -*- coding: utf-8 -*-
import sys
import io
import os

os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['PGCLIENTENCODING'] = 'UTF8'

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import psycopg2
from pymongo import MongoClient

PG_CONFIG = {
    "dbname": "loctra_db",
    "user": "postgres",
    "password":"123456789", 
    "host": "localhost",
}
MONGO_URI = "mongodb://localhost:27017/"

def testar_conexao():
    # Teste PostgreSQL
    try:
        pg_conn = psycopg2.connect(**PG_CONFIG)
        print("✅ PostgreSQL conectado com sucesso!")
        pg_conn.close()
    except UnicodeDecodeError as e:
        # Decodifica a mensagem crua em latin-1
        mensagem = e.object.decode('latin-1')
        print(f"❌ Erro PostgreSQL: {mensagem}")
    except Exception as e:
        print(f"❌ Erro PostgreSQL: {e}")

    # Teste MongoDB
    try:
        mongo_client = MongoClient(MONGO_URI)
        mongo_client.admin.command('ping')
        print("✅ MongoDB conectado com sucesso!")
    except Exception as e:
        print(f"❌ Erro MongoDB: {e}")

if __name__ == "__main__":
    testar_conexao()