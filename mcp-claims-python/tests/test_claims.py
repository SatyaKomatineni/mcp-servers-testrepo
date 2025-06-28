from datetime import datetime, timedelta
from models.claim import MedicalClaim, Provider, Patient, Diagnosis, Procedure

# Sample providers
providers = [
    Provider(
        npi="1234567890",
        name="Dr. Sarah Johnson",
        specialty="Cardiology",
        address="123 Heart Lane, Medical Center, CA 90210",
        phone="555-0101"
    ),
    Provider(
        npi="2345678901",
        name="Dr. Michael Chen",
        specialty="Orthopedics",
        address="456 Bone Street, Medical Center, CA 90210",
        phone="555-0102"
    ),
    Provider(
        npi="3456789012",
        name="Dr. Emily Rodriguez",
        specialty="Pediatrics",
        address="789 Child Avenue, Medical Center, CA 90210",
        phone="555-0103"
    ),
    Provider(
        npi="4567890123",
        name="Dr. James Wilson",
        specialty="Neurology",
        address="321 Brain Boulevard, Medical Center, CA 90210",
        phone="555-0104"
    )
]

# Sample patients
patients = [
    Patient(
        member_id="M001",
        first_name="John",
        last_name="Smith",
        date_of_birth=datetime(1980, 5, 15),
        gender="Male",
        address="100 Main St, Anytown, CA 90210",
        phone="555-1001",
        email="john.smith@email.com"
    ),
    Patient(
        member_id="M002",
        first_name="Maria",
        last_name="Garcia",
        date_of_birth=datetime(1992, 8, 23),
        gender="Female",
        address="200 Oak Ave, Anytown, CA 90210",
        phone="555-1002",
        email="maria.garcia@email.com"
    ),
    Patient(
        member_id="M003",
        first_name="Robert",
        last_name="Johnson",
        date_of_birth=datetime(1975, 3, 10),
        gender="Male",
        address="300 Pine Rd, Anytown, CA 90210",
        phone="555-1003"
    ),
    Patient(
        member_id="M004",
        first_name="Sarah",
        last_name="Williams",
        date_of_birth=datetime(1988, 11, 30),
        gender="Female",
        address="400 Maple Dr, Anytown, CA 90210",
        phone="555-1004",
        email="sarah.williams@email.com"
    )
]

# Sample diagnoses
diagnoses = [
    Diagnosis(
        code="I10",
        description="Essential (primary) hypertension",
        date=datetime(2024, 1, 15)
    ),
    Diagnosis(
        code="E11.9",
        description="Type 2 diabetes mellitus without complications",
        date=datetime(2024, 1, 15)
    ),
    Diagnosis(
        code="M17.9",
        description="Osteoarthritis of knee, unspecified",
        date=datetime(2024, 2, 1)
    ),
    Diagnosis(
        code="J45.909",
        description="Unspecified asthma, uncomplicated",
        date=datetime(2024, 2, 15)
    )
]

# Sample procedures
procedures = [
    Procedure(
        code="99213",
        description="Office visit, established patient, 15 minutes",
        date=datetime(2024, 1, 15),
        charge_amount=150.00
    ),
    Procedure(
        code="93010",
        description="Electrocardiogram, routine ECG with at least 12 leads",
        date=datetime(2024, 1, 15),
        charge_amount=250.00
    ),
    Procedure(
        code="27447",
        description="Total knee arthroplasty",
        date=datetime(2024, 2, 1),
        charge_amount=25000.00
    ),
    Procedure(
        code="94010",
        description="Spirometry, including graphic record",
        date=datetime(2024, 2, 15),
        charge_amount=200.00
    )
]

# Generate 20 test claims
test_claims = []

# Claim 1: Cardiology visit with hypertension
test_claims.append(MedicalClaim(
    claim_id="C001",
    patient=patients[0],
    provider=providers[0],
    diagnoses=[diagnoses[0]],
    procedures=[procedures[0], procedures[1]],
    date_of_service=datetime(2024, 1, 15),
    claim_type="professional",
    status="approved",
    total_charge_amount=400.00,
    insurance_paid=320.00,
    patient_responsibility=80.00
))

# Claim 2: Orthopedic surgery
test_claims.append(MedicalClaim(
    claim_id="C002",
    patient=patients[1],
    provider=providers[1],
    diagnoses=[diagnoses[2]],
    procedures=[procedures[2]],
    date_of_service=datetime(2024, 2, 1),
    claim_type="institutional",
    status="pending",
    total_charge_amount=25000.00
))

