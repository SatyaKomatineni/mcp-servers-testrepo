from models import HealthcareProvider, ProviderType
from datetime import date, timedelta

sample_providers = [
    HealthcareProvider(
        npi="1234567890",
        provider_type=ProviderType.PHYSICIAN,
        first_name="Sarah",
        last_name="Chen",
        email="sarah.chen@healthcare.com",
        phone="415-555-0101",
        addresses=[{
            "street": "1001 Market Street",
            "city": "San Francisco",
            "state": "CA",
            "zip_code": "94103"
        }],
        licenses=[{
            "license_number": "MD123456",
            "state": "CA",
            "issue_date": date(2018, 6, 1),
            "expiration_date": date(2024, 6, 1),
            "license_type": "Medical Doctor"
        }],
        specialties=["Cardiology", "Internal Medicine"],
        insurance_accepted=["Blue Shield", "Kaiser", "Medicare"],
        languages_spoken=["English", "Mandarin"],
        years_of_experience=8,
        rating=4.8
    ),
    
    HealthcareProvider(
        npi="2345678901",
        provider_type=ProviderType.NURSE_PRACTITIONER,
        first_name="Maria",
        last_name="Rodriguez",
        email="maria.rodriguez@healthcare.com",
        phone="212-555-0202",
        addresses=[{
            "street": "200 Park Avenue",
            "city": "New York",
            "state": "NY",
            "zip_code": "10166"
        }],
        licenses=[{
            "license_number": "NP987654",
            "state": "NY",
            "issue_date": date(2020, 1, 15),
            "expiration_date": date(2026, 1, 15),
            "license_type": "Nurse Practitioner"
        }],
        specialties=["Family Medicine", "Primary Care"],
        insurance_accepted=["Aetna", "Cigna", "Medicaid"],
        languages_spoken=["English", "Spanish"],
        years_of_experience=5,
        rating=4.9
    ),
    
    HealthcareProvider(
        npi="3456789012",
        provider_type=ProviderType.PHYSICIAN_ASSISTANT,
        first_name="James",
        last_name="Wilson",
        email="james.wilson@healthcare.com",
        phone="312-555-0303",
        addresses=[{
            "street": "300 Michigan Avenue",
            "city": "Chicago",
            "state": "IL",
            "zip_code": "60601"
        }],
        licenses=[{
            "license_number": "PA456789",
            "state": "IL",
            "issue_date": date(2019, 3, 1),
            "expiration_date": date(2025, 3, 1),
            "license_type": "Physician Assistant"
        }],
        specialties=["Emergency Medicine"],
        insurance_accepted=["Blue Cross", "United Healthcare", "Medicare"],
        years_of_experience=6,
        rating=4.7
    ),
    
    HealthcareProvider(
        npi="4567890123",
        provider_type=ProviderType.SPECIALIST,
        first_name="Aisha",
        last_name="Patel",
        email="aisha.patel@healthcare.com",
        phone="404-555-0404",
        addresses=[{
            "street": "400 Peachtree Street",
            "city": "Atlanta",
            "state": "GA",
            "zip_code": "30303"
        }],
        licenses=[{
            "license_number": "MD789012",
            "state": "GA",
            "issue_date": date(2017, 7, 1),
            "expiration_date": date(2023, 7, 1),
            "license_type": "Medical Doctor"
        }],
        specialties=["Neurology", "Epilepsy"],
        insurance_accepted=["Aetna", "Cigna", "Medicare"],
        languages_spoken=["English", "Hindi", "Gujarati"],
        years_of_experience=10,
        rating=4.9
    ),
    
    HealthcareProvider(
        npi="5678901234",
        provider_type=ProviderType.HOSPITAL,
        first_name="Memorial",
        last_name="Medical Center",
        email="info@memorialmedical.com",
        phone="713-555-0505",
        addresses=[{
            "street": "500 Main Street",
            "city": "Houston",
            "state": "TX",
            "zip_code": "77002"
        }],
        licenses=[{
            "license_number": "HOSP123456",
            "state": "TX",
            "issue_date": date(2015, 1, 1),
            "expiration_date": date(2025, 1, 1),
            "license_type": "Hospital"
        }],
        specialties=["Emergency Care", "Surgery", "Maternity", "Cardiology"],
        insurance_accepted=["Blue Cross", "Aetna", "Medicare", "Medicaid"],
        hospital_affiliations=["Texas Medical Center"],
        rating=4.6
    ),
    
    HealthcareProvider(
        npi="6789012345",
        provider_type=ProviderType.PHYSICIAN,
        first_name="David",
        last_name="Kim",
        email="david.kim@healthcare.com",
        phone="206-555-0606",
        addresses=[{
            "street": "600 Pine Street",
            "city": "Seattle",
            "state": "WA",
            "zip_code": "98101"
        }],
        licenses=[{
            "license_number": "MD345678",
            "state": "WA",
            "issue_date": date(2016, 8, 1),
            "expiration_date": date(2024, 8, 1),
            "license_type": "Medical Doctor"
        }],
        specialties=["Orthopedics", "Sports Medicine"],
        insurance_accepted=["Premera", "Regence", "Medicare"],
        languages_spoken=["English", "Korean"],
        years_of_experience=9,
        rating=4.8
    ),
    
    HealthcareProvider(
        npi="7890123456",
        provider_type=ProviderType.CLINIC,
        first_name="Community",
        last_name="Health Center",
        email="info@communityhealth.org",
        phone="305-555-0707",
        addresses=[{
            "street": "700 Biscayne Boulevard",
            "city": "Miami",
            "state": "FL",
            "zip_code": "33132"
        }],
        licenses=[{
            "license_number": "CLIN789012",
            "state": "FL",
            "issue_date": date(2018, 1, 1),
            "expiration_date": date(2024, 1, 1),
            "license_type": "Clinic"
        }],
        specialties=["Primary Care", "Pediatrics", "Women's Health"],
        insurance_accepted=["Florida Blue", "Medicaid", "Medicare"],
        languages_spoken=["English", "Spanish", "Creole"],
        rating=4.5
    ),
    
    HealthcareProvider(
        npi="8901234567",
        provider_type=ProviderType.PHYSICIAN,
        first_name="Emily",
        last_name="Johnson",
        email="emily.johnson@healthcare.com",
        phone="503-555-0808",
        addresses=[{
            "street": "800 SW Broadway",
            "city": "Portland",
            "state": "OR",
            "zip_code": "97205"
        }],
        licenses=[{
            "license_number": "MD567890",
            "state": "OR",
            "issue_date": date(2019, 5, 1),
            "expiration_date": date(2025, 5, 1),
            "license_type": "Medical Doctor"
        }],
        specialties=["Dermatology", "Cosmetic Dermatology"],
        insurance_accepted=["Providence", "Kaiser", "Medicare"],
        languages_spoken=["English", "French"],
        years_of_experience=7,
        rating=4.9
    ),
    
    HealthcareProvider(
        npi="9012345678",
        provider_type=ProviderType.LABORATORY,
        first_name="Advanced",
        last_name="Diagnostics Lab",
        email="info@advancedlab.com",
        phone="602-555-0909",
        addresses=[{
            "street": "900 Central Avenue",
            "city": "Phoenix",
            "state": "AZ",
            "zip_code": "85004"
        }],
        licenses=[{
            "license_number": "LAB123789",
            "state": "AZ",
            "issue_date": date(2017, 1, 1),
            "expiration_date": date(2025, 1, 1),
            "license_type": "Clinical Laboratory"
        }],
        specialties=["Blood Testing", "Genetic Testing", "COVID-19 Testing"],
        insurance_accepted=["Blue Cross", "Aetna", "Medicare"],
        rating=4.7
    ),
    
    HealthcareProvider(
        npi="0123456789",
        provider_type=ProviderType.PHARMACY,
        first_name="Wellness",
        last_name="Pharmacy",
        email="info@wellnesspharmacy.com",
        phone="303-555-1010",
        addresses=[{
            "street": "1000 16th Street",
            "city": "Denver",
            "state": "CO",
            "zip_code": "80202"
        }],
        licenses=[{
            "license_number": "PHARM456789",
            "state": "CO",
            "issue_date": date(2018, 1, 1),
            "expiration_date": date(2024, 1, 1),
            "license_type": "Pharmacy"
        }],
        specialties=["Prescription Medications", "Compounding", "Vaccinations"],
        insurance_accepted=["Anthem", "Cigna", "Medicare Part D"],
        languages_spoken=["English", "Spanish"],
        rating=4.8
    )
] 