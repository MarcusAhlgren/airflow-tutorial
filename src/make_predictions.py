import joblib
import pandas as pd
from src.paths import PROCESSED_DATA_PATH, PREDICTIONS_PATH, MODEL_PATH

def predict():
    #load data
    X = pd.read_csv(PROCESSED_DATA_PATH)
    
    #load model
    model = joblib.load(MODEL_PATH)

    #model = pickle.load(open(MODEL_PATH, 'rb'))
    
    #make predictions
    predictions = pd.Series(model.predict(X))
    
    #save predictions
    predictions.to_csv(PREDICTIONS_PATH, index = False) 

if __name__ == "__main__":
    predict()