# Lab Outline: ETL Automation & Data Quality Impact

## Introduction (15 mins)
- Setting up the "Lab 10" workspace.
- Understanding the Goal: Build a pipeline that doesn't just "move" data, but "validates" it.

## Part 1: ETL Automation (75 mins)
- **Task**: Automate a pipeline that reads "Sales Data" from a JSON mock API, transforms it (normalization), and loads it into a clean CSV for an AI Agent to read.
- **Complexity Level**: Intermediate (Perfect for vibe coders using AI assistance).
- **Core Concept**: 
    - `fetch_data()` -> `validate_data()` -> `transform_data()` -> `load_data()`.
- **Validation Focus**: Checking for nulls, out-of-range values, and duplicate IDs.

## Part 2: Stress Test — The "Poisoned" Agent (60 mins)
- **The Setup**: We use a pre-built AI Agent (Chatbot) that answers questions based on the data.
- **The Experiment**:
    - Scenario A: Agent reads "Clean" data. (Observe accuracy).
    - Scenario B: Agent reads "Poisoned/Garbage" data (duplicates, extreme outliers, broken schema).
- **Deliverable**: A short report on how the Agent's behavior changed (hallucinations, bias, failure to respond).

## Part 3: Grading & Peer Review (30 mins)
- Comparing solution codes.
- Running the `scoring.py` script to check metric coverage.

---

## Technical Requirements
- Python 3.x
- Libraries: `pandas`, `requests`, `pydantic` (for validation).
- Environment: Google Colab or Local VS Code.
