import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'word': ['bull', 'bear'], 'count': [
        files['content'].str.contains(r'\sbull\s', regex=True).sum(),
        files['content'].str.contains(r'\sbear\s', regex=True).sum()
    ]})