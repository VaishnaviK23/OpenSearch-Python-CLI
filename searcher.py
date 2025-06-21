from opensearchpy import OpenSearch
from config import OPENSEARCH_HOST, INDEX_NAME

client = client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'MimbulusMimbultonia69$'),
    use_ssl=True,  # Set to True if you are using https
    verify_certs=False
)

def full_text_search(query: str):
    body = {
        "query": {
            "match": {
                "description": query
            }
        }
    }

    res = client.search(index=INDEX_NAME, body=body)
    print(f"\nResults for: '{query}'")
    for hit in res["hits"]["hits"]:
        print(f"- {hit['_source']['name']}: {hit['_source']['description']}")

def filter_by_category(category: str):
    body = {
        "query": {
            "term": {
                "category": category
            }
        }
    }

    res = client.search(index=INDEX_NAME, body=body)
    print(f"\nProducts in category '{category}':")
    for hit in res["hits"]["hits"]:
        print(f"- {hit['_source']['name']}")