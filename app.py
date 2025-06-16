from flask import Flask, jsonify, render_template
## import tiktoken 

# set up web server
app = Flask (__name__)

## homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/count', methods =['POST'])
def countTokens():
    data = prompt.get_json()
    prompt = data.get('prompt','')
    token_count = len(prompt.split())
    return jsonify({'token_count': token_count})
