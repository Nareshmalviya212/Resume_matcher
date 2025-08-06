# # main.py

# import streamlit as st
# from resume_utils import process_resumes_from_paths
# from jd_utils import extract_jd_text_from_pdf
# import tempfile
# import os

# st.set_page_config(page_title="AI Resume Matcher", layout="wide")
# st.title("📄 Resume & JD Extractor (Text-Based PDFs Only)")

# # --- Resume Upload ---
# st.subheader("1️⃣ Upload Candidate Resumes")
# resume_files = st.file_uploader("Upload multiple resumes (PDF only)", type=["pdf"], accept_multiple_files=True)

# parsed_resumes = []

# if resume_files:
#     st.info(f"Uploaded {len(resume_files)} resume(s).")
#     temp_resume_paths = []
    
#     # Save temp copies because resume_utils expects file paths
#     for file in resume_files:
#         temp_path = os.path.join(tempfile.gettempdir(), file.name)
#         with open(temp_path, "wb") as f:
#             f.write(file.read())
#         temp_resume_paths.append(temp_path)

#     parsed_resumes = process_resumes_from_paths(temp_resume_paths)

#     if parsed_resumes:
#         st.success(f"✅ Extracted text from {len(parsed_resumes)} resume(s).")
#         for resume in parsed_resumes:
#             with st.expander(resume["filename"]):
#                 st.text_area("Resume Text", resume["content"], height=300)

# # --- JD Upload ---
# st.subheader("2️⃣ Upload Job Description (PDF)")
# jd_file = st.file_uploader("Upload Job Description", type=["pdf"], key="jd")

# if jd_file:
#     jd_temp_path = os.path.join(tempfile.gettempdir(), jd_file.name)
#     with open(jd_temp_path, "wb") as f:
#         f.write(jd_file.read())

#     jd_text = extract_jd_text_from_pdf(jd_temp_path)

#     if jd_text:
#         st.success("✅ Job Description text extracted successfully.")
#         st.text_area("📄 Job Description Text", jd_text, height=300)
#         st.session_state["jd_text"] = jd_text
#     else:
#         st.warning("⚠️ No text found in the uploaded JD PDF.")

# # Store extracted results in session_state (optional for use later)
# if parsed_resumes:
#     st.session_state["resumes"] = parsed_resumes

# app.py

# import streamlit as st
# from jd_utils import extract_jd_text_from_pdf
# from resume_utils import process_resumes_from_paths
# from matcher import rank_resumes_with_llm

# st.set_page_config(page_title="GenAI Resume Matcher", layout="wide")

# st.title("📄 GenAI Resume Matcher")
# st.markdown("Upload a Job Description and at least 10 resumes. The app will rank the top 3 candidates using LLM-powered analysis.")

# # --- Upload JD ---
# st.header("📌 Upload Job Description (PDF)")
# jd_file = st.file_uploader("Upload JD PDF", type=["pdf"], key="jd")

# # --- Upload Resumes ---
# st.header("📌 Upload Resumes (Minimum 10 PDFs)")
# resume_files = st.file_uploader("Upload multiple resumes", type=["pdf"], accept_multiple_files=True, key="resumes")

# if jd_file and resume_files:
#     if len(resume_files) < 10:
#         st.warning("⚠️ Please upload at least 10 resumes.")
#     else:
#         # Extract JD Text
#         st.subheader("📄 Extracting Job Description...")
#         jd_text = extract_jd_text_from_pdf(jd_file)
#         st.text_area("Job Description Preview", jd_text[:2000], height=200)

#         # Extract Resume Texts
#         st.subheader("📄 Extracting Resume Texts...")
#         resumes = process_resumes_from_paths(resume_files)
#         st.success(f"✅ {len(resumes)} resumes processed.")

#         # Show preview
#         with st.expander("🔍 Preview Resumes"):
#             for r in resumes:
#                 st.markdown(f"**{r['filename']}**")
#                 #st.text_area("", r["content"][:1000], height=200)
#                 st.text_area("", r["content"][:1000], height=200, key=r["filename"])


#         # Match & Rank
#         if st.button("🚀 Match & Rank Top 3 Candidates"):
#             with st.spinner("Calling LLM to rank candidates..."):
#                 response = rank_resumes_with_llm(jd_text, resumes, top_n=10)
#             st.subheader("🏆 Top 3 Candidates (LLM Ranking)")
#             st.text(response)

# else:
#     st.info("👆 Please upload both JD and 10+ resume PDFs to continue.")
import streamlit as st
from dotenv import load_dotenv
from jd_utils import extract_jd_text_from_pdf
from resume_utils import process_resumes_from_paths
from matcher import rank_resumes_with_llm
from chatbot import query_candidates_with_llm

load_dotenv()

st.set_page_config(page_title="GenAI Resume Matcher", layout="wide")
st.title("📄 GenAI Resume Matcher")
st.markdown("Upload a Job Description and at least 10 resumes. The app will rank the top 3 candidates using LLM-powered analysis, and allow chatbot-based querying.")

# --- Upload JD ---
st.header("📌 Upload Job Description (PDF)")
jd_file = st.file_uploader("Upload JD PDF", type=["pdf"], key="jd")

# --- Upload Resumes ---
st.header("📌 Upload Resumes (Minimum 10 PDFs)")
resume_files = st.file_uploader("Upload multiple resumes", type=["pdf"], accept_multiple_files=True, key="resumes")

if jd_file and resume_files:
    if len(resume_files) < 10:
        st.warning("⚠️ Please upload at least 10 resumes.")
    else:
        # Extract JD Text
        st.subheader("📄 Extracting Job Description...")
        jd_text = extract_jd_text_from_pdf(jd_file)
        st.text_area("Job Description Preview", jd_text[:2000], height=200)

        # Extract Resume Texts
        st.subheader("📄 Extracting Resume Texts...")
        resumes = process_resumes_from_paths(resume_files)
        st.success(f"✅ {len(resumes)} resumes processed.")

        # Show preview
        with st.expander("🔍 Preview Resumes"):
            for i, r in enumerate(resumes):
                st.markdown(f"**{r['filename']}**")
                st.text_area("", r["content"][:1000], height=200, key=f"{r['filename']}_{i}")

        # Match & Rank
        if st.button("🚀 Match & Rank Top 3 Candidates"):
            with st.spinner("Calling LLM to rank candidates..."):
                response = rank_resumes_with_llm(jd_text, resumes, top_n=10)
            st.subheader("🏆 Top 3 Candidates (LLM Ranking)")
            if response:
                st.text(response)
            else:
                st.warning("⚠️ No response received from LLM. Please check API key, model or try again.")

        # --- Chatbot Section ---
        st.divider()
        st.header("💬 Chatbot: Ask About Candidates")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_query = st.chat_input("Ask about candidates...")

        if user_query:
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.markdown(user_query)

            with st.chat_message("assistant"):
                with st.spinner("Searching candidates..."):
                    reply = query_candidates_with_llm(user_query, resumes)
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})

else:
    st.info("👆 Please upload both JD and 10+ resume PDFs to continue.")
