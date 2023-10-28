import requests
import os
from dotenv import load_dotenv

class astraClass:
    def get(path: str):
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        return str(response.json())

        
    def post(path: str, data: dict):
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.post(url, json=data, headers=headers)
    
        return str(response.json())
    
    def delete(path: str):
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.delete(url, headers=headers)


        return str(response.json())
        
    def put(path: str, data: dict):
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.put(url, json=data, headers=headers)
    
        return str(response.json())
    
    def init(env: str = ".env"):
        load_dotenv(env)

astra = astraClass