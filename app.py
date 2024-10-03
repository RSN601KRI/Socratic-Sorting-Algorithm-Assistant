# File: app.py

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import plotly.graph_objects as go
import random

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up the model
model = genai.GenerativeModel('gemini-pro')

# Import sorting algorithms
from sorting_algorithms import bubble_sort, insertion_sort, quicksort, analyze_bubble_sort, analyze_insertion_sort, analyze_quicksort

def get_socratic_response(user_input, context, algorithm, conversation_history):
    prompt = f"""
    You are a Socratic teaching assistant specializing in sorting algorithms, specifically {algorithm}. Your goal is to guide the student towards understanding through questions, not direct answers. Use the following context, conversation history, and user input to formulate a response:

    Context: {context}
    Conversation History: {conversation_history}
    User Input: {user_input}

    Remember:
    1. Ask probing questions to lead the student to the answer.
    2. Encourage critical thinking about algorithm efficiency and trade-offs.
    3. If the student is stuck, provide small hints rather than full solutions.
    4. Adapt your questions based on the student's level of understanding.
    5. If discussing a timeout issue, guide the student to consider input size and time complexity.
    6. Refer to the visualizations and code execution results when relevant.

    Respond with a question or a series of questions to guide the student's thinking.
    """
    
    response = model.generate_content(prompt)
    return response.text

def visualize_sorting(algorithm, arr):
    fig = go.Figure()
    
    for i in range(len(arr)):
        fig.add_trace(go.Bar(x=[i], y=[arr[i]], name=f'Step {i}'))
    
    fig.update_layout(title=f'{algorithm} Visualization',
                      xaxis_title='Index',
                      yaxis_title='Value',
                      showlegend=False)
    
    return fig

def execute_code(code, input_array):
    try:
        exec(code)
        sorted_array = eval(f"{algorithm.lower().replace(' ', '_')}(input_array)")
        return sorted_array, None
    except Exception as e:
        return None, str(e)

def main():
    st.title("Enhanced Socratic Sorting Algorithm Assistant")

    # Initialize session state
    if 'context' not in st.session_state:
        st.session_state.context = "The student is learning about sorting algorithms: Bubble Sort, Insertion Sort, and Quick Sort."
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    if 'current_algorithm' not in st.session_state:
        st.session_state.current_algorithm = "Bubble Sort"
    if 'input_array' not in st.session_state:
        st.session_state.input_array = [random.randint(1, 100) for _ in range(10)]

    # Sidebar for algorithm selection and context update
    st.sidebar.subheader("Current Algorithm")
    st.session_state.current_algorithm = st.sidebar.selectbox("Select Algorithm", ["Bubble Sort", "Insertion Sort", "Quick Sort"])

    st.sidebar.subheader("Current Context")
    st.sidebar.write(st.session_state.context)

    new_context = st.sidebar.text_area("Update Context", st.session_state.context)
    if st.sidebar.button("Update Context"):
        st.session_state.context = new_context

    # Input array generation
    st.subheader("Input Array")
    array_size = st.slider("Array Size", 5, 20, 10)
    if st.button("Generate New Array"):
        st.session_state.input_array = [random.randint(1, 100) for _ in range(array_size)]
    st.write(st.session_state.input_array)

    # Visualization
    st.subheader("Algorithm Visualization")
    if st.button("Visualize Sorting"):
        sorted_array = eval(f"{st.session_state.current_algorithm.lower().replace(' ', '_')}(st.session_state.input_array.copy())")
        fig = visualize_sorting(st.session_state.current_algorithm, sorted_array)
        st.plotly_chart(fig)

    # Code execution
    st.subheader("Code Execution")
    user_code = st.text_area("Enter your sorting algorithm code:", height=200)
    if st.button("Execute Code"):
        result, error = execute_code(user_code, st.session_state.input_array)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success("Code executed successfully!")
            st.write("Sorted array:", result)

    # Time complexity analysis
    st.subheader("Time Complexity Analysis")
    n = len(st.session_state.input_array)
    if st.session_state.current_algorithm == "Bubble Sort":
        st.write(analyze_bubble_sort(n))
    elif st.session_state.current_algorithm == "Insertion Sort":
        st.write(analyze_insertion_sort(n))
    else:
        st.write(analyze_quicksort(n))

    # Main conversation area
    st.subheader("Conversation")
    for entry in st.session_state.conversation_history:
        st.text(entry)

    # User input
    user_input = st.text_area("Your question or response:")

    if st.button("Submit"):
        if user_input:
            st.session_state.conversation_history.append(f"Student: {user_input}")
            response = get_socratic_response(user_input, st.session_state.context, st.session_state.current_algorithm, st.session_state.conversation_history)
            st.session_state.conversation_history.append(f"Assistant: {response}")
            st.experimental_rerun()
        else:
            st.warning("Please enter a question or response.")

if __name__ == "__main__":
    main()