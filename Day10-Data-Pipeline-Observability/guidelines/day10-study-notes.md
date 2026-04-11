# Day 10 Study Notes: Data Pipeline & Observability

## 1. Key Terminology
- **Pipeline**: The automated journey of data from source to AI.
- **CDC (Change Data Capture)**: Monitoring database logs to capture changes instantly.
- **Data Drift**: When the statistical properties of your input data change over time, making your AI less accurate.
- **ETL (Extract, Transform, Load)**: Pre-processing data before it hits the warehouse. Essential for Privacy (PII).
- **ELT (Extract, Load, Transform)**: Loading raw data first. Modern standard for Cloud Data Warehouses (BigQuery/Snowflake).

## 2. Framework: The 5 Pillars of Observability
Is your data healthy?
1. **Freshness**: Is the data up to date?
2. **Volume**: Is any data missing from the batch?
3. **Distribution**: Are the values within expected ranges?
4. **Schema**: Has a column name or type changed?
5. **Lineage**: Source-to-sink mapping.

## 3. Best Practices for AI Agents
- **Validation Layers**: Always check data types before feeding them to a RAG system.
- **Fail Fast**: Stop the pipeline if the quality score is below a threshold. Better no data than wrong data.
- **Rate Limit Handling**: AI Agents call many APIs. Implement retries with backoff.

## 4. Summary for the Exam
> "Data quality is not a one-time task; it is a continuous pipeline of observability. A guru builder protects the Agent from the Garbage."

---
*Reference: VinUni Day 10 Guideline PDF.*
