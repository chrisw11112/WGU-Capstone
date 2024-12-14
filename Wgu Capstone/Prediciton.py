from pydantic import BaseModel

class prediction(BaseModel):
    bedrooms: int
    bathrooms: int
    sqft_living: int
    sqft_lot: int
    floors: int
    sqft_above: int
    sqft_basement: int
    yr_built: int