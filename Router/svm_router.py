from fastapi import APIRouter
import joblib
import numpy as np
from app.models import CropFeatures

router = APIRouter()

svm_model = joblib.load("svm_model.pkl")

@router.post("/predict/svm")
def predict_svm(data: CropFeatures):
    features = np.array([[ 
        data.N, data.P, data.K,
        data.temperature, data.humidity,
        data.ph, data.rainfall
    ]])
    
    prediction = svm_model.predict(features)
    
    return {"modelo": "SVM", "cultivo": prediction[0]}