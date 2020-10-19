import joblib
import pandas as pd

def predict():
    #load data
    X = pd.read_csv("../data/processed/processed_iris.csv")
    
    #load model
    model = joblib.load("../models/model")
    
    #make predictions
    predictions = pd.Series(model.predict(X))
    
    #save predictions
    predictions.to_csv("../data/predictions/predictions.csv", index = False) 

if __name__ == "__main__":
    predict()