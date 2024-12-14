from model import Model
from fastapi import FastAPI
from Prediciton import prediction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],    
    allow_headers=["*"],   
)


model = Model()

@app.post("/predict")
def predict(input: prediction):
    result = model.predict(input.bedrooms, input.bathrooms, input.sqft_living, input.sqft_lot, input.floors, input.sqft_above, input.sqft_basement, input.yr_built)

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
