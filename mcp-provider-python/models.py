from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date
from enum import Enum

class ProviderType(str, Enum):
    PHYSICIAN = "physician"
    NURSE_PRACTITIONER = "nurse_practitioner"
    PHYSICIAN_ASSISTANT = "physician_assistant"
    SPECIALIST = "specialist"
    HOSPITAL = "hospital"
    CLINIC = "clinic"
    LABORATORY = "laboratory"
    PHARMACY = "pharmacy"

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "USA"

class License(BaseModel):
    license_number: str
    state: str
    issue_date: date
    expiration_date: date
    license_type: str

class HealthcareProvider(BaseModel):
    npi: str = Field(..., description="National Provider Identifier")
    provider_type: ProviderType
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    addresses: List[Address]
    licenses: List[License]
    specialties: List[str]
    accepting_new_patients: bool = True
    languages_spoken: List[str] = ["English"]
    insurance_accepted: List[str]
    hospital_affiliations: Optional[List[str]] = None
    education: List[dict] = Field(default_factory=list, description="List of educational qualifications")
    certifications: Optional[List[str]] = None
    years_of_experience: Optional[int] = None
    rating: Optional[float] = Field(None, ge=0, le=5, description="Provider rating from 0 to 5")
    is_active: bool = True
    created_at: date = Field(default_factory=date.today)
    updated_at: date = Field(default_factory=date.today)

    class Config:
        json_schema_extra = {
            "example": {
                "npi": "1234567890",
                "provider_type": "physician",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@healthcare.com",
                "phone": "555-0123",
                "addresses": [{
                    "street": "123 Medical Center Dr",
                    "city": "Boston",
                    "state": "MA",
                    "zip_code": "02108"
                }],
                "licenses": [{
                    "license_number": "MD123456",
                    "state": "MA",
                    "issue_date": "2020-01-01",
                    "expiration_date": "2025-01-01",
                    "license_type": "Medical Doctor"
                }],
                "specialties": ["Internal Medicine", "Primary Care"],
                "insurance_accepted": ["Blue Cross", "Aetna", "Medicare"],
                "languages_spoken": ["English", "Spanish"]
            }
        } 