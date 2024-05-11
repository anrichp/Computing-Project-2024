# Computing Project 2024

## Contents
- [Computing Project 2024](#computing-project-2024)
  - [Contents](#contents)
  - [Requirements Gathering](#requirements-gathering)
  - [Analysis](#analysis)
  - [Design](#design)
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