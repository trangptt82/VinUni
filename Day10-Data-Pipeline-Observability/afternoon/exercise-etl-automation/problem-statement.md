# Exercise: Build Your First Automated ETL Pipeline

## Context
You are a Data Engineer at a leading E-commerce site. Your AI team needs a clean data source to feed their "Shopping Assistant" agent. Currently, the source data is messy and comes from an external API in JSON format.

## Objective
Write a Python script that:
1.  **Extracts** data from the provided JSON file (or mock URL).
2.  **Validates** the data:
    - ID must be unique.
    - Price must be greater than 0.
    - Product Category must not be empty.
3.  **Transforms** the data:
    - Standardize category names (e.g., "elec" -> "Electronics").
    - Calculate a `discounted_price` (10% off).
4.  **Loads** the data into a clean `processed_data.csv`.

---

## Level 1: The "Happy Path"
- Get the script running such that it moves 100% of the data.

## Level 2: The "Observability" Path (Guru Challenge)
- Implement a logging system that tells you:
    - How many records were processed.
    - How many records failed validation (and why).
    - Time taken for the whole operation.

---

## Submission
- `MaHocVien-Day10-ETL.py`
- `processed_data.csv`
- A screenshot of your terminal/log output.
