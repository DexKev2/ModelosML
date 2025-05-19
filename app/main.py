from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib  # ✅ Usamos joblib en lugar de pycaret

# Inicializa la aplicación FastAPI
app = FastAPI()

# Configura CORS (permite peticiones desde cualquier origen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Carga el modelo KNN entrenado con joblib
model = joblib.load("model.pkl")

# Clase que define los campos esperados del JSON de entrada
class MushroomFeatures(BaseModel):
    Capshape: int
    Capsurf: int
    Capcolor: int
    Bruises: int
    Odor: int
    Gillatt: int
    Gillspace: int
    Gillsize: int
    Gillcolor: int
    Stalkshape: int
    Stalkroot: int
    Ssurfabove: int
    Ssurfbelow: int
    Scolorabove: int
    Scolorbelow: int
    Veiltype: int
    Veilcolor: int
    Ringnum: int
    Ringtype: int
    Spore: int
    Pop: int
    Habitat: int

# Ruta de predicción
@app.post("/predict/")
def predict_mushroom(features: MushroomFeatures):
    try:
        # Convierte los datos recibidos a un DataFrame
        input_data = pd.DataFrame([features.dict()])

        # Realiza la predicción
        pred = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0].max()

        return {
            "prediction": "EDIBLE" if pred == 0 else "POISONOUS",
            "confidence": float(prob)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Lanza el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
