from fastapi import APIRouter, HTTPException, status, Depends, Body
from pymongo.collection import Collection
from typing import List
from .schema import (StatesAndCitiesCreate, StatesAndCitiesResponse, StatesAndCitiesUpdate,
                     SectorCreate, SectorResponse, SectorUpdate,
                     SchemePostCreate, SchemePostResponse, SchemePostUpdate,
                     GovJobPostCreate, GovJobPostResponse, GovJobPostUpdate,
                     DigitalServiceCreate, DigitalServiceResponse, DigitalServiceUpdate)
from .model import (StatesAndCities, City, Sector, SchemePost, Document, Update, GovJobPost, DigitalService)
from app.dependencies import (get_states_and_cities_collection, get_sectors_collection,
                              get_scheme_posts_collection, get_gov_jobs_posts_collection,
                              get_digital_services_collection)
from .examples import (states_and_cities_examples, sector_examples, scheme_post_examples,
                       gov_job_post_examples, digital_service_examples)

router = APIRouter()

# CRUD for states_and_cities
@router.post(
    "/states-and-cities/",
    response_model=StatesAndCitiesResponse,
    status_code=status.HTTP_201_CREATED
)
def create_states_and_cities(
    state: StatesAndCitiesCreate = Body(openapi_examples=states_and_cities_examples),  # Corrected to examples
    collection: Collection = Depends(get_states_and_cities_collection)
):
    cities = [City(**city.dict()) for city in state.cities]
    state_obj = StatesAndCities(name=state.name, cities=cities)
    state_obj.save(collection)
    return state_obj.to_dict()

@router.get("/states-and-cities/{state_id}", response_model=StatesAndCitiesResponse)
def get_states_and_cities(state_id: str, collection: Collection = Depends(get_states_and_cities_collection)):
    state = StatesAndCities.find_by_id(state_id, collection)
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
    return state.to_dict()

@router.get("/states-and-cities/", response_model=List[StatesAndCitiesResponse])
def list_states_and_cities(collection: Collection = Depends(get_states_and_cities_collection)):
    states = StatesAndCities.find_all(collection)
    return [state.to_dict() for state in states]

@router.put("/states-and-cities/{state_id}", response_model=StatesAndCitiesResponse)
def update_states_and_cities(state_id: str, state_update: StatesAndCitiesUpdate,
                            collection: Collection = Depends(get_states_and_cities_collection)):
    state = StatesAndCities.find_by_id(state_id, collection)
    if not state:
        raise HTTPException(status_code=404, detail="State not found")

    update_data = state_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")

    if "cities" in update_data:
        update_data["cities"] = [City(**city) for city in update_data["cities"]]

    for key, value in update_data.items():
        setattr(state, key, value)
    state.save(collection)
    return state.to_dict()

