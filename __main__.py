import requests
import os
from dotenv import load_dotenv

class astraClass:
    """Astra driver wrapper for the Document API. Provides you with high level functions to interact with the Datastax API's HTTP verbs."""
    def get(path: str):
        """Interface for the GET verb, used to fetch data from a collection or a document."""
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        return str(response.json())

        
    def post(path: str, data: dict):
        """Interface for the POST verb, used to write data to a collection or a document."""
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.post(url, json=data, headers=headers)
    
        return str(response.json())
    
    def delete(path: str):
        """Interface for the DELETE verb, used to delete data from a collection or a document."""
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.delete(url, headers=headers)


        return str(response.json())
        
    def put(path: str, data: dict):
        """Interface for the PUT verb, used to modify data of a collection or a document."""
        url = f'https://{os.environ.get("ASTRA_DB_ID")}-{os.environ.get("ASTRA_DB_REGION")}.apps.astra.datastax.com/api/rest/v2/namespaces/{os.environ.get("ASTRA_DB_KEYSPACE")}/collections/{path}'

        headers = {
        'X-Cassandra-Token': os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
        'Content-Type': 'application/json'
        }

        response = requests.put(url, json=data, headers=headers)
    
        return str(response.json())
    
    def init(env: str = ".env"):
        """Loads envoirnement variables from your envoirnement file. The default path is .env"""
        load_dotenv(env)

astra = astraClass