# Lecture Narrative & Slide Content Guide

*Teacher: This is your script for the 3-hour morning session. Each section corresponds to the Lecture Outline.*

---

## Part 1: Opening (15 mins)
**Narrative**: 
"Chào các bạn! Hôm nay chúng ta sẽ nói về một chủ đề mà thường bị bỏ qua nhưng lại là thứ quyết định 80% sự thành bại của một AI Product: **Data Pipeline**. 

Các bạn đã quen với việc gọi API của GPT-4 hay Gemini. Nhưng hãy tưởng tượng bạn đang xây dựng một chatbot cho Vinmec. Nếu chatbot đó đọc nhầm lịch sử bệnh án vì dữ liệu bị lỗi, hậu quả sẽ ra sao? 'Garbage in, Garbage out' không chỉ là một câu nói đùa, nó là rủi ro tỷ đô trong thực tế."

**Slide Content**:
- Title: AI data is like a Digestive System.
- Image: A brain (AI) being fed by a series of pipes.
- Bullet points:
    - AI ≠ Model only.
    - AI = Model + **Vibrant Data**.
    - Garbage in -> Professional Garbage out.

---

## Part 2: The AI Data Stack (45 mins)
**Narrative**: 
"Hãy nhìn vào 'Hệ tiêu hóa' của chúng ta. Dữ liệu bắt đầu từ đâu? Từ App, từ Website, từ cơ sở dữ liệu như PostgreSQL. 

Nếu chúng ta copy-paste bằng tay (Vibe coding style), chúng ta sẽ chết khi hệ thống scale lên 150 triệu bản ghi. Chúng ta cần Automation. Chúng ta cần những công cụ như Airbyte để 'hút' dữ liệu một cách thông minh mà không làm sập Server nguồn (đó là CDC)."

**Slide Content**:
- Diagram: [Source DB/API] -> [Ingestion Pipe] -> [Warehouse] -> [RAG Agent].
- Key Terms: Ingestion, CDC, Rate Limiting.
- "Pro-Tip": Don't scan the whole DB, just capture the changes!

---

## Part 3: ETL vs ELT (45 mins)
**Narrative**: 
"Ở Vinmec, bạn không được phép đẩy tên bệnh nhân lên Cloud khi chưa che giấu thông tin (Anonymization). Đó là lúc bạn cần **ETL**. Bạn biến đổi dữ liệu TRƯỚC khi nạp vào kho. 

Nhưng nếu bạn ở VinFast và có hàng tỷ sensor data, bạn nạp hết chúng vào BigQuery rồi mới dùng dbt để biến đổi sau. Đó là **ELT**. Khác biệt duy nhất là: Bạn biến hóa ở đâu?"

**Slide Content**:
- Table: ETL vs ELT comparison.
- Graphic: Masking "Nguyen Van A" to "N******" (ETL Example).
- Tool logos: Airbyte (ELT), Custom Python (ETL).

---

## Part 4: Data Observability (60 mins)
**Narrative**: 
"Làm sao bạn biết nước bạn đang uống là nước sạch? Bạn cần test định kỳ. Dữ liệu cũng vậy. 

**Observability** là cách chúng ta 'khám bệnh' cho dữ liệu. Nếu bỗng nhiên một cột 'Price' vốn là con số lại trở thành 'Ten dollars' (text), hệ thống của bạn sẽ crash. Chúng ta cần 5 trụ cột để quan sát: Freshness, Volume, Distribution, Schema, và Lineage."

**Slide Content**:
- The 5 Pillars Diagram (Hexagon shape).
- "Data Drift" visualization (A chart where two lines start to separate).
- Question: "Is your data alive or dead today?"

---

## Part 5: Q&A & Wrap-up
**Narrative**: 
"Sáng nay chúng ta đã học về lý thuyết 'Hệ tiêu hóa'. Chiều nay, chúng ta sẽ bắt tay vào xây dựng nó. Các bạn hãy chuẩn bị tinh thần để xử lý những mớ dữ liệu cực kỳ 'bẩn' mà tôi đã chuẩn bị sẵn!"

**Slide Content**:
- Summary of Morning Session.
- Teaser for Lab 10: "Can your Agent survive the Garbage?"
