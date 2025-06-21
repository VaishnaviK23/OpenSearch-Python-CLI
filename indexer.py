import json
from opensearchpy import OpenSearch
from config import OPENSEARCH_HOST, INDEX_NAME

client = client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'your_password_here'),
    use_ssl=True,  # Set to True if you are using https
    verify_certs=False
)

def create_index():
    if client.indices.exists(INDEX_NAME):
        print(f"Index '{INDEX_NAME}' already exists.")
        return

    mapping = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "text"},
                "category": {"type": "keyword"},
                "price": {"type": "float"},
                "description": {"type": "text"}
            }
        }
    }

    client.indices.create(index=INDEX_NAME, body=mapping)
    print(f"Index '{INDEX_NAME}' created successfully.")

def index_data():
    with open("sample_data.json") as f:
        data = json.load(f)
    
    for item in data:
        client.index(index=INDEX_NAME, id=item["id"], body=item)
        print(f"Indexed: {item['name']}")

def delete_index():
    client.indices.delete(index=INDEX_NAME, ignore=[400, 404])
    print(f"Index '{INDEX_NAME}' deleted.")