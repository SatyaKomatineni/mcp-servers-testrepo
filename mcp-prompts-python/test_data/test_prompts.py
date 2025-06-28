from models.prompt import Prompt

test_prompts = [
    # Developer Prompts
    Prompt(
        id="DEV-001",
        name="Code Review Assistant",
        description="Helps developers review code for best practices and potential issues",
        role="developer",
        prompt_string="Please review the following code for potential issues, security concerns, and adherence to best practices. Focus on code quality, maintainability, and performance."
    ),
    Prompt(
        id="DEV-002",
        name="API Documentation Generator",
        description="Generates comprehensive API documentation from code",
        role="developer",
        prompt_string="Analyze the following API endpoint code and generate comprehensive documentation including parameters, response types, and example usage."
    ),
    Prompt(
        id="DEV-003",
        name="Code Refactoring Advisor",
        description="Suggests code refactoring opportunities",
        role="developer",
        prompt_string="Review the following code and suggest specific refactoring opportunities to improve readability, maintainability, and performance."
    ),
    Prompt(
        id="DEV-004",
        name="Dependency Analyzer",
        description="Analyzes project dependencies for security and compatibility",
        role="developer",
        prompt_string="Analyze the following dependency list and identify potential security vulnerabilities, outdated packages, and compatibility issues."
    ),
    Prompt(
        id="DEV-005",
        name="Performance Optimizer",
        description="Identifies performance bottlenecks in code",
        role="developer",
        prompt_string="Review the following code and identify potential performance bottlenecks. Suggest specific optimizations with explanations."
    ),

    # Tester Prompts
    Prompt(
        id="TEST-001",
        name="Test Case Generator",
        description="Generates comprehensive test cases from requirements",
        role="tester",
        prompt_string="Based on the following requirements, generate a comprehensive set of test cases covering happy path, edge cases, and error scenarios."
    ),
    Prompt(
        id="TEST-002",
        name="Bug Report Analyzer",
        description="Analyzes bug reports for completeness and clarity",
        role="tester",
        prompt_string="Review the following bug report and suggest improvements for clarity, reproducibility, and completeness."
    ),
    Prompt(
        id="TEST-003",
        name="Test Coverage Analyzer",
        description="Analyzes test coverage and suggests improvements",
        role="tester",
        prompt_string="Analyze the following test coverage report and identify areas that need additional test coverage with specific suggestions."
    ),
    Prompt(
        id="TEST-004",
        name="Performance Test Designer",
        description="Designs performance test scenarios",
        role="tester",
        prompt_string="Design a comprehensive performance test plan for the following system, including load testing, stress testing, and scalability testing scenarios."
    ),
    Prompt(
        id="TEST-005",
        name="Security Test Planner",
        description="Plans security testing strategies",
        role="tester",
        prompt_string="Create a security testing strategy for the following application, including penetration testing, vulnerability assessment, and security compliance checks."
    ),

    # Care Coordinator Prompts
    Prompt(
        id="CARE-001",
        name="Patient Care Plan Generator",
        description="Generates personalized patient care plans",
        role="care_coordinator",
        prompt_string="Based on the following patient information, generate a comprehensive care plan including treatment goals, interventions, and follow-up schedules."
    ),
    Prompt(
        id="CARE-002",
        name="Resource Allocation Advisor",
        description="Suggests optimal resource allocation for patient care",
        role="care_coordinator",
        prompt_string="Analyze the following patient cases and suggest optimal allocation of healthcare resources, including staff, equipment, and facilities."
    ),
    Prompt(
        id="CARE-003",
        name="Care Transition Planner",
        description="Plans smooth transitions between care settings",
        role="care_coordinator",
        prompt_string="Create a detailed transition plan for the following patient moving between care settings, including necessary documentation and coordination steps."
    ),
    Prompt(
        id="CARE-004",
        name="Patient Education Designer",
        description="Designs patient education materials",
        role="care_coordinator",
        prompt_string="Design patient education materials for the following condition, including treatment options, self-care instructions, and warning signs to watch for."
    ),
    Prompt(
        id="CARE-005",
        name="Care Team Coordinator",
        description="Coordinates care team activities",
        role="care_coordinator",
        prompt_string="Create a coordination plan for the following patient's care team, including roles, responsibilities, and communication protocols."
    ),

    # Project Manager Prompts
    Prompt(
        id="PM-001",
        name="Project Risk Analyzer",
        description="Analyzes project risks and suggests mitigation strategies",
        role="project_manager",
        prompt_string="Analyze the following project details and identify potential risks, their impact, and suggest specific mitigation strategies."
    ),
    Prompt(
        id="PM-002",
        name="Resource Planning Advisor",
        description="Helps with project resource planning",
        role="project_manager",
        prompt_string="Based on the following project requirements, create a detailed resource plan including team composition, equipment needs, and budget estimates."
    ),
    Prompt(
        id="PM-003",
        name="Timeline Optimizer",
        description="Optimizes project timelines",
        role="project_manager",
        prompt_string="Review the following project timeline and suggest optimizations to reduce duration while maintaining quality and scope."
    ),
    Prompt(
        id="PM-004",
        name="Stakeholder Communication Planner",
        description="Plans stakeholder communication strategies",
        role="project_manager",
        prompt_string="Design a comprehensive stakeholder communication plan for the following project, including key messages, communication channels, and frequency."
    ),
    Prompt(
        id="PM-005",
        name="Project Status Reporter",
        description="Generates comprehensive project status reports",
        role="project_manager",
        prompt_string="Generate a detailed project status report based on the following project metrics, including progress, risks, and next steps."
    ),

    # Enterprise Architect Prompts
    Prompt(
        id="EA-001",
        name="Architecture Review Assistant",
        description="Reviews system architecture for best practices",
        role="enterprise_architect",
        prompt_string="Review the following system architecture and provide recommendations for alignment with enterprise standards, scalability, and maintainability."
    ),
    Prompt(
        id="EA-002",
        name="Technology Roadmap Designer",
        description="Designs technology roadmaps",
        role="enterprise_architect",
        prompt_string="Create a technology roadmap for the following enterprise, including current state assessment, future state vision, and transition strategies."
    ),
    Prompt(
        id="EA-003",
        name="Integration Strategy Planner",
        description="Plans system integration strategies",
        role="enterprise_architect",
        prompt_string="Design an integration strategy for the following systems, considering data flow, security, and scalability requirements."
    ),
    Prompt(
        id="EA-004",
        name="Architecture Pattern Advisor",
        description="Advises on architecture patterns",
        role="enterprise_architect",
        prompt_string="Recommend appropriate architecture patterns for the following system requirements, considering scalability, maintainability, and performance needs."
    ),
    Prompt(
        id="EA-005",
        name="Technology Stack Evaluator",
        description="Evaluates technology stack options",
        role="enterprise_architect",
        prompt_string="Evaluate the following technology stack options for the given requirements, considering factors like scalability, maintainability, and total cost of ownership."
    ),

    # Additional Cross-Role Prompts
    Prompt(
        id="CROSS-001",
        name="Documentation Generator",
        description="Generates comprehensive documentation",
        role="developer",
        prompt_string="Generate comprehensive documentation for the following system, including technical specifications, user guides, and API documentation."
    ),
    Prompt(
        id="CROSS-002",
        name="Process Optimizer",
        description="Optimizes business processes",
        role="project_manager",
        prompt_string="Analyze the following business process and suggest optimizations for efficiency, quality, and compliance."
    ),
    Prompt(
        id="CROSS-003",
        name="Quality Assurance Advisor",
        description="Advises on quality assurance practices",
        role="tester",
        prompt_string="Review the following quality assurance practices and suggest improvements for effectiveness and efficiency."
    ),
    Prompt(
        id="CROSS-004",
        name="System Integration Tester",
        description="Tests system integrations",
        role="tester",
        prompt_string="Design a comprehensive integration testing strategy for the following systems, including test scenarios and validation criteria."
    ),
    Prompt(
        id="CROSS-005",
        name="Healthcare Workflow Optimizer",
        description="Optimizes healthcare workflows",
        role="care_coordinator",
        prompt_string="Analyze the following healthcare workflow and suggest optimizations for patient care, staff efficiency, and resource utilization."
    )
] 