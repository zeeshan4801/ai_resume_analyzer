import os
import json
from dotenv import load_dotenv
from groq import Groq
from prompts import ANALYSIS_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text, job_description):
    prompt = ANALYSIS_PROMPT.format(
        resume=resume_text,
        job_description=job_description
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "ats_keywords": [],
            "problems": ["AI response was not valid JSON"],
            "recommendations": [content],
            "final_result": "Please try again."
        }