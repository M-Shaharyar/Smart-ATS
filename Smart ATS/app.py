# Importing required libraries and modules
import streamlit as st  # Streamlit for creating the web application interface
import google.generativeai as genai  # Google Generative AI library for calling AI models
import os  # os module for interacting with the operating system (e.g., accessing environment variables)
import PyPDF2 as pdf  # PyPDF2 for reading and extracting text from PDF files
from dotenv import load_dotenv  # load_dotenv to load environment variables from a .env file

# Load all environment variables from a .env file
load_dotenv()

# Configure the Generative AI model by setting the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define a function to get a response from the generative model using a given input
def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-pro')  # Initialize the model with 'gemini-pro' as the model type
    response = model.generate_content(input)  # Generate content based on the input prompt
    return response.text  # Return the generated response text

# Define a function to extract text from an uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)  # Initialize PdfReader with the uploaded file
    text = ""  # Initialize an empty string to hold the extracted text
    # Loop through each page of the PDF to extract text
    for page in range(len(reader.pages)):
        page = reader.pages[page]  # Get the current page object
        text += str(page.extract_text())  # Append the extracted text from each page
    return text  # Return the accumulated text from all pages

# Define prompt templates for AI evaluation with placeholders for dynamic content
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst,
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive, and you should provide 
the best assistance for improving the resumes. Assign the percentage matching based 
on JD and the missing keywords with high accuracy.
resume: {text}
description: {jd}
"""

input_prompt1 = """
You are an experienced Technical Human Resource Manager; your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
resume: {text}
description: {jd}
"""

# Streamlit app components
st.title("Smart ATS")  # Title of the Streamlit application
st.text("Improve Your Resume ATS")  # Short description of the application

# Text area for users to paste the job description
jd = st.text_area("Paste the Job Description")

# File uploader for users to upload a resume in PDF format
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

# Buttons for selecting which evaluation to run
submit_main = st.button("Evaluate with Main ATS Prompt")  # Button for Main ATS evaluation
submit_hr = st.button("Evaluate with HR Perspective")  # Button for HR Perspective evaluation

# Check if a file has been uploaded
if uploaded_file is not None:
    text = input_pdf_text(uploaded_file)  # Extract text from the uploaded PDF file

    # Run Main ATS Prompt if the corresponding button is clicked
    if submit_main:
        response = get_gemini_repsonse(input_prompt.format(text=text, jd=jd))  # Generate response
        st.subheader("ATS Evaluation Result:")  # Display section header
        st.write(response)  # Display the response

    # Run HR Perspective Prompt if the corresponding button is clicked
    elif submit_hr:
        response = get_gemini_repsonse(input_prompt1.format(text=text, jd=jd))  # Generate response
        st.subheader("HR Evaluation Result:")  # Display section header
        st.write(response)  # Display the response

# If no file is uploaded, display a message prompting the user to upload one
else:
    st.write("Please upload the resume")
