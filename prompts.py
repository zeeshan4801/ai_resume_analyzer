ANALYSIS_PROMPT = """
You are an expert ATS resume analyzer.

Compare the resume with the job description.

Return ONLY valid JSON.

Required format:

{{
"match_score": number,
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
