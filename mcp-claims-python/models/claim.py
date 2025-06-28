from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr

class Provider(BaseModel):
    """Healthcare provider information"""
    npi: str = Field(..., description="National Provider Identifier")
    name: str = Field(..., description="Provider's full name")
    specialty: str = Field(..., description="Provider's medical specialty")
    address: str = Field(..., description="Provider's address")
    phone: str = Field(..., description="Provider's contact phone number")

class Patient(BaseModel):
    """Patient information"""
    member_id: str = Field(..., description="Patient's member/insurance ID")
    first_name: str = Field(..., description="Patient's first name")
    last_name: str = Field(..., description="Patient's last name")
    date_of_birth: datetime = Field(..., description="Patient's date of birth")
    gender: str = Field(..., description="Patient's gender")
    address: str = Field(..., description="Patient's address")
    phone: str = Field(..., description="Patient's contact phone number")
    email: Optional[EmailStr] = Field(None, description="Patient's email address")

class Diagnosis(BaseModel):
    """Diagnosis information"""
    code: str = Field(..., description="ICD-10 diagnosis code")
    description: str = Field(..., description="Diagnosis description")
    date: datetime = Field(..., description="Date of diagnosis")

class Procedure(BaseModel):
    """Medical procedure information"""
    code: str = Field(..., description="CPT/HCPCS procedure code")
    description: str = Field(..., description="Procedure description")
    date: datetime = Field(..., description="Date of procedure")
    units: int = Field(1, description="Number of units/procedures performed")
    charge_amount: float = Field(..., description="Amount charged for the procedure")

class MedicalClaim(BaseModel):
    """Medical claim information"""
    claim_id: str = Field(..., description="Unique claim identifier")
    patient: Patient = Field(..., description="Patient information")
    provider: Provider = Field(..., description="Provider information")
    diagnoses: List[Diagnosis] = Field(..., description="List of diagnoses")
    procedures: List[Procedure] = Field(..., description="List of procedures")
    date_of_service: datetime = Field(..., description="Date of service")
    claim_type: str = Field(..., description="Type of claim (e.g., professional, institutional)")
    status: str = Field(..., description="Claim status (e.g., pending, approved, denied)")
    total_charge_amount: float = Field(..., description="Total amount charged")
    insurance_paid: Optional[float] = Field(None, description="Amount paid by insurance")
    patient_responsibility: Optional[float] = Field(None, description="Amount patient is responsible for")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="When the claim was created")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="When the claim was last updated")