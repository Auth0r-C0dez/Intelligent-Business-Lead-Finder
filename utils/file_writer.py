import pandas as pd
import os


def save_to_csv(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
