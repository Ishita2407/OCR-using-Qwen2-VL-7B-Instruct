# Install necessary packages
# This should not be included in the script when deploying on Hugging Face Spaces
# Use requirements.txt instead

import gradio as gr
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
import torch

# Load the model and processor
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-7B-Instruct",
    torch_dtype="auto",
    device_map="auto",
)

processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")

# OCR extraction function
def ocr_and_query(image, question):
    # Prepare image for the model
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {
                    "type": "text",
                    "text": question
                },
            ],
        }
    ]
    
    # Process image and text prompt
    text_prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=[text_prompt], images=[image], padding=True, return_tensors="pt")
    
    # Run the model to generate OCR results
    inputs = inputs.to("cuda")
    output_ids = model.generate(**inputs, max_new_tokens=1024)
    
    # Decode the generated text
    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(inputs.input_ids, output_ids)
    ]
    output_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)[0]
    
    return output_text

# Gradio interface
def gradio_app(image, question):
    extracted_text = ocr_and_query(image, question)
    return extracted_text

# Gradio interface setup
app = gr.Interface(
    fn=gradio_app,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(lines=2, placeholder="Enter your question here...", label="Question")
    ],
    outputs=[
        gr.Textbox(label="Extracted Text and Response")
    ],
    title="Image OCR and Query",
    description="Upload an image, extract text, and ask questions about its contents."
)

# Launch the app
app.launch(share=True)
