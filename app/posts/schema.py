from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

# Custom ObjectId validator for Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# Nested schemas for states_and_cities
class CityBase(BaseModel):
    city_id: str
    name: str

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "city_id": "60d5f7c9b1d5e9b4a8f9a2b3",
                "name": "Mumbai"
            }
        }

class StatesAndCitiesCreate(BaseModel):
    name: str
    cities: List[CityBase]

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Maharashtra",
                "cities": [
                    {"city_id": "60d5f7c9b1d5e9b4a8f9a2b3", "name": "Mumbai"},
                    {"city_id": "60d5f7c9b1d5e9b4a8f9a2b4", "name": "Pune"}
                ]
            }
        }

class StatesAndCitiesResponse(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    cities: List[CityBase]

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class StatesAndCitiesUpdate(BaseModel):
    name: Optional[str] = None
    cities: Optional[List[CityBase]] = None

# Nested schemas for scheme_posts, gov_jobs_posts, digital_services
class DocumentBase(BaseModel):
    name: str
    type: Optional[str] = None
    description: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Aadhaar Card",
                "type": "ID",
                "description": "Proof of identity"
            }
        }

class UpdateBase(BaseModel):
    date: datetime
    note: str

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "date": "2025-04-01T00:00:00",
                "note": "Application window opened"
            }
        }

# Schemas for sectors
class SectorCreate(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Education",
                "description": "Sector for educational services and schemes"
            }
        }

class SectorResponse(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    description: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class SectorUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

# Schemas for scheme_posts
class SchemePostCreate(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    description: str
    required_documents: List[DocumentBase]
    states: List[str]
    cities: List[str]
    updates: List[UpdateBase]
    sector_id: str

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Scholarship Scheme 2025",
                "start_date": "2025-01-01T00:00:00",
                "end_date": "2025-12-31T23:59:59",
                "description": "A scholarship program for students",
                "required_documents": [
                    {"name": "Aadhaar Card", "type": "ID", "description": "Proof of identity"}
                ],
                "states": ["Maharashtra", "Karnataka"],
                "cities": ["Mumbai", "Bangalore"],
                "updates": [
                    {"date": "2025-04-01T00:00:00", "note": "Application window opened"}
                ],
                "sector_id": "60d5f7c9b1d5e9b4a8f9a2b5"
            }
        }

class SchemePostResponse(BaseModel):
    id: str = Field(..., alias="_id")
    title: str
    start_date: datetime
    end_date: datetime
    description: str
    required_documents: List[DocumentBase]
    states: List[str]
    cities: List[str]
    updates: List[UpdateBase]
    sector_id: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class SchemePostUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    description: Optional[str] = None
    required_documents: Optional[List[DocumentBase]] = None
    states: Optional[List[str]] = None
    cities: Optional[List[str]] = None
    updates: Optional[List[UpdateBase]] = None
    sector_id: Optional[str] = None

# Schemas for gov_jobs_posts
class GovJobPostCreate(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    description: str
    required_documents: List[DocumentBase]
    states: List[str]
    cities: List[str]
    updates: List[UpdateBase]
    sector_id: str

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Government Teacher Recruitment 2025",
                "start_date": "2025-02-01T00:00:00",
                "end_date": "2025-03-31T23:59:59",
                "description": "Recruitment for government school teachers",
                "required_documents": [
                    {"name": "Resume", "type": "Document", "description": "Job application resume"}
                ],
                "states": ["Tamil Nadu", "Kerala"],
                "cities": ["Chennai", "Kochi"],
                "updates": [
                    {"date": "2025-02-15T00:00:00", "note": "Exam schedule released"}
                ],
                "sector_id": "60d5f7c9b1d5e9b4a8f9a2b6"
            }
        }

class GovJobPostResponse(BaseModel):
    id: str = Field(..., alias="_id")
    title: str
    start_date: datetime
    end_date: datetime
    description: str
    required_documents: List[DocumentBase]
    states: List[str]
    cities: List[str]
    updates: List[UpdateBase]
    sector_id: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class GovJobPostUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    description: Optional[str] = None
    required_documents: Optional[List[DocumentBase]] = None
    states: Optional[List[str]] = None
    cities: Optional[List[str]] = None
    updates: Optional[List[UpdateBase]] = None
    sector_id: Optional[str] = None

# Schemas for digital_services
class DigitalServiceCreate(BaseModel):
    title: str
    description: str
    required_documents: List[DocumentBase]
    updates: List[UpdateBase]
    states: List[str]
    cities: List[str]

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Online Tax Filing Service",
                "description": "Digital service for filing taxes online",
                "required_documents": [
                    {"name": "PAN Card", "type": "ID", "description": "Permanent Account Number"}
                ],
                "updates": [
                    {"date": "2025-03-01T00:00:00", "note": "New portal launched"}
                ],
                "states": ["Gujarat", "Rajasthan"],
                "cities": ["Ahmedabad", "Jaipur"]
            }
        }

class DigitalServiceResponse(BaseModel):
    id: str = Field(..., alias="_id")
    title: str
    description: str
    required_documents: List[DocumentBase]
    updates: List[UpdateBase]
    states: List[str]
    cities: List[str]

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class DigitalServiceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    required_documents: Optional[List[DocumentBase]] = None
    updates: Optional[List[UpdateBase]] = None
    states: Optional[List[str]] = None
    cities: Optional[List[str]] = None