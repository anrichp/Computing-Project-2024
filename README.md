# Computing Project 2024

## Contents

- [Computing Project 2024](#computing-project-2024)
  - [Contents](#contents)
  - [Requirements Gathering](#requirements-gathering)
    - [Functional Requirements](#functional-requirements)
    - [Non-functional Requirements](#non-functional-requirements)
    - [User Requirements](#user-requirements)
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

### Functional Requirements

* Analise the readability of the content.
* Provide simplification recommendations.
* Display the analysis results and recommendations.

### Non-functional Requirements

* Performance: Handle large volumes of content.
* Security: Ensure the security of the users data.
* Usability: Provide an intuitive user interface.

### User Requirements

* Users should be be able to request content analysis.
* Users should be able to view the analysis results and recommendations.

## Analysis

## Design

### Tool Architecture

```mermaid
---
title: Moodle Block Class Diagram
---
classDiagram

class MoodleBlock {
        -courseId: int
        -content: string
        +getCourseContent()
        +sendContentToReadabilityAnalyser()
        +displayReadabilityResults()
        +displaySimplificationRecommendations()
        +showReportingDashboard()
        +displayScanSummary(Scan)
    }
    class Database {
        -tables: Table[]
        +getCourseContent(courseId: int)
        +saveScanResults(scan: Scan)
        +getScanResults(courseId: int): Scan
    }
    class ReadabilityAnalyser {
        -text: string
        -readabilityScores: dict
        -structuralAnalysis: dict
        +calculateReadability()
        +performStructuralAnalysis()
        +getSimplificationRecommendations()
    }
    class ReadabilityAnalysisModule {
        +calculateFleschKincaid()
        +calculateSMOG()
        +calculateGradeLevel()
    }
    class SimplificationEngine {
        +generateSimplificationRecommendations()
    }
    class ReportingInterface {
        +displayReadabilityResults()
        +displaySimplificationRecommendations()
        +displayFullScanResults(Scan)
        +getScanResultsFromDatabase(courseId: int): Scan
    }
    class Table {
        -name: string
        -fields: Field[]
    }
    class Field {
        -name: string
        -type: string
    }
    class Scan {
        -id: int
        -courseId: int
        -readabilityScores: dict
        -structuralAnalysis: dict
    }
    MoodleBlock --> ReadabilityAnalyser: uses
    ReadabilityAnalyser --> ReadabilityAnalysisModule: uses
    ReadabilityAnalyser --> SimplificationEngine: uses
    MoodleBlock --> Database: uses
    Database --> Table: stores
    Table --> Field: stores
    MoodleBlock --> ReportingInterface: uses
    MoodleBlock --> Scan: displays summary
    ReportingInterface --> Database: obtains scan results
    ReportingInterface --> Scan: displays full results
```

```mermaid
---
title: Sequence Diagram of Application Components
---
sequenceDiagram
    participant MoodleBlock as "Moodle Block"
    participant ReadabilityAnalyser as "Readability Analyser"
    participant SimplificationEngine as "Simplification Engine"
    participant Database as "Database"
    participant ReportingInterface as "Reporting Interface"

    note left of MoodleBlock: User requests accessibility analysis
    MoodleBlock->>ReadabilityAnalyser: Request analysis
    ReadabilityAnalyser->>Database: Retrieve content
    Database->>ReadabilityAnalyser: Return content
    ReadabilityAnalyser->>ReadabilityAnalyser: Perform readability analysis
    ReadabilityAnalyser->>SimplificationEngine: Request simplification recommendations
    SimplificationEngine->>SimplificationEngine: Generate recommendations
    SimplificationEngine->>ReadabilityAnalyser: Return recommendations
    ReadabilityAnalyser->>ReportingInterface: Send analysis results
    ReportingInterface->>ReportingInterface: Generate report
    ReportingInterface->>MoodleBlock: Display report
```

```mermaid
---
title: Sequence Diagram for Text Analyser
---
stateDiagram-v2
    State_Idle: Waiting for users input
    note left of State_Idle
        Tool is waiting for a user to select a course
    end note
    State_Analysing: Analysing text readability
    State_Reporting: Generating report and reccomendations
    note right of State_Reporting
        Report is being generated
    end note
    State_Done: Results displayed
    note right of State_Done
        Results displayed to user
    end note

    State_Idle-->State_Analysing: User selects course
    State_Analysing-->State_Reporting
    State_Reporting-->State_Done
    State_Done-->State_Idle

```

```mermaid
---
title: Flow Diagram of Text Analysing
---
flowchart LR
    start([Start])-->cond1{Complex sentence detected?}
    cond1-->|Yes| simplify1[Apply rule-based heuristics]
    simplify1-->cond2{Improved readability?}
    cond2-->|Yes| done([Done])
    cond2-->|No| simplify2[Apply machine learning model]
    simplify2-->done

    cond1-->|No| done
```

```mermaid
---
title: Readability Analyser Class Diagram
---
classDiagram
    note "Readability Analyser and dependencies"
    ReadabilityAnalyser <|-- TextstatLibrary
    ReadabilityAnalyser <|-- SpacyLibrary
    ReadabilityAnalyser <|-- SQLiteDatabase
    class ReadabilityAnalyser{
        -courseContent: string
        -readabilityScores: object
        -textStructure: object
        +analyzeText()
        +generateReport()
    }
    class TextstatLibrary{
        +calculateReadabilityScores(text: string)
    }
    class SpacyLibrary{
        +analyzeTextStructure(text: string)
    }
    class SQLiteDatabase{
        +saveScanResults(courseId: int, results: object)
    }
```

### User Interfaces

#### Login Page

##### Login Graph Diagram

```mermaid
---
title: Graph Diagram of Login Sequence
---
graph TD
    A[TextBox: Username] ---> | Enter Username | B[TextBox: Password]
    B ---> | Enter Password | C[Button: Login]
    C ---> | Login Successful | D[Main Application]
    C ---> | Invalid Credentials | E[Error Message]
    E ---> | Try Again | A
```

##### Login Sequence Diagram

```mermaid
---
title: Sequence Diagram of Login Process
---
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
