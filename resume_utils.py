# # resume_utils.py

# import pdfplumber
# import os

# def extract_resume_text_from_path(file_path):
#     try:
#         with pdfplumber.open(file_path) as pdf:
#             full_text = ''
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     full_text += text + '\n'
#         return full_text.strip()
#     except Exception as e:
#         print(f"[ERROR] Failed to extract from {file_path}: {e}")
#         return ''

# def process_resumes_from_paths(file_paths):
#     parsed = []

#     if isinstance(file_paths, str):
#         file_paths = [file_paths]

#     for path in file_paths:
#         try:
#             text = extract_resume_text_from_path(path)
#             if text:
#                 parsed.append({
#                     "filename": os.path.basename(path),
#                     "content": text
#                 })
#         except Exception as e:
#             print(f"[ERROR] Cannot process {path}: {e}")

#     return parsed
# resume_utils.py

import pdfplumber

def extract_resume_text(file):
    """
    Extract text from a single resume file (UploadedFile or file path).
    """
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text.strip()
    except Exception as e:
        print(f"[ERROR] Failed to process file: {file} | {e}")
        return ""

def process_resumes_from_paths(uploaded_files):
    """
    Takes a list of Streamlit UploadedFile objects.
    Returns a list of dicts: [{filename, content}, ...]
    """
    parsed = []
    for file in uploaded_files:
        text = extract_resume_text(file)
        if text:
            parsed.append({
                "filename": file.name,
                "content": text
            })
    return parsed
