# VinUni: Google Codelab Setup & Authoring Guide

This guide is designed for teachers and instructors at VinUni to help them transition their lecture materials and labs into a structured, interactive format using **Google Codelabs**.

---

## 1. Prerequisites (The Teacher's Toolkit)

Before you begin, ensure your development environment is set up with the following tools:

### A. Install Go
The `claat` tool is built using the Go programming language.
1. Download Go for macOS (ARM64) from [golang.org](https://go.dev/dl/).
2. Run the installer and follow the prompts.
3. Verify the installation:
   ```bash
   go version
   ```

### B. Install the `claat` Tool
`claat` (Codelabs as a Thing) is the command-line tool used to convert Markdown into the interactive Codelab format.
```bash
go install github.com/googlecodelabs/tools/claat@latest
```
*Tip: Ensure your `$GOPATH/bin` is in your system `PATH`.*

---

## 2. The Authoring Workflow

The lifecycle of a Codelab follows a simple three-step process:

1.  **Drafting (Markdown)**: Write your lab instructions in a standard Markdown (`.md`) file using the specific metadata header.
2.  **Conversion (Claat)**: Run the `claat` export command to generate the HTML files.
3.  **Deployment**: Upload the generated files to a static host (like GitHub Pages).

---

## 3. Codelab Syntax Cheat Sheet

Google Codelabs use standard Markdown with a few special conventions.

### Metadata Header
Every Codelab file MUST start with a metadata header.
```markdown
---
id: day-10-data-observability
summary: Learn the principles of Data Pipeline Observability and Data Quality.
authors: VinUni Guru
categories: Data Science, AI
status: Published
feedback link: https://github.com/appsheetway/VinUni/issues
---
```

### Steps & Durations
Each `##` header starts a new step in the Codelab.
```markdown
## 1. Introduction
Duration: 0:02:00

Welcome to the lab!
```

### Info Boxes (Asides)
Use these to highlight tips or warnings for students.
```markdown
> aside positive
> **Pro Tip**: Use `pd.to_numeric` with `errors='coerce'` to handle messy pricing data.

> aside negative
> **Warning**: Never let "Garbage Data" reach your AI Agent, as it will cause hallucinations.
```

---

## 4. Example: Day 10 Transformation

To see this in action, check out the source file for our Day 10 lab:
`codelabs/day10-data-observability.md`

### How we converted it:
- **Theory (Morning)**: Integrated into the "Introduction" and "Key Concepts" steps.
- **Lab (Afternoon)**: Broken down into "Step-by-step" implementation tasks.
- **Code**: Embedded as distinct code blocks with syntax highlighting.

---

## 5. Deployment Guide (GitHub Pages)

To make your labs accessible to students:
1. Generate the lab: `claat export codelabs/day10-data-observability.md`
2. This creates a directory named `day-10-data-observability`.
3. Push this directory to your `main` branch.
4. Go to **Settings > Pages** on GitHub and set the source to your `main` branch.
5. Your lab will be live at `https://appsheetway.github.io/VinUni/day-10-data-observability`.

---

## 6. Local Testing & Verification

Before sharing a lab with the entire class or teammate, it is highly recommended to run a local test to verify the flow and formatting.

### Step-by-Step Local Test:

1.  **Export the Codelab**:
    ```bash
    claat export codelabs/day10-data-observability.md
    ```
2.  **Start the Local Server**:
    ```bash
    claat serve
    ```
3.  **View in Browser**:
    The command will provide a local address (usually `http://localhost:9090`). Open this in your browser to see the interactive lab.

### Feedback for Team Members:
If you are asking a teammate to test your lab, ensure they have **Go** and **Claat** installed (see Section 1). They can then pull your latest changes and run the local test steps above.
