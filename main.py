from fastapi import FastAPI
from app.routes import rf_routes, svm_routes

app = FastAPI(title="API Recomendación de Cultivos")

app.include_router(rf_routes.router)
app.include_router(svm_routes.router)