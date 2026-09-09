# AI Resume Analyzer

An AI application that compares a resume with a job description.

## Features

- PDF and DOCX resume extraction
- AI-powered resume analysis
- Match score
- Matching skills
- Missing skills
- ATS keyword analysis
- Resume problems
- Recommendations

## Project Structure

```
app.py
analyzer.py
resume_parser.py
prompts.py
requirements.txt
.env.example
.gitignore
README.md
```

## Setup

Create environment:

```
python -m venv venv
```

Activate:

Windows:
```
venv\\Scripts\\activate
```

Linux/Mac:
```
source venv/bin/activate
```

Install packages:

```
pip install -r requirements.txt
```

Create `.env`

Copy:

```
.env.example
```

Rename it:

```
.env
```

Add your Groq API key.

## Run

```
streamlit run app.py
```

## Workflow

User Resume
→ Resume Parser
→ Job Description Analysis
→ Groq AI Comparison
→ JSON Result
→ Streamlit Report