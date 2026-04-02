from fastapi import APIRouter
import joblib
import numpy as np
from app.models import CropFeatures

router = APIRouter()

rf_model = joblib.load("rf_model.pkl")

@router.post("/predict/rf")
def predict_rf(data: CropFeatures):
    features = np.array([[ 
        data.N, data.P, data.K,
        data.temperature, data.humidity,
        data.ph, data.rainfall
    ]])
    
    prediction = rf_model.predict(features)
    
    return {"modelo": "RandomForest", "cultivo": prediction[0]}