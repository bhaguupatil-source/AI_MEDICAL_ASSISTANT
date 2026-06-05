from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def medical_chat(question):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="text-embedding-004",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [d.page_content for d in docs]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content