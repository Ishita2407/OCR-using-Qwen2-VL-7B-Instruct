# Image OCR with Keyword Search and Question Answering

This project utilizes the `Qwen2-VL-7B-Instruct` model from Hugging Face to perform Optical Character Recognition (OCR) on uploaded images. The application allows users to extract text from images and either search for specific keywords or ask questions about the content.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application Locally](#running-the-application-locally)
- [Deployment Process](#deployment-process)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- Python 3.7 or higher
- pip (Python package installer)
- A compatible GPU with CUDA support (optional, but recommended for performance)

## Setup Instructions

1. **Clone the Repository**

   Open your terminal and run the following command to clone this repository:

   ```bash
   git clone 
   cd OCR_application
Create a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install Required Packages

Install the necessary libraries using pip:

bash
Copy code
pip install -r requirements.txt
Make sure the requirements.txt file includes the following packages:

plaintext
Copy code
torch
transformers
gradio
Pillow
Running the Application Locally
Ensure your environment is activated (refer to step 2 in the Setup Instructions).

Run the application

Execute the following command to start the Gradio app:

bash
Copy code
python app.py
Replace app.py with the name of your main Python file if it's named differently.

Access the Application

Once the application is running, you will see output in your terminal indicating that the app is accessible. Open your web browser and go to the following URL:

arduino
Copy code
http://localhost:7860
Deployment Process
To deploy this application, you can use platforms like Hugging Face Spaces or Streamlit Sharing. Below is a general outline for deploying on Hugging Face Spaces:

Create a New Space

Go to Hugging Face Spaces and create a new space.

Upload Your Files

Upload the following files to your space:

app.py (or your main Python file)
requirements.txt (make sure it includes all necessary libraries)
Configure the Space

Ensure that your space is configured to run Python applications. You may need to specify the entry point in the settings.

Deploy

Once your files are uploaded, Hugging Face will automatically build and deploy your application. You will receive a URL to access your deployed app once it is live.

Usage
Upload Image: Click on the "Upload Image" button to select an image from your device.
Keyword Search: Enter a keyword to search for in the extracted text.
Question Answering: Switch to the "Question Answering" mode to ask questions about the image content.
Contributing
Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.