@router.delete("/states-and-cities/{state_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_states_and_cities(state_id: str, collection: Collection = Depends(get_states_and_cities_collection)):
    state = StatesAndCities.find_by_id(state_id, collection)
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
    state.delete(collection)
    return None

# CRUD for sectors
@router.post(
    "/sectors/",
    response_model=SectorResponse,
    status_code=status.HTTP_201_CREATED
)
def create_sector(
    sector: SectorCreate = Body(openapi_examples=sector_examples),  # Corrected to examples
    collection: Collection = Depends(get_sectors_collection)
):
    sector_obj = Sector(name=sector.name, description=sector.description)
    sector_obj.save(collection)
    return sector_obj.to_dict()

@router.get("/sectors/{sector_id}", response_model=SectorResponse)
def get_sector(sector_id: str, collection: Collection = Depends(get_sectors_collection)):
    sector = Sector.find_by_id(sector_id, collection)
    if not sector:
        raise HTTPException(status_code=404, detail="Sector not found")
    return sector.to_dict()

@router.get("/sectors/", response_model=List[SectorResponse])
def list_sectors(collection: Collection = Depends(get_sectors_collection)):
    sectors = Sector.find_all(collection)
    return [sector.to_dict() for sector in sectors]

@router.put("/sectors/{sector_id}", response_model=SectorResponse)
def update_sector(sector_id: str, sector_update: SectorUpdate,
                  collection: Collection = Depends(get_sectors_collection)):
    sector = Sector.find_by_id(sector_id, collection)
    if not sector:
        raise HTTPException(status_code=404, detail="Sector not found")

    update_data = sector_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")

    for key, value in update_data.items():
        setattr(sector, key, value)
    sector.save(collection)
    return sector.to_dict()

@router.delete("/sectors/{sector_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sector(sector_id: str, collection: Collection = Depends(get_sectors_collection)):
    sector = Sector.find_by_id(sector_id, collection)
    if not sector:
        raise HTTPException(status_code=404, detail="Sector not found")
    sector.delete(collection)
    return None

# CRUD for scheme_posts
@router.post(
    "/scheme-posts/",
    response_model=SchemePostResponse,
    status_code=status.HTTP_201_CREATED
)
def create_scheme_post(
    post: SchemePostCreate = Body(openapi_examples=scheme_post_examples),  # Corrected to examples
    collection: Collection = Depends(get_scheme_posts_collection)
):
    required_documents = [Document(**doc.dict()) for doc in post.required_documents]
    updates = [Update(**update.dict()) for update in post.updates]
    post_obj = SchemePost(
        title=post.title,
        start_date=post.start_date,
        end_date=post.end_date,
        description=post.description,
        required_documents=required_documents,
        states=post.states,
        cities=post.cities,
        updates=updates,
        sector_id=post.sector_id
    )
    post_obj.save(collection)
    return post_obj.to_dict()

@router.get("/scheme-posts/{post_id}", response_model=SchemePostResponse)
def get_scheme_post(post_id: str, collection: Collection = Depends(get_scheme_posts_collection)):
    post = SchemePost.find_by_id(post_id, collection)
    if not post:
        raise HTTPException(status_code=404, detail="Scheme post not found")
    return post.to_dict()

@router.get("/scheme-posts/", response_model=List[SchemePostResponse])
def list_scheme_posts(collection: Collection = Depends(get_scheme_posts_collection)):
    posts = SchemePost.find_all(collection)
    return [post.to_dict() for post in posts]

@router.put("/scheme-posts/{post_id}", response_model=SchemePostResponse)
def update_scheme_post(post_id: str, post_update: SchemePostUpdate,
                      collection: Collection = Depends(get_scheme_posts_collection)):
    post = SchemePost.find_by_id(post_id, collection)
    if not post:
        raise HTTPException(status_code=404, detail="Scheme post not found")

    update_data = post_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")

    if "required_documents" in update_data:
        update_data["required_documents"] = [Document(**doc) for doc in update_data["required_documents"]]
    if "updates" in update_data:
        update_data["updates"] = [Update(**update) for update in update_data["updates"]]

    for key, value in update_data.items():
        setattr(post, key, value)
    post.save(collection)
    return post.to_dict()

@router.delete("/scheme-posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scheme_post(post_id: str, collection: Collection = Depends(get_scheme_posts_collection)):
    post = SchemePost.find_by_id(post_id, collection)
    if not post:
        raise HTTPException(status_code=404, detail="Scheme post not found")
    post.delete(collection)
    return None

# CRUD for gov_jobs_posts
@router.post(
    "/gov-jobs-posts/",
    response_model=GovJobPostResponse,
    status_code=status.HTTP_201_CREATED
)
def create_gov_job_post(
    post: GovJobPostCreate = Body(openapi_examples=gov_job_post_examples),  # Corrected to examples
    collection: Collection = Depends(get_gov_jobs_posts_collection)
):
    required_documents = [Document(**doc.dict()) for doc in post.required_documents]
    updates = [Update(**update.dict()) for update in post.updates]
    post_obj = GovJobPost(
        title=post.title,
        start_date=post.start_date,
        end_date=post.end_date,
        description=post.description,
        required_documents=required_documents,
        states=post.states,
        cities=post.cities,
        updates=updates,
        sector_id=post.sector_id
    )
    post_obj.save(collection)
    return post_obj.to_dict()

@router.get("/gov-jobs-posts/{post_id}", response_model=GovJobPostResponse)
def get_gov_job_post(post_id: str, collection: Collection = Depends(get_gov_jobs_posts_collection)):
    post = GovJobPost.find_by_id(post_id, collection)
    if not post:
        raise HTTPException(status_code=404, detail="Government job post not found")
    return post.to_dict()

@router.get("/gov-jobs-posts/", response_model=List[GovJobPostResponse])
def list_gov_job_posts(collection: Collection = Depends(get_gov_jobs_posts_collection)):
    posts = GovJobPost.find_all(collection)
    return [post.to_dict() for post in posts]

@router.put("/gov-jobs-posts/{post_id}", response_model=GovJobPostResponse)
def update_gov_job_post(post_id: str, post_update: GovJobPostUpdate,
                       collection: Collection = Depends(get_gov_jobs_posts_collection)):
    post = GovJobPost.find_by_id(post_id, collection)
    if not post:
        raise HTTPException(status_code=404, detail="Government job post not found")

    update_data = post_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")

    if "required_documents" in update_data:
        update_data["required_documents"] = [Document(**doc) for doc in update_data["required_documents"]]
    if "updates" in update_data:
        update_data["updates"] = [Update(**update) for update in update_data["updates"]]

    for key, value in update_data.items():
        setattr(post, key, value)
    post.save(collection)
    return post.to_dict()

@router.delete("/gov-jobs-posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gov_job_post(post_id: str, collection: Collection = Depends(get_gov_jobs_posts_collection)):
    post = GovJobPost.find_by_id(post_id, collection)
    if not post:
        raise HTTPException(status_code=404, detail="Government job post not found")
    post.delete(collection)
    return None

# CRUD for digital_services
@router.post(
    "/digital-services/",
    response_model=DigitalServiceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_digital_service(
    service: DigitalServiceCreate = Body(openapi_examples=digital_service_examples),  # Corrected to examples
    collection: Collection = Depends(get_digital_services_collection)
):
    required_documents = [Document(**doc.dict()) for doc in service.required_documents]
    updates = [Update(**update.dict()) for update in service.updates]
    service_obj = DigitalService(
        title=service.title,
        description=service.description,
        required_documents=required_documents,
        updates=updates,
        states=service.states,
        cities=service.cities
    )
    service_obj.save(collection)
    return service_obj.to_dict()

@router.get("/digital-services/{service_id}", response_model=DigitalServiceResponse)
def get_digital_service(service_id: str, collection: Collection = Depends(get_digital_services_collection)):
    service = DigitalService.find_by_id(service_id, collection)
    if not service:
        raise HTTPException(status_code=404, detail="Digital service not found")
    return service.to_dict()

@router.get("/digital-services/", response_model=List[DigitalServiceResponse])
def list_digital_services(collection: Collection = Depends(get_digital_services_collection)):
    services = DigitalService.find_all(collection)
    return [service.to_dict() for service in services]

@router.put("/digital-services/{service_id}", response_model=DigitalServiceResponse)
def update_digital_service(service_id: str, service_update: DigitalServiceUpdate,
                          collection: Collection = Depends(get_digital_services_collection)):
    service = DigitalService.find_by_id(service_id, collection)
    if not service:
        raise HTTPException(status_code=404, detail="Digital service not found")

    update_data = service_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")

    if "required_documents" in update_data:
        update_data["required_documents"] = [Document(**doc) for doc in update_data["required_documents"]]
    if "updates" in update_data:
        update_data["updates"] = [Update(**update) for update in update_data["updates"]]

    for key, value in update_data.items():
        setattr(service, key, value)
    service.save(collection)
    return service.to_dict()

@router.delete("/digital-services/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_digital_service(service_id: str, collection: Collection = Depends(get_digital_services_collection)):
    service = DigitalService.find_by_id(service_id, collection)
    if not service:
        raise HTTPException(status_code=404, detail="Digital service not found")
    service.delete(collection)
    return None