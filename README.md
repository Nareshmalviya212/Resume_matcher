# 🧠 GenAI Resume Matcher with Chatbot Interface

A smart, modular application that uses Generative AI techniques to match candidate resumes with a job description (JD) and allows users to interact with the data using a chatbot.

Built using **Python**, **Streamlit**, **Groq LLM**, and **HuggingFace Embeddings**.

---

## 📦 Features

- ✅ Upload and extract text from resumes (PDF)
- ✅ Upload job description (PDF)
- ✅ NLP-based filtering using sentence embeddings
- ✅ Groq LLM-powered ranking of top 3 most relevant candidates
- ✅ Interactive chatbot to query candidates (e.g., "Who knows Python?")
- ✅ Modular structure with separate utility files
- ✅ Robust error handling for file processing and LLM failures
- ✅ Clearly indicates upload and processing status

---

## 🧰 Tech Stack

| Tool                       | Purpose                                                   |
| -------------------------- | --------------------------------------------------------- |
| **Streamlit**              | Web Interface (i didn't worked on django and flask mostly) |
| **Groq LLM (LLaMA 3)**     | Resume ranking & chatbot                                  |
| **HuggingFace Embeddings** | Semantic similarity (MiniLM model)                        |
| **pdfplumber**             | PDF text extraction                                       |
| **Python-dotenv**          | Environment variable management                           |

---
## 📁 Project Structure


---

## 🚀 How It Works

### Step 1: Upload Files
- Upload **Job Description (PDF)**
- Upload **Minimum 10 Resumes (PDF)**
- Shows upload and processing status clearly

### Step 2: Extract Text
- Uses `pdfplumber` to extract readable text from PDFs
- Logs and handles errors (e.g., empty or corrupted PDFs)

### Step 3: Match Candidates
- Embeds JD and all resumes using HuggingFace model
- Computes cosine similarity for basic ranking
- Sends top 10 resumes to Groq LLM to deeply evaluate skill/experience match
- Ranks and displays top 3 best-fit candidates

### Step 4: Chatbot Interface
- Ask questions like:
  - "List candidates who know Python"
  - "Who has experience with Django?"
  - "Any resume with NLP and TensorFlow?"
- LLM scans resume data and responds conversationally with structured or natural replies

---

## 💬 Sample Chatbot Prompts

> "Who has more than 2 years of experience with Python?"

> "Anyone worked on NLP projects?"

> "Which candidates used TensorFlow or PyTorch?"

---

## ✅ Dependencies (requirements.txt)

```txt
streamlit
openai==0.28
pdfplumber
sentence-transformers
scikit-learn
python-dotenv
