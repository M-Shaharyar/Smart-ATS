# Smart ATS - Resume Evaluation Tool
Smart ATS is a Streamlit application designed to help users improve their resumes by providing a detailed analysis against a specific job description. It leverages Google’s Generative AI model to offer feedback from both an ATS (Applicant Tracking System) and HR perspective, identifying strengths, weaknesses, and missing keywords for an improved match with job requirements

## Features
* Upload Resume PDF: Upload your resume in PDF format for analysis.
* ATS Evaluation: Get a detailed assessment from an ATS perspective, including percentage matching and missing keywords.
* HR Evaluation: Receive an HR manager's view, highlighting strengths and weaknesses in relation to job requirements.
* Insights for Improvement: Offers feedback tailored to improve resume alignment with the provided job description.

## Tech Stack
* Python
* Streamlit - for building the web interface
* Google Generative AI - for generating content and evaluations
* PyPDF2 - for reading PDF files and extracting text
* dotenv - for managing environment variables


## Installation
1. Clone the Repository
```
git clone https://github.com/M-Shaharyar/smart-ats.git
cd smart-ats
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Set Up Environment Variables
Create a .env file in the root directory with your Google API key:
```
GOOGLE_API_KEY=your_google_api_key
```
## Running the Application
* Run the application using Streamlit:
```
streamlit run app.py
```

## Usage
1. Enter Job Description: Paste the job description into the provided text area.
2. Upload Resume: Upload your resume in PDF format.
3. Choose Evaluation Method:
4. Main ATS Prompt: Provides a machine-based ATS evaluation, including percentage match and missing keywords.
5. HR Perspective: Offers an HR manager’s perspective on resume strengths and weaknesses.
6. View the generated evaluation results in the app.




