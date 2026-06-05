# AI_MEDICAL_ASSISTANT

An End-to-End AI Medical Assistant built using Machine Learning, NLP, RAG (Retrieval-Augmented Generation), Gemini LLM, FAISS Vector Database, and Streamlit.

## 📌 Project Overview

This project predicts diseases based on symptoms and answers medical questions using a RAG-powered chatbot.

The system combines:

- Machine Learning for Disease Prediction
- Medical PDF Knowledge Base
- Embeddings and Vector Search
- Gemini Large Language Model
- Streamlit Web Application

---

## 🚀 Features

### Disease Prediction
- Predict diseases from symptoms
- Random Forest Machine Learning Model
- Fast and simple prediction system

### Medical Chatbot
- Ask medical questions
- Uses Retrieval-Augmented Generation (RAG)
- Searches medical PDFs for context
- Generates answers using Gemini

### Knowledge Base
- Medical Books
- Disease Guides
- Custom Medical PDFs

### User Interface
- Streamlit Dashboard
- Real-time predictions
- Interactive chatbot

---

## 📂 Project Structure

```text
AI_MEDICAL_ASSISTANT/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── disease_dataset.csv
│   ├── medical_book.pdf
│   └── disease_guide.pdf
│
├── models/
│   ├── disease_model.pkl
│   └── encoder.pkl
│
├── vectorstore/
│
└── src/
    ├── train_model.py
    ├── predictor.py
    ├── rag.py
    └── chatbot.py

**🛠 Technologies Used**
Python
Pandas
NumPy
Scikit-Learn
LangChain
Google Gemini
FAISS
PyPDF
Streamlit
RAG
⚙ Installation
1. Clone Repository
git clone <your-repository-url>
cd AI_MEDICAL_ASSISTANT
2. Create Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
Linux / Mac
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
📦 requirements.txt
streamlit
pandas
numpy
scikit-learn
joblib
langchain
langchain-community
langchain-google-genai
langchain-text-splitters
faiss-cpu
pypdf
python-dotenv
🔑 Gemini API Setup

Create a .env file in the project root.

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

Get an API key from:

Google AI Studio

📊 Dataset Format
data/disease_dataset.csv
fever,cough,headache,fatigue,disease
1,1,1,1,Flu
1,1,0,1,Cold
0,0,1,1,Migraine
1,0,1,0,Dengue
0,1,0,1,Asthma
🧠 Train Machine Learning Model

Run:

python src/train_model.py

Output:

Model Saved

Generated files:

models/
├── disease_model.pkl
└── encoder.pkl
📚 Create Vector Database

Place PDFs inside:

data/
├── medical_book.pdf
└── disease_guide.pdf

Run:

python src/rag.py

Output:

Vector DB Created Successfully

Generated folder:

vectorstore/
🤖 Run Application

Start Streamlit:

streamlit run app.py

Open:

http://localhost:8501
🔄 Application Workflow
Disease Prediction
Symptoms
    ↓
Feature Selection
    ↓
Random Forest Model
    ↓
Disease Prediction
Medical Chatbot (RAG)
Medical PDFs
      ↓
Document Loader
      ↓
Text Splitter
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Gemini LLM
      ↓
Medical Answer
🖥 Example Usage
Disease Prediction

Input:

Fever = 1
Cough = 1
Headache = 1
Fatigue = 1

Output:

Predicted Disease: Flu
Medical Chatbot

Input:

What are the symptoms of dengue?

Output:

AI-generated response based on medical documents
📈 Future Enhancements
Deep Learning Disease Prediction
Medical Image Analysis
Voice Assistant
Multilingual Support
Patient History Tracking
Doctor Recommendation System
Cloud Deployment
Authentication System
⚠ Disclaimer

This project is intended for educational and research purposes only.

It is not a substitute for professional medical advice, diagnosis, or treatment.

Always consult qualified healthcare professionals for medical decisions.

👨‍💻 Author

Bhagyashri Patil

Data Science | Machine Learning | Generative AI Engineer

⭐ Support

If you found this project useful:

Star the repository
Fork the project
Share with others

Happy Coding! 🚀
