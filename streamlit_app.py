# socratic_helper.py

import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
API_ENDPOINT = "https://gemini.googleapis.com/v1/your-endpoint"

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def generate_socratic_question_for_sorting(student_input, context, previous_question=None):
    """
    Generates a Socratic method question specifically for sorting algorithm learning.
    This function avoids repeating the same questions and adapts based on input.
    """
    # Map different student input to responses based on keywords
    if 'timeout' in student_input.lower():
        if 'input size' in student_input.lower():
            if previous_question == "How does your sorting algorithm perform with larger inputs?":
                return "Can you think of a more efficient sorting algorithm for larger datasets?"
            return "How does your sorting algorithm perform with larger inputs?"

    if 'time complexity' in student_input.lower():
        return "What is the time complexity of your current sorting algorithm?"

    if 'slow' in student_input.lower():
        return "Can you explain why your algorithm might be slow for larger inputs?"

    if 'fail' in student_input.lower():
        return "What can you say about the input size of the test case?"

    # If no specific response found, call the Gemini API or fallback to a generic question
    return generate_generic_socratic_question(student_input)

def generate_generic_socratic_question(student_input):
    """
    Generates a general Socratic method question by interacting with the Gemini API.
    This is used as a fallback if no specific probing questions are triggered.
    """
    prompt = f"The student asked: {student_input}. Respond with a probing Socratic question focused on sorting algorithms."

    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(data))

        if response.status_code == 200:
            response_data = response.json()
            return response_data.get('choices')[0]['text'].strip()
        else:
            return "I encountered an issue with generating a question. Could you provide more details on your problem?"
    except Exception as e:
        return f"Error: {str(e)}. Please try again."
