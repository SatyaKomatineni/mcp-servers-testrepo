from datetime import datetime, timedelta
from models import System

test_systems = [
    # Production Web Servers
    System(
        id="web-prod-01",
        name="Web Server Production 01",
        description="Primary web server for customer portal",
        hostname="web-prod-01",
        fqdn="web-prod-01.example.com",
        ip_addresses=["10.0.1.10", "10.0.1.11"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=500.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Web Team",
        department="Engineering",
        tags=["web", "production", "critical"],
        custom_fields={"maintenance_window": "Sunday 02:00-04:00 UTC"}
    ),
    
    # Database Servers
    System(
        id="db-prod-01",
        name="Database Server Production 01",
        description="Primary PostgreSQL database server",
        hostname="db-prod-01",
        fqdn="db-prod-01.example.com",
        ip_addresses=["10.0.2.10"],
        os_type="Linux",
        os_version="RHEL 8.6",
        cpu_cores=16,
        memory_gb=64.0,
        storage_gb=2000.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Database Team",
        department="Engineering",
        tags=["database", "production", "critical"],
        custom_fields={"backup_schedule": "Daily 01:00 UTC"}
    ),
    
    # Staging Environment
    System(
        id="web-staging-01",
        name="Web Server Staging 01",
        description="Staging web server for testing",
        hostname="web-staging-01",
        fqdn="web-staging-01.example.com",
        ip_addresses=["10.1.1.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=4,
        memory_gb=16.0,
        storage_gb=250.0,
        status="active",
        environment="staging",
        location="US-East-1",
        owner="Web Team",
        department="Engineering",
        tags=["web", "staging"]
    ),
    
    # Development Environment
    System(
        id="dev-01",
        name="Development Server 01",
        description="Development environment for team A",
        hostname="dev-01",
        fqdn="dev-01.example.com",
        ip_addresses=["10.2.1.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=4,
        memory_gb=8.0,
        storage_gb=100.0,
        status="active",
        environment="development",
        location="US-East-1",
        owner="Team A",
        department="Engineering",
        tags=["development"]
    ),
    
    # Monitoring Systems
    System(
        id="mon-01",
        name="Monitoring Server 01",
        description="Prometheus monitoring server",
        hostname="mon-01",
        fqdn="mon-01.example.com",
        ip_addresses=["10.0.3.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=4,
        memory_gb=16.0,
        storage_gb=1000.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="SRE Team",
        department="Engineering",
        tags=["monitoring", "production"]
    ),
    
    # Windows Servers
    System(
        id="win-app-01",
        name="Windows Application Server 01",
        description="Windows application server for legacy systems",
        hostname="win-app-01",
        fqdn="win-app-01.example.com",
        ip_addresses=["10.0.4.10"],
        os_type="Windows",
        os_version="Windows Server 2019",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=500.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Windows Team",
        department="Engineering",
        tags=["windows", "production"]
    ),
    
    # Load Balancers
    System(
        id="lb-prod-01",
        name="Load Balancer Production 01",
        description="Primary load balancer for web traffic",
        hostname="lb-prod-01",
        fqdn="lb-prod-01.example.com",
        ip_addresses=["10.0.5.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=4,
        memory_gb=16.0,
        storage_gb=100.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Network Team",
        department="Engineering",
        tags=["load-balancer", "production", "critical"]
    ),
    
    # Cache Servers
    System(
        id="cache-prod-01",
        name="Redis Cache Server 01",
        description="Primary Redis cache server",
        hostname="cache-prod-01",
        fqdn="cache-prod-01.example.com",
        ip_addresses=["10.0.6.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=100.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Cache Team",
        department="Engineering",
        tags=["cache", "production"]
    ),
    
    # Backup Servers
    System(
        id="backup-01",
        name="Backup Server 01",
        description="Primary backup server",
        hostname="backup-01",
        fqdn="backup-01.example.com",
        ip_addresses=["10.0.7.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=5000.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Storage Team",
        department="Engineering",
        tags=["backup", "production"]
    ),
    
    # CI/CD Servers
    System(
        id="jenkins-01",
        name="Jenkins Server 01",
        description="Primary Jenkins CI/CD server",
        hostname="jenkins-01",
        fqdn="jenkins-01.example.com",
        ip_addresses=["10.0.8.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=500.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="DevOps Team",
        department="Engineering",
        tags=["ci-cd", "production"]
    ),
    
    # Inactive Systems
    System(
        id="web-prod-02-old",
        name="Web Server Production 02 (Decommissioned)",
        description="Decommissioned web server",
        hostname="web-prod-02",
        fqdn="web-prod-02.example.com",
        ip_addresses=["10.0.1.12"],
        os_type="Linux",
        os_version="Ubuntu 20.04 LTS",
        cpu_cores=4,
        memory_gb=16.0,
        storage_gb=250.0,
        status="inactive",
        environment="production",
        location="US-East-1",
        owner="Web Team",
        department="Engineering",
        tags=["web", "production", "decommissioned"]
    ),
    
    # Systems in Maintenance
    System(
        id="db-prod-02",
        name="Database Server Production 02",
        description="Secondary PostgreSQL database server",
        hostname="db-prod-02",
        fqdn="db-prod-02.example.com",
        ip_addresses=["10.0.2.11"],
        os_type="Linux",
        os_version="RHEL 8.6",
        cpu_cores=16,
        memory_gb=64.0,
        storage_gb=2000.0,
        status="maintenance",
        environment="production",
        location="US-East-1",
        owner="Database Team",
        department="Engineering",
        tags=["database", "production", "maintenance"]
    ),
    
    # Development Workstations
    System(
        id="dev-ws-01",
        name="Developer Workstation 01",
        description="Developer workstation for team B",
        hostname="dev-ws-01",
        fqdn="dev-ws-01.example.com",
        ip_addresses=["10.2.2.10"],
        os_type="macOS",
        os_version="macOS 13.1",
        cpu_cores=8,
        memory_gb=16.0,
        storage_gb=512.0,
        status="active",
        environment="development",
        location="US-East-1",
        owner="Developer A",
        department="Engineering",
        tags=["workstation", "development"]
    ),
    
    # Test Environment
    System(
        id="test-01",
        name="Test Server 01",
        description="Test environment for QA team",
        hostname="test-01",
        fqdn="test-01.example.com",
        ip_addresses=["10.1.2.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=4,
        memory_gb=8.0,
        storage_gb=100.0,
        status="active",
        environment="testing",
        location="US-East-1",
        owner="QA Team",
        department="Engineering",
        tags=["testing", "qa"]
    ),
    
    # Logging Servers
    System(
        id="log-01",
        name="Log Server 01",
        description="ELK stack logging server",
        hostname="log-01",
        fqdn="log-01.example.com",
        ip_addresses=["10.0.9.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=2000.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="SRE Team",
        department="Engineering",
        tags=["logging", "production"]
    ),
    
    # Security Systems
    System(
        id="sec-01",
        name="Security Server 01",
        description="Security monitoring and scanning server",
        hostname="sec-01",
        fqdn="sec-01.example.com",
        ip_addresses=["10.0.10.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=4,
        memory_gb=16.0,
        storage_gb=500.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Security Team",
        department="Security",
        tags=["security", "production"]
    ),
    
    # API Servers
    System(
        id="api-prod-01",
        name="API Server Production 01",
        description="Primary API server",
        hostname="api-prod-01",
        fqdn="api-prod-01.example.com",
        ip_addresses=["10.0.11.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=250.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="API Team",
        department="Engineering",
        tags=["api", "production"]
    ),
    
    # Message Queue Servers
    System(
        id="mq-prod-01",
        name="RabbitMQ Server 01",
        description="Primary RabbitMQ message queue server",
        hostname="mq-prod-01",
        fqdn="mq-prod-01.example.com",
        ip_addresses=["10.0.12.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=4,
        memory_gb=16.0,
        storage_gb=100.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Messaging Team",
        department="Engineering",
        tags=["message-queue", "production"]
    ),
    
    # Search Servers
    System(
        id="search-prod-01",
        name="Elasticsearch Server 01",
        description="Primary Elasticsearch server",
        hostname="search-prod-01",
        fqdn="search-prod-01.example.com",
        ip_addresses=["10.0.13.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=8,
        memory_gb=32.0,
        storage_gb=1000.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Search Team",
        department="Engineering",
        tags=["search", "production"]
    ),
    
    # Analytics Servers
    System(
        id="analytics-prod-01",
        name="Analytics Server 01",
        description="Primary analytics processing server",
        hostname="analytics-prod-01",
        fqdn="analytics-prod-01.example.com",
        ip_addresses=["10.0.14.10"],
        os_type="Linux",
        os_version="Ubuntu 22.04 LTS",
        cpu_cores=16,
        memory_gb=64.0,
        storage_gb=2000.0,
        status="active",
        environment="production",
        location="US-East-1",
        owner="Analytics Team",
        department="Data Science",
        tags=["analytics", "production"]
    )
] 