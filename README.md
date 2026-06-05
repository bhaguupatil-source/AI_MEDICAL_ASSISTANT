# 🩺 AI Medical Assistant

AI Medical Assistant is an intelligent healthcare application that combines Machine Learning, NLP, Retrieval-Augmented Generation (RAG), Vector Databases, and Large Language Models (LLMs) to predict diseases from symptoms and provide accurate medical information through an AI-powered chatbot. The system uses medical datasets for disease prediction and medical PDFs as a knowledge base for question answering.

## 🚀 Features
- Disease prediction based on symptoms
- AI-powered medical chatbot
- Retrieval-Augmented Generation (RAG)
- Medical PDF knowledge base
- FAISS vector database for semantic search
- Gemini LLM integration
- Streamlit web interface
- Interactive and user-friendly dashboard

## 🏗️ Project Structure

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
│   └── disease_model.pkl
│
├── vectorstore/
│   └── faiss_index
│
└── src/
    ├── train_model.py
    ├── predictor.py
    ├── create_vectorstore.py
    └── rag_chatbot.py

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- LangChain
- Google Gemini
- FAISS
- PyPDF
- Sentence Transformers
- RAG Architecture

## ⚙️ Installation

### Clone Repository
```bash
git clone https://github.com/yourusername/AI_MEDICAL_ASSISTANT.git
cd AI_MEDICAL_ASSISTANT
```

### Create Virtual Environment
```bash
python -m venv .venv
```

### Activate Environment

Windows:
```bash
.venv\Scripts\activate
```

Linux/Mac:
```bash
source .venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Configure API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

## 📊 Train Disease Prediction Model

```bash
python src/train_model.py
```

The trained model will be saved inside the `models` folder.

## 📚 Create Vector Database

```bash
python src/create_vectorstore.py
```

This will process medical PDFs and create a FAISS vector database.

## ▶️ Run Application

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

## 🔄 Workflow

User Symptoms → Disease Prediction Model → Predicted Disease → Vector Search (FAISS) → Relevant Medical Context → Gemini LLM → AI Response

## 💬 Example Queries

- What are the symptoms of diabetes?
- What causes asthma?
- How can hypertension be controlled?
- Explain dengue fever.
- What precautions should be taken for COVID-19?

## 📦 Requirements

- streamlit
- pandas
- numpy
- scikit-learn
- joblib
- langchain
- langchain-community
- langchain-google-genai
- faiss-cpu
- pypdf
- sentence-transformers
- python-dotenv
- google-generativeai

## ⚠️ Disclaimer

This project is developed for educational and research purposes only. It should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.

## 👩‍💻 Author

**Bhagyashri Patil**

AI | Data Science | Machine Learning | Deep Learning | Generative AI

## ⭐ Future Enhancements
- Voice-enabled medical assistant
- Medical image analysis
- Multi-language support
- Patient history tracking
- Cloud deployment (AWS/Azure/GCP)
- Drug recommendation system

If you find this project useful, consider giving it a ⭐ on GitHub.
