from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId

class PostDBModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    full_name: str
    email: EmailStr
    phone_number: str
    date_of_birth: str  # YYYY-MM-DD
    address: str
    qualification: str

    class Config:
        json_encoders = {
            ObjectId: str
        }
        allow_population_by_field_name = True
