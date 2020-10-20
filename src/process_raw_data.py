import pandas as pd
from src.paths import RAW_DATA_PATH, PROCESSED_DATA_PATH

def preprocess():
    #load data
    df = pd.read_csv(RAW_DATA_PATH)

    #drop unnecessary columns
    df = df.drop(["Id", "Species"], axis = 1)

    #save processed data
    df.to_csv(PROCESSED_DATA_PATH, index = False)

if __name__ == "__main__":
    preprocess()