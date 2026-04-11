# Data Dictionary: Day 10 Master Terms

*Teacher: Use this document to standardize the language used in class. Students should refer to this if they get confused by the technical jargon.*

| Term | Meaning (Eng) | Ý nghĩa (Viet) | Context |
| :--- | :--- | :--- | :--- |
| **Pipeline** | A sequence of data processing steps. | Chuỗi xử lý dữ liệu tự động. | The "pipes" that move data from Source to Agent. |
| **Ingestion** | The process of importing data from sources. | Thu thập/Nạp dữ liệu. | Getting data from PostgreSQL/APIs. |
| **ETL** | Extract, Transform, Load. | Trích xuất, Biến đổi, Nạp. | Traditional pipeline (Transform BEFORE loading). |
| **ELT** | Extract, Load, Transform. | Trích xuất, Nạp, Biến đổi. | Modern cloud pipeline (Transform AFTER loading). |
| **CDC** | Change Data Capture. | Theo dõi thay đổi dữ liệu. | Capturing only changes (Inserts/Updates) in a DB. |
| **Observability** | Tracking the internal state/health of data. | Khả năng quan sát/Theo dõi "sức khỏe" dữ liệu. | Knowing if data is "sick" (garbage) before it breaks the AI. |
| **Data Drift** | Change in data patterns over time. | Sự trôi dạt dữ liệu. | Why AI becomes less accurate over time. |
| **Freshness** | How up-to-date the data is. | Độ tươi mới của dữ liệu. | Is the data from today or 3 years ago? |
| **Validation** | Checking if data meets quality rules. | Kiểm định dữ liệu. | Dropping "garbage" records (e.g., negative prices). |
| **Hallucination** | AI generating confident but false info. | Ảo giác AI. | What happens when AI is fed bad data. |
| **RAG** | Retrieval-Augmented Generation. | Tăng cường tạo lập bằng truy xuất. | The focus of Topic 02: Giving AI access to our clean data store. |
| **Schema** | The structure of a database or file. | Lược đồ/Cấu trúc dữ liệu. | The "Skeleton" of our JSON or CSV files. |
| **DLQ** | Dead Letter Queue. | Hàng chờ dữ liệu lỗi. | Where failed records go for inspection. |
