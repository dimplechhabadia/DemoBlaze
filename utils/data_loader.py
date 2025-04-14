import json
import os

def load_json(file_name):
    base_path = os.path.dirname(__file__)  # Get current directory
    data_path = os.path.join(base_path, '..', 'testdata', file_name)
    with open(data_path, 'r') as f:
        return json.load(f)
