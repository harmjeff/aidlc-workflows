# Discovery Report

**Project**: [Project Name]  
**Date**: [Date]  
**Phase**: Discovery  
**Status**: [Complete/In Progress]

## Executive Summary

This report documents the development environment, coding standards, and Agile process established for the project. It provides technical leaders with the information needed to evaluate tools, libraries, languages, coding practices, and other aspects of the produced code.

## 1. Workspace Analysis

### 1.1 Workspace State
- **Project Type**: [Greenfield/Brownfield]
- **Existing Code**: [Yes/No - description]
- **Template/Starter Code**: [If applicable, describe template location and purpose]
- **Workspace Root**: [Path]

### 1.2 Existing Code Analysis (if applicable)
- **Technologies Found**: [List technologies in existing code]
- **Structure**: [Monolith/Microservices/Library/etc.]
- **Build System**: [If found]
- **Key Findings**: [Important observations about existing code]

### 1.3 Template/Starter Code (if applicable)
- **Template Location**: [Path to template]
- **Template Technologies**: [List technologies used in template]
- **Template Patterns to Preserve**: [List patterns/components to keep]
- **Template Patterns to Replace**: [List patterns/components to replace]
- **Migration Strategy**: [How template will be adapted for project]

## 2. Development Environment

### 2.1 Operating Systems
- **Primary OS**: [Operating System and Version]
- **Supported OS**: [List supported operating systems]
- **Notes**: [Any OS-specific considerations]

### 2.2 Development Tools
- **IDE/Editor**: [Tool name and version]
- **Version Control**: [Git/SVN/etc. and version]
- **Build Tool**: [Maven/Gradle/npm/etc. and version]
- **Package Manager**: [npm/pip/etc. and version]
- **Other Tools**: [List other development tools]

### 2.3 Runtime Environment
- **Language Version**: [e.g., Java 17, Node.js 18, Python 3.11]
- **Runtime**: [JVM, Node.js, Python interpreter, etc.]
- **Framework**: [Spring Boot, Express, Django, etc. and version]

### 2.4 Infrastructure Tools
- **Cloud Provider**: [AWS/Azure/GCP/On-premise]
- **Container Platform**: [Docker/Kubernetes/etc.]
- **CI/CD**: [Jenkins/GitHub Actions/etc.]
- **Monitoring**: [CloudWatch/Datadog/etc.]

## 3. Coding Standards

### 3.1 Code Style Guide
- **Style Guide**: [Google Style Guide, Airbnb, etc.]
- **Formatting Tool**: [Prettier, Black, etc.]
- **Linting Tool**: [ESLint, Checkstyle, etc.]
- **Configuration**: [Link to configuration files]

### 3.2 Naming Conventions
- **Variables**: [camelCase, snake_case, etc.]
- **Classes**: [PascalCase, etc.]
- **Constants**: [UPPER_SNAKE_CASE, etc.]
- **Files**: [Naming pattern]

### 3.3 Documentation Standards
- **Code Comments**: [Required level and format]
- **API Documentation**: [OpenAPI/Swagger, JSDoc, etc.]
- **README Requirements**: [What must be included]

### 3.4 Code Review Process
- **Review Requirements**: [Number of reviewers, approval process]
- **Review Checklist**: [Link to checklist]
- **Automated Checks**: [Pre-commit hooks, CI checks]

## 4. Development Workflow

### 4.1 Workflow Type
- **Workflow Type**: [Scrum/Kanban/AI-DLC/Custom/etc.]
- **Workflow Description**: [How the workflow operates]
- **Sprint/Iteration Duration**: [If applicable - 1 week, 2 weeks, etc.]
- **Planning Process**: [How planning is done]
- **Daily Standup**: [Time and format, if applicable]
- **Review Process**: [How reviews are conducted]
- **Retrospective**: [Process and duration, if applicable]

**Note**: [Any special notes about the workflow, e.g., "This project uses AI-DLC adaptive workflow rather than traditional sprints"]

### 4.2 Sprint Structure (if applicable)
- **Sprint Duration**: [1 week, 2 weeks, etc.]
- **Sprint Planning**: [Process and duration]
- **Daily Standup**: [Time and format]
- **Sprint Review**: [Process and duration]
- **Retrospective**: [Process and duration]

### 4.3 Estimation
- **Estimation Method**: [Story points, T-shirt sizes, etc.]
- **Estimation Scale**: [Fibonacci, 1-10, etc.]
- **Estimation Process**: [Planning poker, etc.]

### 4.4 Definition of Done
- [ ] Code written and reviewed
- [ ] Unit tests written and passing
- [ ] Integration tests passing (if applicable)
- [ ] Documentation updated
- [ ] Code merged to main branch
- [ ] [Additional criteria]

