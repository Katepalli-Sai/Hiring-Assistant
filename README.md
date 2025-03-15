AI Hiring Assistant

Overview

The AI Hiring Assistant is a chatbot built using Streamlit and Google's Gemini AI. It helps recruiters screen candidates by generating relevant technical questions based on their experience and tech stack. Additionally, it provides an interactive chat interface for hiring-related queries.

Installation

1)Clone the repository:

2)Create a virtual environment (optional but recommended):

3)python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4)Install dependencies:

pip install -r requirements.txt

5)Set up the API Key:

Get your API key from Google AI Studio.

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here

6)Run the application:

streamlit run app.py

Usage

Enter candidate details such as name, experience, and tech stack.

Click the "Generate Questions" button to get relevant interview questions.

Use the chatbot to ask hiring-related questions.

Technical Details

Frameworks & Libraries: Streamlit, Google Generative AI, Python

AI Model: Gemini 2.0 (via Google AI Studio API)

Functionality:

Generates customized technical questions

Provides interactive chat for hiring process queries

Challenges & Solutions

Model Compatibility: Faced issues with Gemini API versioning, resolved by using gemini-2.0-flash.

Streamlit Not Found Error: Fixed by ensuring Streamlit is installed and activated in the virtual environment.

Future Improvements:

1)Enhance prompt engineering for better question generation.

2)Add candidate response evaluation features.

3)Improve UI for better recruiter experience.
