import pandas as pd


def load_data(fileindex):
    try:
        data = pd.read_csv(fileindex, dtype=float, sep='\t', index_col=0)
        return data
    except Exception as e:
        return e
