import pandas as pd
def load_and_clean_data(path):
    raw_data = pd.read_csv(path)
    raw_data.drop_duplicates(inplace=True)
    return raw_data