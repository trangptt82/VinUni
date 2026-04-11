# Day 10 Mini-Quizzes (Check your understanding)

---

## Quiz 01: Ingestion & Sources
**Question:** Bạn đang xây dựng một chatbot hỗ trợ khách hàng cho VinFast. Hệ thống cần lấy thông tin bảo hành từ một cơ sở dữ liệu PostgreSQL cũ (Legacy) và thông tin review từ social media qua API.
1. **Phương pháp nào tối ưu nhất để lấy dữ liệu từ PostgreSQL mà không làm quá tải hệ thống đang chạy?**
    - A) `SELECT *` toàn bộ bảng mỗi 10 phút.
    - B) Sử dụng **CDC (Change Data Capture)** để chỉ lấy những dòng thay đổi.
    - C) Copy file CSV thủ công mỗi ngày.
2. **Nếu API của social media giới hạn 100 requests/phút, bạn sẽ làm gì để pipeline không bị chết?**
    - (Trả lời ngắn gọn: .....................................................)

---

## Quiz 02: ETL vs ELT
**Question:** Bạn làm việc cho Vinmec. Dữ liệu bệnh nhân chứa thông tin nhạy cảm (Tên, Số điện thoại). Bạn muốn đẩy dữ liệu này lên một Cloud Data Warehouse để phân tích.
1. **Bạn nên chọn ETL hay ELT? Vì sao?**
    - .....................................................................................
2. **Sự khác biệt lớn nhất giữa Batch và Streaming trong ngữ cảnh RAG (Retrieval-Augmented Generation) là gì?**
    - .....................................................................................

---

## Answer Key (For Teacher Only)
- **Quiz 01 - Q1**: B (CDC is the standard for non-intrusive ingestion).
- **Quiz 01 - Q2**: Implementation of Rate Limiting with Exponential Backoff and Queuing.
- **Quiz 02 - Q1**: ETL (To mask/anonymize PII *before* it leaves the local environment).
- **Quiz 02 - Q2**: Latency and Freshness. Streaming allows the Agent to know about events that happened seconds ago; Batch might have a 24-hour delay.
