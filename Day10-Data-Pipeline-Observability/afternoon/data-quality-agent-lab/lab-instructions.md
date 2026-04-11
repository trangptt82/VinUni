# Lab: Data Quality Impact on AI Agents

## Overview
In this lab, we will compare how an AI Agent (RAG-based) responds when its knowledge source is "Clean" vs "Garbage".

### 1. The Agent (Agent Setup)
We use a simple Python script to simulate an Agent. It uses a "Knowledge Base" (the CSV you generated in the ETL lab).

### 2. The Experiment

#### Step A: Clean Data Test
- Run the agent using `processed_data.csv`.
- Ask: "What is the best electronic product for $1200?"
- **Expected**: Correct answer based on your transformation.

#### Step B: Poisoned Data Test
- Create a `garbage_data.csv` with:
    - Duplicate IDs.
    - Mixed data types (e.g., price = "ten dollars").
    - Conflicting info (ID 1 is a Laptop, another ID 1 is a Banana).
- Run the agent using `garbage_data.csv`.
- Ask the same question.
- **Expected**: Observe Hallucination, Error, or Confusion.

---

## Deliverables
Students must fill out this table:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data | | | |
| Garbage Data | | | |

## Why this matters?
Most students focus on the "Prompt". Today we prove that **Quality Data > Quality Prompt**.
