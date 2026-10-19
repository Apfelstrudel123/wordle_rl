import pandas as pd
import random

def load_data(path: str):
    df = pd.read_csv(path)
    lst = df.columns.tolist()
    data = [s.strip().lower() for s in lst]
    return data

def sample_word(data: list):
    return random.choice(data)
