# # jd_utils.py

# import pdfplumber
# import os

# def extract_jd_text_from_pdf(file_path):
#     if not os.path.isfile(file_path):
#         print(f"[ERROR] File not found: {file_path}")
#         return ''

#     try:
#         with pdfplumber.open(file_path) as pdf:
#             full_text = ''
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     full_text += text + '\n'
#         return full_text.strip()
#     except Exception as e:
#         print(f"[ERROR] Failed to read JD PDF: {e}")
#         return ''
# jd_utils.py

import pdfplumber

def extract_jd_text_from_pdf(file):
    """
    Extract text from a Job Description PDF file (UploadedFile from Streamlit).
    """
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text.strip()
    except Exception as e:
        print(f"[ERROR] Could not extract JD text: {e}")
        return ""
