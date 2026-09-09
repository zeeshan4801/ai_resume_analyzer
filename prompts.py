ANALYSIS_PROMPT = """
You are an expert ATS resume analyzer.

Analyze the resume against the job description.

Return ONLY valid JSON.
Do not add markdown.
Do not add explanations outside JSON.

JSON format:

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "ats_keywords": {{
        "found": [],
        "missing": []
    }},
    "problems": [],
    "recommendations": [],
    "final_result": ""
}}

Resume:

{resume}

Job Description:

{job_description}
"""
