# Google Codelab: Building a Reliable ETL for AI Agents

## 1. Overview
In this Codelab, you will learn how to:
- Extract data from JSON sources.
- Implement robust validation logic.
- Observe pipeline performance via logging.

## 2. Prerequisites
- Python installed or access to Google Colab.
- Basic knowledge of `pip install pandas`.

## 3. Step-by-Step Instructions
### Step 3.1: The Fetcher
Write the `extract()` function to handle potential `FileNotFoundError`.

### Step 3.2: The Quality Guard
Implement the `validate()` function. Remember to handle the "ten dollars" edge case!

### Step 3.3: The Transformer
Use Pandas to create the `discounted_price` column.

### Step 3.4: The Agent Stress Test
Run the `agent_simulation.py` with your `processed_data.csv`.

## 4. Conclusion
You've just built a production-ready (mini) data pipeline!
