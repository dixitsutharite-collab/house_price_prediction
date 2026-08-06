from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import joblib
app = FastAPI()
model = joblib.load("house_price_model.joblib")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class House(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    Population: float
    Latitude: float
    Longitude: float

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.post("/predict")
def predict_price(data: House):
    df = pd.DataFrame(
        [[
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.Population,
        data.Latitude,
        data.Longitude
    ]],
    columns=['MedInc', 'HouseAge', 'AveRooms', 'Population', 'Latitude', 'Longitude']
    )

    prediction = model.predict(df)
    return {"predicted_price": float(prediction[0])}