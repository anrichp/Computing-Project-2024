# Algorithm Evaluation

## Design Diagrams
```mermaid
---
title: Flow Diagram
---
graph TD
    A[Start] --> B[Set up Logging]
    B --> C[Define Root Directory and Subdirectories]
    C --> D[Initialize Readability Data List]
    D --> E[Define Function to Calculate Readability Scores]
    E --> F[Iterate Through Directories]
    F --> G[For Each File in Directory]
    G --> H[Check if File is a Text File]
    H -- Yes --> I[Read File Content]
    I --> J[Calculate Readability Scores]
    J --> K[Store Scores in List]
    K --> L[Log Processed File]
    H -- No --> M[Skip File]
    L --> N{More Files?}
    N -- Yes --> G
    N -- No --> O[Create DataFrame from Readability Data]
    O --> P[Export DataFrame to Excel]
    P --> Q[End]

```
```mermaid
---
title: Class Diagram
---
classDiagram
    class Logger {
        -level : INFO
        -format : string
        +basicConfig()
    }

    class FileManager {
        -root_dir : string
        -directories : dict
        +iterate_directories()
    }

    class ReadabilityCalculator {
        +get_readability_scores(text : string) : dict
    }

    class DataFrameManager {
        -readability_data : list
        +create_dataframe(data : list) : DataFrame
        +export_to_excel(df : DataFrame, filename : string)
    }

    Logger -- FileManager
    Logger -- ReadabilityCalculator
    FileManager -- ReadabilityCalculator
    FileManager -- DataFrameManager
    DataFrameManager -- ReadabilityCalculator

```
```mermaid
---
title: Sequence Diagram
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