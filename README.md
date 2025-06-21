# OpenSearch Demo App

A Python CLI application that demonstrates basic OpenSearch operations like creating an index, indexing documents, performing full-text search, filtering by category, and deleting the index.

## Features

- Create an index
- Index sample data
- Full-text search
- Filter by category
- Delete the index

## Requirements

- Python 3.10+
- OpenSearch running locally (default: `http://localhost:9200`)
- `opensearch-py` library

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2.	Run the app:

```bash
python main.py
```

Notes
- Make sure your OpenSearch instance is running and accessible.
- Default index name is products.
   
