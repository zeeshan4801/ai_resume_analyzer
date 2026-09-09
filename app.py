import streamlit as st
from resume_parser import extract_text_from_file
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description using AI.")

resume_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):
    if not resume_file or not job_description.strip():
        st.warning("Please upload a resume and enter a job description.")
    else:
        with st.spinner("Analyzing resume..."):
            resume_text = extract_text_from_file(resume_file)
            result = analyze_resume(resume_text, job_description)

        st.success("Analysis Completed")

        st.subheader("Match Score")
        st.metric("Resume Match", f"{result.get('match_score', 0)}%")

        sections = [
            "matching_skills",
            "missing_skills",
            "ats_keywords",
            "problems",
            "recommendations",
            "final_result"
        ]

        for section in sections:
            st.subheader(section.replace("_", " ").title())
            value = result.get(section, [])
            if isinstance(value, list):
                for item in value:
                    st.write(f"- {item}")
            else:
                st.write(value)