from db import models, schemas, database
from db.database import get_db
import crud, auth_security, predict
from db.database import engine
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
import json


models.Base.metadata.create_all (engine)

app = FastAPI ()

app.add_middleware (CORSMiddleware,
                    allow_origins=["*"],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
                    
                    )


@app.post ("/token")
def login (form_data: OAuth2PasswordRequestForm = Depends()):

    if form_data.username == "admin" and form_data.password =="1234":
        token = jwt.encode ({"sub": form_data.username}, "secret123", algorithm="HS256")
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException (status_code=401, detail="Invalid Credentials")



@app.post ("/predict", response_model=schemas.PredictionOut)
def predict_endpoint (input_data: schemas.InputData, db: Session = Depends (get_db), user: str  = Depends (auth_security.get_current_user)):
    data_dict = input_data.model_dump()
    prediction = predict.predict_price (data_dict)
    crud.save_prediction(db, user, json.dumps(data_dict), prediction)
    return {"prediction": prediction}
    