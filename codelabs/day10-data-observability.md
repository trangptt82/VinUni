---
id: day-10-data-observability
summary: Learn the principles of Data Pipeline Observability and Data Quality for AI Agents.
authors: VinUni Guru
categories: Data Science, AI
status: Published
feedback link: https://github.com/appsheetway/VinUni/issues
---

# Day 10: Data Pipeline & Data Observability

## 1. Introduction: The Digestive System of AI
Duration: 0:05:00

In this session, we explore the "Digestive System" metaphor for data pipelines:
- **Ingestion** = Eating (Ăn vào).
- **Processing** = Digestion/Metabolism (Tiêu hóa/Chuyển hóa).
- **Observability** = Periodic Health Checks (Đi khám bác sĩ định kỳ).
- **AI Agent** = The Brain (Cần năng lượng sạch để suy nghĩ đúng).

> aside positive
> **Remember**: An AI Agent needs high-quality data to avoid hallucinations. "Garbage In, Professional Garbage Out."

---

## 2. Key Concepts & Guru Q&A
Duration: 0:10:00

### Why use tools like Airbyte or dbt?
Scripting works for one source, but it becomes a maintenance nightmare at scale. Tools provide standards and save hundreds of hours when APIs change.

### Can LLMs handle noisy data?
LLMs are smart but prone to hallucination. If input data is wrong, they will confidently provide a worthless answer.

### How to spot a "sick" pipeline?
Use observability metrics! If volume drops from 10,000 to 10 records, the code might not crash, but the data is broken.

---

## 3. Lab: Data Quality Impact on AI Agents
Duration: 0:15:00

In this lab, we compare how an AI Agent (RAG-based) responds to "Clean" vs. "Garbage" data.

### Step A: Generate Garbage Data
We need to create a "Poisoned" dataset to test our Agent's limits.

```python
import csv

def generate_garbage_data():
    data = [
        ['id', 'product', 'price', 'category'],
        [1, 'Laptop', 1200, 'electronics'],
        [1, 'Banana', 2, 'fruit'], # Duplicate ID
        [2, 'Broken Chair', 'ten dollars', 'furniture'], # Wrong type
        [3, 'Nuclear Reactor', 999999, 'electronics'], # Extreme Outlier
        [None, 'Ghost Item', 0, None], # Null values
    ]
    with open('garbage_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("garbage_data.csv has been created.")

generate_garbage_data()
```

---

## 4. Step B: Testing the Agent
Duration: 0:10:00

Now, simulate the Agent's response using the "Knowledge Base" (the CSV you just created).

### Observe the impact:
1. Run the script with `processed_data.csv` (Clean).
2. Run the script with `garbage_data.csv` (Poisoned).

> aside negative
> **Warning**: Observe how the duplicate IDs and mixed data types cause the Agent to "choke" or return hallucinated results (e.g., a "Laptop Banana").

---

## 5. Summary & Deliverables
Duration: 0:05:00

Fill out the following table based on your observations:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data | | | |
| Garbage Data | | | |

### Why this matters?
Most students focus on the "Prompt". Today we proved that **Quality Data > Quality Prompt**.
