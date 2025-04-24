from app.database import db

def get_states_and_cities_collection():
    return db["states_and_cities"]

def get_sectors_collection():
    return db["sectors"]

def get_scheme_posts_collection():
    return db["scheme_posts"]

def get_gov_jobs_posts_collection():
    return db["gov_jobs_posts"]

def get_digital_services_collection():
    return db["digital_services"]