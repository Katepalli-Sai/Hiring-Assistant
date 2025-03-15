import streamlit as st
import requests
import json

# Replace with your actual Google AI API Key
API_KEY = ""  

# Function to call Gemini API
def chat_with_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # Extract response text
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "⚠️ Error: No response from API. Check API key & model."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Streamlit UI
st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! I will help screen candidates for technical roles.")

# Collect candidate details
st.subheader("📋 Candidate Details")
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
position = st.text_input("Desired Position")
location = st.text_input("Current Location")
tech_stack = st.text_area("Tech Stack (e.g., Python, Django, React, PostgreSQL)")

# Generate technical questions
if st.button("Generate Questions"):
    if name and email and experience and position and tech_stack:
        prompt = f"""
        Act as a hiring assistant. A candidate has applied with the following details:
        - Name: {name}
        - Email: {email}
        - Experience: {experience} years
        - Desired Position: {position}
        - Tech Stack: {tech_stack}

        Generate 3-5 relevant technical questions to assess the candidate's proficiency.
        """
        questions = chat_with_gemini(prompt)
        st.subheader("🧑‍💻 Technical Questions")
        st.write(questions)
    else:
        st.warning("⚠️ Please fill in all fields before generating questions.")

# Chatbot interaction
st.subheader("💬 Chat with TalentScout")
user_input = st.text_input("Ask me anything about the hiring process!")

if user_input:
    response = chat_with_gemini(user_input)
    st.write("🤖 TalentScout:", response)
