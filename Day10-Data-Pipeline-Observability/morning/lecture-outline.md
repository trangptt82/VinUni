# Lecture Outline: Data Pipeline & Data Observability
## Topic 01: "Xây dựng hệ tiêu hóa cho AI"

### 1. Introduction (15 mins)
- **The "Vibe Coder" Trap**: Why "just calling an API" isn't enough for scale.
- **The Core Thesis**: AI response quality is 80% data quality, 20% prompt engineering.
- **Visualizing the Stack**: 
    - Source (ERP/Web/DB) -> Extraction -> Processing -> Storage -> AI Agent.

### 2. The AI Data Stack (45 mins)
- **Data Sources**: 
    - Structured (SQL) vs. Unstructured (PDF/Markdown).
    - Real-time (CDC) vs. Static (Snapshots).
- **Ingestion Tools**: 
    - When to use Airbyte/Fivetran vs. Custom Python scripts.
    - Rate limiting and API handling (Preventing "429 Too Many Requests").
- **Mini-Quiz 01**: Ingestion Basics.

### 3. ETL vs ELT — Cuộc chiến trong mây (45 mins)
- **ETL (Extract-Transform-Load)**: Data privacy first. Masking PII before it hits the cloud.
- **ELT (Extract-Load-Transform)**: Warehouse power. Using dbt and BigQuery for massive scale.
- **Batch vs. Streaming**:
    - "Dữ liệu nguội" (Batch) vs. "Dữ liệu nóng" (Streaming).
    - Which one does your RAG need?
- **Mini-Quiz 02**: Architecting the flow.

### 4. Data Observability — Chụp X-quang cho dữ liệu (60 mins)
- **Why Pipelines Break**: Schema changes, upstream API failures, silent data drift.
- **The 5 Pillars of Observability**:
    1. **Freshness**: Dữ liệu có mới không?
    2. **Distribution**: Dữ liệu có bị lệch không (Drift)?
    3. **Volume**: Dữ liệu có bị "mất tích" không?
    4. **Schema**: Cấu trúc có bị đổi không?
    5. **Lineage**: Dữ liệu này đến từ đâu?
- **Garbage In, BUT NOT Out**: Implementing "Data Contracts" and validation layers.

### 5. Q&A and Morning Wrap-up (15 mins)
- Transitioning from "Theory" (Morning) to "Hands-on" (Afternoon).
- Preparing the environment for the Lab.
