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
    class block_readabilityscore {
        - title: string
        - content: string
        + init()
        + specialization()
        + get_content()
        + applicable_formats()
    }
    class block_readabilityscore_external {
        + process_text(selectedtext: string, pageurl: string)
        + process_text_parameters()
        + process_text_returns()
    }
    class external_api {
        + validate_parameters(params: object, data: object)
    }
    block_readabilityscore --> block_readabilityscore_external : extends
    block_readabilityscore_external --> external_api : extends
    class readability_score {
        + calculate_readability_score(text: string)
    }
    class lib {
        + readability_score(text: string)
        + count_syllables(word: string)
        + count_words_custom(text: string)
        + count_sentences(text: string)
        + calculate_readability_score(text: string)
        + store_readability_score(userid: int, score: int, selectedtext: string, pageurl: string)
    }
    block_readabilityscore --> lib : uses
    block_readabilityscore_external --> lib : uses
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
title: State Diagram for Moodle Block
---
stateDiagram
    state ReadabilityScoreBlock {
        [*] --> Idle
        Idle --> GettingContent : get_content()
        GettingContent --> ShowingContent : content generated
        ShowingContent --> Idle : user interaction
        Idle --> Uninstalling : uninstall.php
        Uninstalling --> [*]
    }
    state GettingContent {
        [*] --> FetchingData
        FetchingData --> ProcessingData : data fetched
        ProcessingData --> GeneratingContent : data processed
        GeneratingContent --> [*]
    }
    state ProcessingData {
        [*] --> CalculatingScore
        CalculatingScore --> CountingSyllables : score calculated
        CountingSyllables --> CountingWords : syllables counted
        CountingWords --> CountingSentences : words counted
        CountingSentences --> CalculatingScore : sentences counted
    }

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
