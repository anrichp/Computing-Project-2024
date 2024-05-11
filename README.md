# Computing Project 2024

## Contents
- [Computing Project 2024](#computing-project-2024)
  - [Contents](#contents)
  - [Requirements Gathering](#requirements-gathering)
  - [Analysis](#analysis)
  - [Design](#design)
    - [Tool Architecture](#tool-architecture)
    - [User Interfaces](#user-interfaces)
      - [Login Page](#login-page)
        - [Login Graph Diagram](#login-graph-diagram)
        - [Login Sequence Diagram](#login-sequence-diagram)
  - [Implementation](#implementation)
  - [Testing](#testing)
  - [Evlauation](#evlauation)

## Requirements Gathering 

## Analysis

## Design
### Tool Architecture
```mermaid
sequenceDiagram
    participant Moodle as "Moodle REST API"
    participant Tool as "Readability Analyser Tool"
    participant Textstat as "Textstat Library"
    participant Spacy as "Spacy Library"
    participant DB as "SQLite Database"

    Note right of Moodle: Retrieve course content
    Moodle->>Tool: GET /course/content
    Tool->>Moodle: JSON response

    Note right of Tool: Analyze text readability
    Tool->>Textstat: Calculate readability scores
    Textstat->>Tool: Readability scores
    Tool->>Spacy: Analyze text structure
    Spacy->>Tool: Text structure analysis

    Note right of Tool: Store results in database
    Tool->>DB: Save scan results
    DB->>Tool: Saved successfully

    Note right of Tool: Display results and recommendations
    Tool->>Tool: Generate report and simplification recommendations
    Tool->>User: Display report and recommendations
```
### User Interfaces
#### Login Page
##### Login Graph Diagram
```mermaid
graph TD
    A[TextBox: Username] ---> | Enter Username | B[TextBox: Password]
    B ---> | Enter Password | C[Button: Login]
    C ---> | Login Successful | D[Main Application]
    C ---> | Invalid Credentials | E[Error Message]
    E ---> | Try Again | A
```
##### Login Sequence Diagram
```mermaid
sequenceDiagram
    participant User as "User"
    participant LoginPage as "Login Page"
    participant LoginButton as "Login Button"
    participant Authentication as "Authentication"

    User->>LoginPage: enter username and password
    LoginPage->>LoginButton: click login
    LoginButton->>Authentication: authenticate
    Authentication->>User: authentication result
```
## Implementation

## Testing

## Evlauation