import pandas as pd

def load_data():
    df = pd.read_csv("stock_data.csv")
    return df