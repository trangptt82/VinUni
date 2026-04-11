# Proposed Day 10 Repository Structure

Following your instruction to act as your teaching assistant, I have designed a repository-style structure for **Day 10: Data Pipeline & Data Observability**. This structure ensures clarity for both you (as the teacher) and the 150 students (especially the "vibe coders").

## Root Directory Plan: `Day10-Data-Everything/`

### 1. High-Level Overview
- `README.md`: The "Command Center" for Day 10.
    - Full-day time schedule (09:00 - 16:30).
    - Narrative connecting Morning (Theory) to Afternoon (Lab).
    - Learning objectives and Prerequisites.

### 2. Morning Session: Theory & Concepts (3 Hours)
`morning/`
- `lecture-outline.md`: Detailed breakdown of Data Pipeline & Observability concepts.
- `quizzes/`: Mini-quizzes (5-10 mins) to check understanding.
    - `quiz-01-fundamental.md`: Pipeline basics.
    - `quiz-02-observability.md`: "Garbage in → Garbage out" specifics.
- `qa-theory.md`: Frequently asked questions and "Pro-tips" for the teacher.

### 3. Afternoon Session: Hands-on & Lab (3 Hours)
`afternoon/`
- `lab-outline.md`: Detailed roadmap for the Afternoon session.
- `exercise-etl-automation/`: Topic 02 focus.
    - `problem-statement.md`: Narrative and task description.
    - `starter-code/`: Environment-agnostic Python/Bash scripts.
    - `solution-code/`: Completed automation scripts with verbose comments for "vibe coders".
    - `explanation-guide.md`: Step-by-step breakdown of the solution logic.
- `data-quality-agent-lab/`: Investigating quality impact on AI Agents.
    - `agent-setup.py`: Minimalist agent implementation.
    - `bad-data-simulation.py`: Simulation of quality issues.
- `grading/`:
    - `rubric.md`: Clear criteria for assessment.
    - `autoscore-script/`: (Optional) Simple script to help grade student submissions.

### 4. Logistics & Integration
`logistics/`
- `github-repo-setup.md`: Instructions for setting up the student workspace.
- `codelab-guide.md`: Google Codelab tutorial format for the hands-on session.
- `env-setup/`: Docker or light setup scripts to handle varying student environments.

### 5. Reference Guideline
`guidelines/`
- `day10-study-notes.md`: Summary derived from the `.pdf` guideline.

---

## Next Steps
Once you approve this structure, I will:
1.  Analyze the `.pdf` guideline in detail.
2.  Start generating the `README.md` and the Morning lecture outline as the first concrete deliverables.

**Teacher, please review this structure and let me know if you want to add, remove, or rename any components.**
