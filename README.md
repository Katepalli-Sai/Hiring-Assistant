# AI Hiring Assistant

## Overview
The AI Hiring Assistant is a chatbot built using Streamlit and Google's Gemini AI. It helps recruiters screen candidates by generating relevant technical questions based on their experience and tech stack. Additionally, it provides an interactive chat interface for hiring-related queries.

## Installation

### 1. Clone the repository:
```sh
git clone https://github.com/your-repo/ai-hiring-assistant.git
cd ai-hiring-assistant
```

### 2. Create a virtual environment (optional but recommended):
```sh
python -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```sh
pip install -r requirements.txt
```

### 4. Set up the API Key:
- Get your API key from Google AI Studio.
- Create a `.env` file and add:
```sh
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application:
```sh
streamlit run app.py
```

## Usage
1. Enter candidate details such as name, experience, and tech stack.
2. Click the "Generate Questions" button to get relevant interview questions.
3. Use the chatbot to ask hiring-related questions.

## Technical Details
- **Frameworks & Libraries**: Streamlit, Google Generative AI, Python
- **AI Model**: Gemini 2.0 (via Google AI Studio API)
- **Functionality**:
  - Generates customized technical questions
  - Provides interactive chat for hiring process queries

## Challenges & Solutions
- **Model Compatibility**: Faced issues with Gemini API versioning, resolved by using `gemini-2.0-flash`.
- **Streamlit Not Found Error**: Fixed by ensuring Streamlit is installed and activated in the virtual environment.

## Future Improvements
1. Enhance prompt engineering for better question generation.
2. Add candidate response evaluation features.
3. Improve UI for better recruiter experience.
