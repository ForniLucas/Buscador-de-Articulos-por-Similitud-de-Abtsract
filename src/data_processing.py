import json
import os
import pandas as pd

def load_and_preprocess_data(file_path,max_lines):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for _ in range(max_lines) if (line := f.readline())]
    return pd.DataFrame(data)