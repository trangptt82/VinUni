# Ngày 10 — Data Pipeline & Data Observability
## "Garbage in → Garbage out — Fix thế nào?"

> AI chạy được chưa phải product. Hôm nay học cách xây dựng "hệ tiêu hóa" (Data Pipeline) khỏe mạnh và cách "khám bệnh" (Observability) cho dữ liệu để AI Agent không bị "ngộ độc".

---

## Tổng quan buổi học

```text
SÁNG — Lecture + Mini Quiz                     CHIỀU — Hands-on Lab + Automation
┌───────────────────────────────┐               ┌───────────────────────────────┐
│ Data Stack cho AI Agent       │               │ Lab 10: ETL Automation        │
│ ETL vs ELT: Chọn phe nào?     │       →       │ Data Quality vs Agent Performance│
│ Observability: Health check   │               │ Grading & Peer Review         │
│ Quiz: "Hệ tiêu hóa" dữ liệu   │               │ Submit to GitHub/LMS          │
└───────────────────────────────┘               └───────────────────────────────┘
```

**SÁNG: Framework & Concepts.** Tại sao Data Pipeline lại là xương sống của AI? Chúng ta sẽ đi từ nguồn dữ liệu (PostgreSQL, APIs) qua các bước biến đổi (Transform) đến khi nuôi dưỡng AI Agent qua RAG/Vector Stores. Học về cách CDC (Change Data Capture) và Observability giúp bạn biết dữ liệu "sai ở đâu" trước khi user phát hiện.

**CHIỀU: Hands-on Practice.** Bạn sẽ tự tay xây dựng một mini-automation pipeline. Thử nghiệm xem khi dữ liệu bị "bẩn" (poisoned/noisy), AI Agent của bạn sẽ cư xử kỳ quặc như thế nào và cách dùng code để chặn đứng "rác" ngay từ cửa ngõ.

---

## Agenda

| Giờ | Hoạt động | Hình thức | Deliverable |
|-----|-----------|-----------|-------------|
| 09:00 | **Opening** — 3 thảm họa dữ liệu & Thesis: "Data is the new code" | Lecture | |
| 09:15 | **Block 1**: The AI Data Stack — Từ Source đến Agent | Theory | [Quiz 1] |
| 10:00 | **Block 2**: ETL vs ELT & Batch vs Streaming | Decision Making | [Quiz 2] |
| 11:00 | **Block 3**: Data Observability — Garbage in, but not out! | Concept | [Case Study] |
| 12:00 | Nghỉ trưa | | |
| 13:30 | **Block 4**: Lab 10 — Xây dựng ETL Automation Pipeline | Hands-on | Code Script |
| 14:30 | **Block 5**: Stress Test — Data Quality vs AI Agent | Practice | Agent Log |
| 15:30 | **Grading** — Peer Review & Solution Walkthrough | Review | |
| 16:00 | **Closing** — Q&A & Ngày 11 Teaser | Q&A | |

---

## Hoạt động chính

### 1. Morning Mini-Quizzes (Cá nhân, 5-10 phút)
Kiểm tra nhanh sự hiểu biết về cách dữ liệu di chuyển trong hệ thống.
**Chi tiết:** [`morning/quizzes/`](morning/quizzes/)

### 2. Lab 10: ETL Automation (Nhóm/Cá nhân)
Viết script Python để tự động hóa việc thu thập và xử lý dữ liệu, có tích hợp Validation checks.
**Starter Code:** [`afternoon/exercise-etl-automation/starter-code/`](afternoon/exercise-etl-automation/starter-code/)

---

## Tài liệu & Công cụ
- **Reference Doc:** [`guidelines/day10-study-notes.md`](guidelines/day10-study-notes.md)
- **Environment:** Google Colab / Local VS Code.
- **Data Source Simulation:** PostgreSQL/JSON mock API.

---

*Ngày 10 — VinUni A20 — AI Thực Chiến · 2026*
