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
    class block_base {
        <<Moodle Core>>
        +instance
        +config
        +title
        +content
        +init()
        +specialization()
        +applicable_formats()
        +instance_allow_multiple()
        +get_content()
        +hide_header()
    }
    class block_readabilityscore {
        +init()
        +specialization()
        +applicable_formats()
        +get_content()
    }
    class TextStatistics {
        +word_count(text)
        +sentence_count(text)
        +complex_word_count(text)
        -is_complex_word(word)
        -syllable_count(word)
        +gunning_fog(text)
    }
    class block_readabilityscore_external {
        +process_text_parameters()
        +process_text(selectedtext, pageurl)
        +process_text_returns()
    }
    class external_api {
        <<Moodle Core>>
        +validate_parameters()
        +validate_context()
        +get_context_from_params()
    }
    class Dashboard {
        +display_readability_levels()
        +display_scans()
        +filter_by_page_url()
    }

    block_base <|-- block_readabilityscore
    block_readabilityscore ..> TextStatistics : uses
    external_api <|-- block_readabilityscore_external
    block_readabilityscore_external ..> TextStatistics : uses
    block_readabilityscore ..> Dashboard : links to
```

```mermaid
---
title: Sequence Diagram of Readability Block
---
sequenceDiagram
    participant User
    participant Block UI
    participant main.js
    participant repository.js
    participant externallib.php
    participant lib.php
    participant Database

    User->>Block UI: Clicks 'Scan' button
    Block UI->>main.js: Trigger scan event
    main.js->>User: Prompt to select text
    User->>main.js: Selects text
    main.js->>repository.js: Send selected text
    repository.js->>externallib.php: AJAX call (processText)
    externallib.php->>lib.php: Calculate readability score
    lib.php->>externallib.php: Return score
    externallib.php->>Database: Store result
    externallib.php->>repository.js: Return result
    repository.js->>main.js: Display score
    main.js->>Block UI: Update UI with score
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
title: Flow Diagram of Moodle Block
---
flowchart TD
    start --> fetchSelectedText
    fetchSelectedText --> calculateReadabilityScore
    calculateReadabilityScore --> countSyllables
    countSyllables --> countWords
    countWords --> countSentences
    countSentences --> calculateReadabilityScore
    calculateReadabilityScore --> generateContent
    generateContent --> storeScanInDatabase
    storeScanInDatabase --> showContent
    showContent --> stop

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
## Implementation

## Testing

## Evlauation
