from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace 'YOUR_HUGGINGFACE_API_TOKEN' with your actual Hugging Face API token
API_URL = "https://api-inference.huggingface.co/models/JanSt/albert-base-v2_mbti-classification"
API_TOKEN = "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"

def query_huggingface(payload):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        response = query_huggingface({"inputs": text})
        # Assuming the response is a list of dictionaries as shown
        if response:
            # Sort the response based on scores
            sorted_response = sorted(response[0], key=lambda k: k['score'], reverse=True)
            result = sorted_response
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