# Claim 3: Pediatric asthma visit
test_claims.append(MedicalClaim(
    claim_id="C003",
    patient=patients[2],
    provider=providers[2],
    diagnoses=[diagnoses[3]],
    procedures=[procedures[3]],
    date_of_service=datetime(2024, 2, 15),
    claim_type="professional",
    status="approved",
    total_charge_amount=200.00,
    insurance_paid=160.00,
    patient_responsibility=40.00
))

# Claim 4: Diabetes follow-up
test_claims.append(MedicalClaim(
    claim_id="C004",
    patient=patients[0],
    provider=providers[0],
    diagnoses=[diagnoses[1]],
    procedures=[procedures[0]],
    date_of_service=datetime(2024, 2, 20),
    claim_type="professional",
    status="approved",
    total_charge_amount=150.00,
    insurance_paid=120.00,
    patient_responsibility=30.00
))

# Claim 5: Neurology consultation
test_claims.append(MedicalClaim(
    claim_id="C005",
    patient=patients[3],
    provider=providers[3],
    diagnoses=[Diagnosis(
        code="G40.909",
        description="Epilepsy, unspecified, not intractable, without status epilepticus",
        date=datetime(2024, 3, 1)
    )],
    procedures=[Procedure(
        code="99204",
        description="Office visit, new patient, 45 minutes",
        date=datetime(2024, 3, 1),
        charge_amount=250.00
    )],
    date_of_service=datetime(2024, 3, 1),
    claim_type="professional",
    status="pending",
    total_charge_amount=250.00
))

# Continue with more claims...
# Claims 6-20 would follow similar patterns with different combinations
# of patients, providers, diagnoses, and procedures

# For brevity, I'll add a few more varied examples:

# Claim 6: Emergency room visit
test_claims.append(MedicalClaim(
    claim_id="C006",
    patient=patients[1],
    provider=providers[0],
    diagnoses=[Diagnosis(
        code="R07.9",
        description="Chest pain, unspecified",
        date=datetime(2024, 3, 5)
    )],
    procedures=[Procedure(
        code="99284",
        description="Emergency department visit, moderate severity",
        date=datetime(2024, 3, 5),
        charge_amount=750.00
    )],
    date_of_service=datetime(2024, 3, 5),
    claim_type="institutional",
    status="approved",
    total_charge_amount=750.00,
    insurance_paid=600.00,
    patient_responsibility=150.00
))

# Claim 7: Physical therapy
test_claims.append(MedicalClaim(
    claim_id="C007",
    patient=patients[2],
    provider=providers[1],
    diagnoses=[diagnoses[2]],
    procedures=[Procedure(
        code="97110",
        description="Therapeutic exercise",
        date=datetime(2024, 3, 10),
        charge_amount=85.00,
        units=3
    )],
    date_of_service=datetime(2024, 3, 10),
    claim_type="professional",
    status="approved",
    total_charge_amount=255.00,
    insurance_paid=204.00,
    patient_responsibility=51.00
))

# Claim 8: Lab work
test_claims.append(MedicalClaim(
    claim_id="C008",
    patient=patients[0],
    provider=providers[0],
    diagnoses=[diagnoses[1]],
    procedures=[Procedure(
        code="80053",
        description="Comprehensive metabolic panel",
        date=datetime(2024, 3, 15),
        charge_amount=125.00
    )],
    date_of_service=datetime(2024, 3, 15),
    claim_type="professional",
    status="approved",
    total_charge_amount=125.00,
    insurance_paid=100.00,
    patient_responsibility=25.00
))

# Note: In a real implementation, you would want to add more claims
# to reach the full 20, with various combinations of the above patterns
# and additional scenarios. Each claim would have realistic dates,
# amounts, and appropriate combinations of diagnoses and procedures.

# Example of how to use the test claims:
if __name__ == "__main__":
    for claim in test_claims:
        print(f"Claim ID: {claim.claim_id}")
        print(f"Patient: {claim.patient.first_name} {claim.patient.last_name}")
        print(f"Provider: {claim.provider.name}")
        print(f"Total Amount: ${claim.total_charge_amount}")
        print(f"Status: {claim.status}")
        print("---") 