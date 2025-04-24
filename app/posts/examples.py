# app/posts/examples.py

# Examples for StatesAndCities
states_and_cities_examples = {
    "example1": {
        "summary": "Western State",
        "description": "A state in Western India with major cities",
        "value": {
            "name": "Maharashtra",
            "cities": [
                {"city_id": "60d5f7c9b1d5e9b4a8f9a2b3", "name": "Mumbai"},
                {"city_id": "60d5f7c9b1d5e9b4a8f9a2b4", "name": "Pune"}
            ]
        }
    },
    "example2": {
        "summary": "Southern State",
        "description": "A state in Southern India with tech hubs",
        "value": {
            "name": "Karnataka",
            "cities": [
                {"city_id": "60d5f7c9b1d5e9b4a8f9a2b5", "name": "Bangalore"},
                {"city_id": "60d5f7c9b1d5e9b4a8f9a2b6", "name": "Mysore"}
            ]
        }
    }
}

# Examples for Sectors
sector_examples = {
    "example1": {
        "summary": "Education Sector",
        "description": "Sector focused on educational initiatives",
        "value": {
            "name": "Education",
            "description": "Sector for educational services and schemes"
        }
    },
    "example2": {
        "summary": "Healthcare Sector",
        "description": "Sector focused on healthcare services",
        "value": {
            "name": "Healthcare",
            "description": "Sector for healthcare services and programs"
        }
    }
}

# Examples for SchemePosts
scheme_post_examples = {
    "example1": {
        "summary": "Scholarship Scheme",
        "description": "A scholarship program for students",
        "value": {
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
    },
    "example2": {
        "summary": "Agricultural Subsidy",
        "description": "A subsidy program for farmers",
        "value": {
            "title": "Agricultural Subsidy 2025",
            "start_date": "2025-03-01T00:00:00",
            "end_date": "2025-11-30T23:59:59",
            "description": "A subsidy program for farmers to support crop production",
            "required_documents": [
                {"name": "Land Ownership Document", "type": "Proof", "description": "Proof of land ownership"}
            ],
            "states": ["Punjab", "Haryana"],
            "cities": ["Chandigarh", "Ambala"],
            "updates": [
                {"date": "2025-03-15T00:00:00", "note": "Subsidy application started"}
            ],
            "sector_id": "60d5f7c9b1d5e9b4a8f9a2b7"
        }
    }
}

# Examples for GovJobPosts
gov_job_post_examples = {
    "example1": {
        "summary": "Teacher Recruitment",
        "description": "Recruitment for government school teachers",
        "value": {
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
    },
    "example2": {
        "summary": "Police Recruitment",
        "description": "Recruitment for state police force",
        "value": {
            "title": "State Police Recruitment 2025",
            "start_date": "2025-04-01T00:00:00",
            "end_date": "2025-06-30T23:59:59",
            "description": "Recruitment for state police officers",
            "required_documents": [
                {"name": "Fitness Certificate", "type": "Medical", "description": "Proof of physical fitness"}
            ],
            "states": ["Uttar Pradesh", "Bihar"],
            "cities": ["Lucknow", "Patna"],
            "updates": [
                {"date": "2025-04-10T00:00:00", "note": "Written test scheduled"}
            ],
            "sector_id": "60d5f7c9b1d5e9b4a8f9a2b8"
        }
    }
}

# Examples for DigitalServices
digital_service_examples = {
    "example1": {
        "summary": "Tax Filing Service",
        "description": "Digital service for filing taxes online",
        "value": {
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
    },
    "example2": {
        "summary": "E-Governance Portal",
        "description": "Portal for accessing government services online",
        "value": {
            "title": "E-Governance Portal 2025",
            "description": "Portal for accessing government services online",
            "required_documents": [
                {"name": "Voter ID", "type": "ID", "description": "Proof of citizenship"}
            ],
            "updates": [
                {"date": "2025-05-01T00:00:00", "note": "Portal updated with new services"}
            ],
            "states": ["Delhi", "Haryana"],
            "cities": ["New Delhi", "Gurgaon"]
        }
    }
}