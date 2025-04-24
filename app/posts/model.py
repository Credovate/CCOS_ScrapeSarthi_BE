from pymongo.collection import Collection
from bson import ObjectId
from typing import List, Dict, Optional
from datetime import datetime

# Nested class for City in states_and_cities
class City:
    def __init__(self, city_id: str, name: str):
        self.city_id = city_id  # Keep as string
        self.name = name

    def to_dict(self) -> Dict:
        return {
            "city_id": self.city_id,  # No ObjectId conversion, keep as string
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "City":
        return cls(
            city_id=str(data["city_id"]),  # Ensure city_id is string
            name=data["name"]
        )

# Model for states_and_cities collection
class StatesAndCities:
    def __init__(self, name: str, cities: List[City], id: Optional[str] = None):
        self.id = id if id else str(ObjectId())  # id is string
        self.name = name
        self.cities = cities

    def to_dict(self) -> Dict:
        return {
            "_id": self.id,  # Use string id directly, no ObjectId conversion
            "name": self.name,
            "cities": [city.to_dict() for city in self.cities]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "StatesAndCities":
        return cls(
            id=str(data["_id"]),
            name=data["name"],
            cities=[City.from_dict(city) for city in data["cities"]]
        )

    def save(self, collection: Collection) -> None:
        data = self.to_dict()
        # Convert id to ObjectId for MongoDB storage
        data["_id"] = ObjectId(self.id)
        collection.replace_one({"_id": data["_id"]}, data, upsert=True)

    @classmethod
    def find_by_id(cls, state_id: str, collection: Collection) -> Optional["StatesAndCities"]:
        data = collection.find_one({"_id": ObjectId(state_id)})
        return cls.from_dict(data) if data else None

    @classmethod
    def find_all(cls, collection: Collection) -> List["StatesAndCities"]:
        data = collection.find()
        return [cls.from_dict(state) for state in data]

    def delete(self, collection: Collection) -> bool:
        result = collection.delete_one({"_id": ObjectId(self.id)})
        return result.deleted_count > 0

# Model for sectors collection
class Sector:
    def __init__(self, name: str, description: Optional[str] = None, id: Optional[str] = None):
        self.id = id if id else str(ObjectId())
        self.name = name
        self.description = description

    def to_dict(self) -> Dict:
        return {
            "_id": self.id,  # Use string id directly
            "name": self.name,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Sector":
        return cls(
            id=str(data["_id"]),
            name=data["name"],
            description=data.get("description")
        )

    def save(self, collection: Collection) -> None:
        data = self.to_dict()
        data["_id"] = ObjectId(self.id)  # Convert to ObjectId for MongoDB
        collection.replace_one({"_id": data["_id"]}, data, upsert=True)

    @classmethod
    def find_by_id(cls, sector_id: str, collection: Collection) -> Optional["Sector"]:
        data = collection.find_one({"_id": ObjectId(sector_id)})
        return cls.from_dict(data) if data else None

    @classmethod
    def find_all(cls, collection: Collection) -> List["Sector"]:
        data = collection.find()
        return [cls.from_dict(sector) for sector in data]

    def delete(self, collection: Collection) -> bool:
        result = collection.delete_one({"_id": ObjectId(self.id)})
        return result.deleted_count > 0

# Nested classes for scheme_posts, gov_jobs_posts, and digital_services
class Document:
    def __init__(self, name: str, type: Optional[str] = None, description: Optional[str] = None):
        self.name = name
        self.type = type
        self.description = description

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Document":
        return cls(
            name=data["name"],
            type=data.get("type"),
            description=data.get("description")
        )

class Update:
    def __init__(self, date: datetime, note: str):
        self.date = date
        self.note = note

    def to_dict(self) -> Dict:
        return {
            "date": self.date,
            "note": self.note
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Update":
        return cls(
            date=data["date"],
            note=data["note"]
        )

# Model for scheme_posts collection
class SchemePost:
    def __init__(self, title: str, start_date: datetime, end_date: datetime, description: str,
                 required_documents: List[Document], states: List[str], cities: List[str],
                 updates: List[Update], sector_id: str, id: Optional[str] = None):
        self.id = id if id else str(ObjectId())
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.required_documents = required_documents
        self.states = states
        self.cities = cities
        self.updates = updates
        self.sector_id = sector_id

    def to_dict(self) -> Dict:
        return {
            "_id": self.id,  # Use string id
            "title": self.title,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "required_documents": [doc.to_dict() for doc in self.required_documents],
            "states": self.states,
            "cities": self.cities,
            "updates": [update.to_dict() for update in self.updates],
            "sector_id": self.sector_id  # Keep sector_id as string
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "SchemePost":
        return cls(
            id=str(data["_id"]),
            title=data["title"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            required_documents=[Document.from_dict(doc) for doc in data["required_documents"]],
            states=data["states"],
            cities=data["cities"],
            updates=[Update.from_dict(update) for update in data["updates"]],
            sector_id=str(data["sector_id"])
        )

    def save(self, collection: Collection) -> None:
        data = self.to_dict()
        data["_id"] = ObjectId(self.id)  # Convert to ObjectId for MongoDB
        collection.replace_one({"_id": data["_id"]}, data, upsert=True)

    @classmethod
    def find_by_id(cls, post_id: str, collection: Collection) -> Optional["SchemePost"]:
        data = collection.find_one({"_id": ObjectId(post_id)})
        return cls.from_dict(data) if data else None

    @classmethod
    def find_all(cls, collection: Collection) -> List["SchemePost"]:
        data = collection.find()
        return [cls.from_dict(post) for post in data]

    def delete(self, collection: Collection) -> bool:
        result = collection.delete_one({"_id": ObjectId(self.id)})
        return result.deleted_count > 0

# Model for gov_jobs_posts collection
class GovJobPost:
    def __init__(self, title: str, start_date: datetime, end_date: datetime, description: str,
                 required_documents: List[Document], states: List[str], cities: List[str],
                 updates: List[Update], sector_id: str, id: Optional[str] = None):
        self.id = id if id else str(ObjectId())
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.required_documents = required_documents
        self.states = states
        self.cities = cities
        self.updates = updates
        self.sector_id = sector_id

    def to_dict(self) -> Dict:
        return {
            "_id": self.id,  # Use string id
            "title": self.title,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "required_documents": [doc.to_dict() for doc in self.required_documents],
            "states": self.states,
            "cities": self.cities,
            "updates": [update.to_dict() for update in self.updates],
            "sector_id": self.sector_id  # Keep sector_id as string
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "GovJobPost":
        return cls(
            id=str(data["_id"]),
            title=data["title"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            required_documents=[Document.from_dict(doc) for doc in data["required_documents"]],
            states=data["states"],
            cities=data["cities"],
            updates=[Update.from_dict(update) for update in data["updates"]],
            sector_id=str(data["sector_id"])
        )

    def save(self, collection: Collection) -> None:
        data = self.to_dict()
        data["_id"] = ObjectId(self.id)  # Convert to ObjectId for MongoDB
        collection.replace_one({"_id": data["_id"]}, data, upsert=True)

    @classmethod
    def find_by_id(cls, post_id: str, collection: Collection) -> Optional["GovJobPost"]:
        data = collection.find_one({"_id": ObjectId(post_id)})
        return cls.from_dict(data) if data else None

    @classmethod
    def find_all(cls, collection: Collection) -> List["GovJobPost"]:
        data = collection.find()
        return [cls.from_dict(post) for post in data]

    def delete(self, collection: Collection) -> bool:
        result = collection.delete_one({"_id": ObjectId(self.id)})
        return result.deleted_count > 0

# Model for digital_services collection
class DigitalService:
    def __init__(self, title: str, description: str, required_documents: List[Document],
                 updates: List[Update], states: List[str], cities: List[str], id: Optional[str] = None):
        self.id = id if id else str(ObjectId())
        self.title = title
        self.description = description
        self.required_documents = required_documents
        self.updates = updates
        self.states = states
        self.cities = cities

    def to_dict(self) -> Dict:
        return {
            "_id": self.id,  # Use string id
            "title": self.title,
            "description": self.description,
            "required_documents": [doc.to_dict() for doc in self.required_documents],
            "updates": [update.to_dict() for update in self.updates],
            "states": self.states,
            "cities": self.cities
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "DigitalService":
        return cls(
            id=str(data["_id"]),
            title=data["title"],
            description=data["description"],
            required_documents=[Document.from_dict(doc) for doc in data["required_documents"]],
            updates=[Update.from_dict(update) for update in data["updates"]],
            states=data["states"],
            cities=data["cities"]
        )

    def save(self, collection: Collection) -> None:
        data = self.to_dict()
        data["_id"] = ObjectId(self.id)  # Convert to ObjectId for MongoDB
        collection.replace_one({"_id": data["_id"]}, data, upsert=True)

    @classmethod
    def find_by_id(cls, service_id: str, collection: Collection) -> Optional["DigitalService"]:
        data = collection.find_one({"_id": ObjectId(service_id)})
        return cls.from_dict(data) if data else None

    @classmethod
    def find_all(cls, collection: Collection) -> List["DigitalService"]:
        data = collection.find()
        return [cls.from_dict(service) for service in data]

    def delete(self, collection: Collection) -> bool:
        result = collection.delete_one({"_id": ObjectId(self.id)})
        return result.deleted_count > 0