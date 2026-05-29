# NBA-GUI-
An NBA management system built on strict Model-View-Controller (MVC) architecture, featuring multi window navigation state management, multi criteria data filtering pipelines, and reactive data observability patterns

----
## Architectural Overview & System Design
The application is built entirely on a **Model-View-Controller (MVC)** architectural pattern to ensure complete decoupling of data structures, business logic, and presentation layers.

```
              ┌─────────────────────────────────────────┐
              │                 MODEL                   │
              │   (Data Structures & Business Logic)    │
              └────────────┬───────────────▲────────────┘
                           │               │
   Notifies View of Changes│               │Updates Model
   via Property Listeners  │               │via Action Handlers
                           ▼               │
┌────────────────────────────┐           ┌─┴──────────────────────────┐
│            VIEW            │           │         CONTROLLER         │
│  (FXML / Presentation)     ├──────────►│ (Action Event Listeners)   │
└────────────────────────────┘User Action└────────────────────────────┘

```

----
### Core Architecture Specifications:
* **Presentation Layer:** Designed declaratively via **FXML** coupled with custom corporate CSS skinning, eliminating presentation logic within raw code files.
* **State & Stage Management:** Orchestrates a nested, multi layered window deployment pipeline. The core hub manages distinct standalone window lifecycles for roster additions, updates, and diagnostic errors.
* **Data Observability:** Implements the **Observer Pattern** leveraging native data property mapping and observable collection wrappers. Any structural change in underlying model entities propagates synchronously to update tabular graphical nodes in real time.

----
## Functional Requirements Mapping
To ensure the software addresses accurate business requirements, the application fulfills the following functional matrices:

### 1. Roster Management & Multi-Stage CRUD Operations
* **Requirement:** Provide administrative capability to add, view, update, and delete teams and athletic profiles within isolated data nodes.
* **System Implementation:** Deployed a responsive `Teams Table View` displaying real-time aggregated metrics (Average Player Credit, Average Age, and Roster Headcounts). Row selection flags toggle contextual visibility state buttons (`Manage`, `Delete`), locking or unlocking functional pathways depending on system context.

### 2. Multi-Criteria Collaborative Filtering Pipelines
* **Requirement:** Allow business analysts to search cross-team personnel profiles via collaborative, non case sensitive conditions simultaneously.
* **System Implementation:** Created a multi input data filter logic block combining Level text matching, Partial Name text matching, and Upper/Lower boundary Age constraints. Inputs execute down an iterative pipeline, instantly filtering active table rows or displaying structured placeholder fallbacks if sero-match exceptions occur.

----
## Data Integrity & Input Validation Engine
System workflows are heavily protected by an autonomous validation engine, routing structural inputs through a validation pattern matching algorithm before database assignment commits occur:

* **Name Pattern Auditing:** Strings are programmatically verified via regular expressions ensuring a rigid format (First Name and Last Name must both exist as capital letter capitalised words).
* **Numerical Bounds Auditing:** Roster numeric identifiers (Player No, Age, Credit limits) must qualify as positive whole integers or structural decimals.
* **Collision Protection Logic:** Prior to finalising record modifications, an indexing engine scans memory allocation to catch entity key duplication, throwing localised `Error/Input Error` window exceptions to block data corruption.

----
## Technology Stack & Environment Details
* **Core Language:** Python (Object-Oriented Design Paradigm)
* **GUI Engine:** JavaFX / Tkinter Frameworks
* **Layout Mapping:** Declarative FXML UI Structuring
* **Design Metaphor:** Model-View-Controller (MVC) 
* **Target Runtime Infrastructure:** OpenJDK Runtime Engine Core Baseline
