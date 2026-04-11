# Q&A Guide: Lab Session (Afternoon)

### Common Student Issues

**Issue 1: "My script crashes because of the 'ten dollars' string in price."**
- **Teacher Tip**: "This is the point of the lab! Emphasize that they need `try-except` blocks or `pd.to_numeric(..., errors='coerce')` in their validation step."

**Issue 2: "Is it okay if I just delete the bad data? Shouldn't I fix it?"**
- **Teacher Tip**: "In a real pipeline, fixing is better, but sometimes you don't know *how* to fix it. Deleting (Dropping) is safer than letting garbage reach the Agent. Today, we focus on 'Dropping' to protect the Agent."

**Issue 3: "The AI Agent still gives an answer for the Garbage data, but it's weird."**
- **Teacher Tip**: "This is **Hallucination**. Explain that when provided with conflicting info (ID 1 is both a Laptop and a Banana), the LLM might try to combine them into a 'Laptop Banana'. This is why Observability is a safety feature."

---

### Pro-tips for Topic 02
- **Environment Agnostic**: Remind students that `os.path.join` is better than hardcoded slashes `/` if they are on diverse OS.
- **The "Billion-Dollar Mistake"**: Share a story of a company that lost money because of a simple data type error in their pipeline.
