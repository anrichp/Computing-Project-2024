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
      - [Scan Button and Report Display](#scan-button-and-report-display)
      - [Moodle Block Interface](#moodle-block-interface)
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
title: Moodle Block Project Structure
---
graph TD
    A[block_readabilityscore] --> B[lang]
    B --> C[en]
    C --> D[block_readabilityscore.php]
    A --> E[db]
    A --> F[amd]
    A --> G[lib.php]
    A --> H[block_readabilityscore.php]
    A --> I[version.php]
    A --> J[externallib.php]
    A --> K[tests]
    K --> L[behat]
    E --> M[access.php]
    E --> N[install.php]
    E --> O[services.php]
    E --> P[uninstall.php]
    F --> Q[src]
    Q --> R[main.js]
    Q --> S[repository.js]
```

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
title: Sequence Diagram of Readability Block
---
sequenceDiagram
    participant Client
    participant block_readabilityscore
    participant externallib
    participant lib
    participant db

    Client ->> block_readabilityscore: Request to process text
    block_readabilityscore ->> externallib: Call process_text(selectedtext, pageurl)
    externallib ->> lib: Call calculate_readability_score(selectedtext)
    lib ->> lib: Perform calculations
    lib ->> db: Store readability score
    db -->> lib: Confirmation
    lib -->> externallib: Return readability score
    externallib -->> block_readabilityscore: Return readability score
    block_readabilityscore -->> Client: Return readability score
```

```mermaid
---
title: State Diagram for Text Analyser
---
stateDiagram-v2
    State_Idle: Waiting for user action
    note left of State_Idle
        Block is waiting for user to press Scan button
    end note
    State_Analysing: Analysing text readability
    State_Reporting: Generating report and recommendations
    note right of State_Reporting
        Report is being generated
    end note
    State_Done: Results displayed
    note right of State_Done
        Results displayed to user
    end note

    State_Idle-->State_Analysing: User presses Scan button
    State_Analysing-->State_Reporting: Analysis complete
    State_Reporting-->State_Done: Report generated
    State_Done-->State_Idle: User views results

```
```mermaid
---
title: Entity Relationship Diagram
---
erDiagram
    READABILITY_SCORES {
        INTEGER id PK
        INTEGER userid
        INTEGER score
        TEXT selectedtext
        TEXT pageurl
        INTEGER timecreated
    }

    USERS {
        INTEGER id PK
        VARCHAR username
        VARCHAR email
        VARCHAR password
    }

    READABILITY_SCORES }|..|| USERS : "belongs to"

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
### User Interfaces

#### Scan Button and Report Display

```mermaid
---
title: Flow Diagram of Scan Process
---
flowchart LR
    A[Scan Button] -- click --> B[Text Analyzer]
    B -- analysis --> C[Report Display]
    C -- display --> D[Readability Scores]
    C -- display --> E[Text Structure Analysis]
    C -- display --> F[Recommendations]
```

#### Moodle Block Interface

```mermaid
---
title: Flow Diagram Showing Block Interface
---
flowchart LR
    A[Moodle Block] -- contains --> B[Scan Button]
    A -- contains --> C[Report Display]
    C -- display --> D[Readability Scores]
    C -- display --> E[Text Structure Analysis]
    C -- display --> F[Recommendations]
```

## Implementation

## Testing

## Evlauation
