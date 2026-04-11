# Q&A Guide & Narrative (Morning Session)

## Roleplay Concept
*Teacher, use this as your "cheat sheet" during the lecture. Remember, students are "vibe coders" — avoid over-complicating with deep math, focus on the "Why" and "What happens if we don't do this".*

### Key Narrative: The "Digestive System" Metaphor
- **Ingestion** = Ăn vào.
- **Processing** = Tiêu hóa/Chuyển hóa.
- **Observability** = Health Check/Đi khám bác sĩ định kỳ.
- **AI Agent** = Bộ não (Cần năng lượng sạch để suy nghĩ đúng).

---

### Potential Student Questions & Guru Answers

**Q1: "Tại sao không dùng luôn Python script đơn giản cho nhanh, học chi mấy cái tool như Airbyte hay dbt?"**
- **Guru Answer**: "Script đơn giản chạy tốt cho 1 nguồn. Nhưng khi em có 50 nguồn, 50 schema khác nhau, cái script đó sẽ trở thành cơn ác mộng để bảo trì. Tool giúp em có 'Standard' và tiết kiệm hàng trăm giờ sửa code khi API bên thứ 3 thay đổi."

**Q2: "Em dùng LLM mạnh nhất (GPT-4o/Gemini 1.5 Pro) rồi, dữ liệu hơi nhiễu một chút chắc nó vẫn xử lý được chứ?"**
- **Guru Answer**: "LLM rất thông minh nhưng nó cũng rất giỏi... bịa (Hallucination). Nếu dữ liệu đầu vào sai, nó sẽ bịa ra một câu trả lời trông rất thật nhưng hoàn toàn vô giá trị. Đó là định nghĩa của 'Garbage In, Professional Garbage Out'."

**Q3: "Làm sao biết pipeline đang bị 'bệnh' (Data Drift)?"**
- **Guru Answer**: "Dùng Observability metrics. Ví dụ: Bình thường mỗi ngày có 10,000 khách hàng mới, hôm nay bỗng dưng chỉ có 10 người. Code không crash, nhưng data có vấn đề. Đó là lúc chúng ta cần Volume monitoring."

---

### Pro-tips for Topic 01
- **Focus on Reliability**: 150 students need to understand that "working once" is not "working at scale".
- **Visual Aids**: Use a live dashboard if possible or screenshots of broken data vs. clean data.