### 4.5 Workflow
- **Branch Strategy**: [Git Flow, GitHub Flow, etc.]
- **Pull Request Process**: [Requirements and process]
- **Deployment Process**: [Process description]

## 5. Team Structure

### 5.1 Team Members
| Role | Name | Responsibilities |
|------|------|------------------|
| Product Owner | [Name] | [Responsibilities] |
| Tech Lead | [Name] | [Responsibilities] |
| Developer | [Name] | [Responsibilities] |
| QA Engineer | [Name] | [Responsibilities] |

### 5.2 Communication Channels
- **Primary**: [Slack, Teams, etc.]
- **Meetings**: [Tool and schedule]
- **Documentation**: [Confluence, Wiki, etc.]

### 5.3 Decision-Making Process
- **Technical Decisions**: [Process]
- **Architecture Decisions**: [Process]
- **Scope Decisions**: [Process]

## 6. Project Structure

### 6.1 Directory Structure
```
[Project Root]/
├── src/
│   ├── main/
│   │   ├── java/ (or appropriate language)
│   │   └── resources/
│   └── test/
├── docs/
├── scripts/
└── [Other directories]
```

### 6.2 Configuration Management
- **Environment Variables**: [How managed]
- **Configuration Files**: [Location and format]
- **Secrets Management**: [Tool and process]

## 7. Technology Stack Summary

### 7.1 Technology Decisions
| Layer | Technology | Version | Rationale |
|-------|-----------|---------|-----------|
| Frontend Framework | [React/Vue/Angular/etc.] | [Version] | [Why chosen] |
| Frontend Language | [TypeScript/JavaScript/etc.] | [Version] | [Why chosen] |
| Backend Framework | [FastAPI/Express/Django/etc.] | [Version] | [Why chosen] |
| Backend Language | [Python/Node.js/Java/etc.] | [Version] | [Why chosen] |
| Database | [PostgreSQL/MySQL/MongoDB/etc.] | [Version] | [Why chosen] |
| Cache | [Redis/Memcached/etc.] | [Version] | [Why chosen] |
| Container Runtime | [Docker/Podman/etc.] | [Version] | [Why chosen] |

### 7.2 Key Technology Rationale
- [Major technology decision 1]: [Rationale]
- [Major technology decision 2]: [Rationale]

## 8. Quality Assurance

### 8.1 Testing Strategy
- **Unit Testing**: [Framework and approach]
- **Integration Testing**: [Framework and approach]
- **E2E Testing**: [Framework and approach]
- **Test Coverage Target**: [Percentage]

### 8.2 Code Quality Tools
- **Static Analysis**: [SonarQube, CodeClimate, etc.]
- **Dependency Scanning**: [Snyk, Dependabot, etc.]
- **Security Scanning**: [Tool and process]

## 9. Dependencies and Libraries

### 9.1 Core Dependencies
| Library | Version | Purpose |
|---------|---------|---------|
| [Library] | [Version] | [Purpose] |
| [Library] | [Version] | [Purpose] |

### 9.2 Dependency Management
- **Update Process**: [How dependencies are updated]
- **Version Pinning**: [Strategy]
- **Security Updates**: [Process]

## 10. Human Tasks to Complete Phase

### 10.1 Immediate Actions
- [ ] Review and approve this Discovery Report
- [ ] Set up development environment per specifications
- [ ] Configure IDE/editor with coding standards
- [ ] Set up version control repository
- [ ] Configure CI/CD pipeline

### 10.2 Team Alignment
- [ ] Share Discovery Report with team
- [ ] Conduct team review session
- [ ] Address any questions or concerns
- [ ] Get team sign-off on standards and process

### 10.3 Environment Setup
- [ ] Install required tools and dependencies
- [ ] Configure development environment
- [ ] Set up test environment
- [ ] Configure monitoring and logging

## 11. Notes and Decisions

### 11.1 Key Decisions
- [Decision 1]: [Rationale]
- [Decision 2]: [Rationale]

### 11.2 Project Constraints
- **Network Constraints**: [Internal only, VPN required, etc.]
- **Infrastructure Constraints**: [On-premise, specific hardware, etc.]
- **Scale Constraints**: [User limits, data limits, etc.]
- **Technology Constraints**: [Must use specific technologies, etc.]
- **Resource Constraints**: [Team size, budget, timeline, etc.]

### 11.3 Assumptions
- **Infrastructure Assumptions**: [Available services, network setup, etc.]
- **Team Assumptions**: [Skills available, availability, etc.]
- **Business Assumptions**: [User behavior, requirements stability, etc.]
- **Technical Assumptions**: [Technology availability, compatibility, etc.]

### 11.4 Open Questions
- [Question 1]: [Status]
- [Question 2]: [Status]

## 12. Approval

**Prepared by**: [Name]  
**Reviewed by**: [Name]  
**Approved by**: [Name]  
**Date**: [Date]

---

**Next Phase**: Vision
