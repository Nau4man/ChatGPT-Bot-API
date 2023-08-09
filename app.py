import os
from flask import Flask, render_template, request, jsonify
from chatbot_api import ChatGPTBotAPI  
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
chatbot_api = ChatGPTBotAPI(openai_api_key)

try:
    chatbot_api.initialize_gpt3()
except Exception as e:
    # Handle initialization error
    print("Error initializing GPT-3:", e)

@app.route("/")
def root():
    return render_template('index.html')

@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    try:
        data = request.get_json()
        prompt = data.get('prompt')
        if prompt is None:
            return jsonify({"error": "Missing 'prompt' in the request data."}), 400

        prompt_index = chatbot_api.create_prompt(prompt)
        return jsonify({"prompt_index": prompt_index})
    except Exception as e:
        # Handle error during prompt creation
        return jsonify({"error": str(e)}), 500

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()
        prompt_index = data.get('prompt_index')
        if prompt_index is None:
            return jsonify({"error": "Missing 'prompt_index' in the request data."}), 400

        response = chatbot_api.get_response(prompt_index)
        return jsonify({"response": response})
    except Exception as e:
        # Handle error during response retrieval
        return jsonify({"error": str(e)}), 500

@app.route('/update_prompt', methods=['POST'])
def update_prompt():
    try:
        data = request.get_json()
        prompt_index = data.get('prompt_index')
        new_prompt = data.get('new_prompt')
        if prompt_index is None or new_prompt is None:
            return jsonify({"error": "Missing 'prompt_index' or 'new_prompt' in the request data."}), 400

        result = chatbot_api.update_prompt(prompt_index, new_prompt)
        return jsonify({"result": result})
    except Exception as e:
        # Handle error during prompt update
        return jsonify({"error": str(e)}), 500
        
@app.route('/delete_prompt', methods=['POST'])
def delete_prompt():
    try:
        data = request.get_json()
        prompt_index = data.get('prompt_index')
        if prompt_index is None:
            return jsonify({"error": "Missing 'prompt_index' in the request data."}), 400

        result = chatbot_api.delete_prompt(prompt_index)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
