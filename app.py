import streamlit as st

from src.predictor import predict_disease
from src.chatbot import medical_chat

st.title("AI Medical Assistant")

st.subheader("Disease Prediction")

fever = st.selectbox("Fever",[0,1])
cough = st.selectbox("Cough",[0,1])
headache = st.selectbox("Headache",[0,1])
fatigue = st.selectbox("Fatigue",[0,1])

if st.button("Predict"):

    symptoms = [
        fever,
        cough,
        headache,
        fatigue
    ]

    result = predict_disease(
        symptoms
    )

    st.success(
        f"Disease: {result}"
    )

st.subheader("Medical Chatbot")

question = st.text_input(
    "Ask Medical Question"
)

if st.button("Ask"):

    answer = medical_chat(
        question
    )

    st.write(answer)