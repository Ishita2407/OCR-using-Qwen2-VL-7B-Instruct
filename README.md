# Image OCR with Keyword Search and Question Answering

This project utilizes the `Qwen2-VL-7B-Instruct` model from Hugging Face to perform Optical Character Recognition (OCR) on uploaded images. The application allows users to extract text from images and either search for specific keywords or ask questions about the content.
# Project Results Screenshorts
Demo1
![image](https://github.com/user-attachments/assets/ef905e5e-95bc-47cd-b601-3758eb6c6cac)

Demo 2
![image](https://github.com/user-attachments/assets/07d40bfb-065f-4706-8879-0ee2cc82a1fc)

Demo 3
![image](https://github.com/user-attachments/assets/0d842371-d554-4a28-9a0c-4154a10af902)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- Python 3.7 or higher
- pip (Python package installer)
- A compatible GPU with CUDA support (optional, but recommended for performance)

## Setup Instructions

1. **Clone the Repository**

   Open your terminal and run the following command to clone this repository:

   ```bash
   git clone https://github.com/Ishita2407/OCR-using-Qwen2-VL-7B-Instruct.git
   cd OCR_application
## Create a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies:

- bash
- python -m venv venv

## Activate the virtual environment:
- On Windows:
bash
venv\Scripts\activate

- On macOS/Linux:
bash
source venv/bin/activate

## Install Required Packages
Install the necessary libraries using pip:
- bash
- pip install -r requirements.txt

## Make sure the requirements.txt file includes the following packages:
- plaintext
- torch
- transformers
- gradio
- Pillow

## Running the Application Locally
Ensure your environment is activated (refer to step 2 in the Setup Instructions).

## Run the application
Execute the following command to start the Gradio app:
bash
python app.py
