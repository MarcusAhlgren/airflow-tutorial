import pandas as pd

def preprocess():
    #load data
    df = pd.read_csv("../data/raw/iris.csv")

    #drop unnecessary columns
    df = df.drop(["Id", "Species"], axis = 1)

    #save processed data
    df.to_csv("../data/processed/processed_iris.csv", index = False)

if __name__ == "__main__":
    preprocess()