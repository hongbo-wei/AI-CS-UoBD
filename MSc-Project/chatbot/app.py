import os
from transformers import pipeline
from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM


app = Flask(__name__)

# model = 'meta-llama/Llama-2-7b-chat-hf'
# model = 'gpt2'
tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-7b")

# Load the text generation pipeline with pre-trained model
generator = pipeline('text-generation', model=model)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']

    # Generate response using Hugging Face Transformers
    response = generate_response(user_message)

    return jsonify({'response': response})

def generate_response(user_message):
    # Generate response using GPT-2 model
    response = generator(user_message, max_length=50, num_return_sequences=1)[0]['generated_text']

    return response

if __name__ == '__main__':
    app.run(debug=True)
