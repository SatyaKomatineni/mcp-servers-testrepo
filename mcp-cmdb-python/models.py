from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, IPvAnyAddress

class System(BaseModel):
    """Represents a system in the Configuration Management Database."""
    
    # Basic Information
    id: str = Field(..., description="Unique identifier for the system")
    name: str = Field(..., description="Display name of the system")
    description: Optional[str] = Field(None, description="Detailed description of the system")
    
    # System Details
    hostname: str = Field(..., description="Hostname of the system")
    fqdn: Optional[str] = Field(None, description="Fully qualified domain name")
    ip_addresses: List[IPvAnyAddress] = Field(default_factory=list, description="List of IP addresses")
    os_type: str = Field(..., description="Operating system type (e.g., Linux, Windows, macOS)")
    os_version: str = Field(..., description="Operating system version")
    
    # Hardware Information
    cpu_cores: Optional[int] = Field(None, description="Number of CPU cores")
    memory_gb: Optional[float] = Field(None, description="Total memory in gigabytes")
    storage_gb: Optional[float] = Field(None, description="Total storage in gigabytes")
    
    # Status and Environment
    status: str = Field(default="active", description="System status (active, inactive, maintenance, etc.)")
    environment: str = Field(..., description="Environment (production, staging, development, etc.)")
    location: Optional[str] = Field(None, description="Physical or logical location")
    
    # Ownership and Management
    owner: Optional[str] = Field(None, description="System owner or responsible team")
    department: Optional[str] = Field(None, description="Owning department")
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    last_boot_time: Optional[datetime] = Field(None, description="Last system boot time")
    
    # Additional Metadata
    tags: List[str] = Field(default_factory=list, description="System tags for categorization")
    custom_fields: dict = Field(default_factory=dict, description="Additional custom fields")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "sys-001",
                "name": "Web Server 01",
                "description": "Primary web server for customer portal",
                "hostname": "web01",
                "fqdn": "web01.example.com",
                "ip_addresses": ["192.168.1.100"],
                "os_type": "Linux",
                "os_version": "Ubuntu 22.04 LTS",
                "cpu_cores": 4,
                "memory_gb": 16.0,
                "storage_gb": 500.0,
                "status": "active",
                "environment": "production",
                "location": "US-East-1",
                "owner": "Web Team",
                "department": "Engineering",
                "tags": ["web", "production", "critical"],
                "custom_fields": {
                    "maintenance_window": "Sunday 02:00-04:00 UTC",
                    "backup_schedule": "Daily 01:00 UTC"
                }
            }
        } 