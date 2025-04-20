from pydantic import BaseModel, EmailStr

class PostCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    date_of_birth: str
    address: str
    qualification: str

class PostOut(PostCreate):
    id: str
