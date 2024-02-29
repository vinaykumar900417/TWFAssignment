from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the Translation API! This API allows you to translate text from English to French using the Google Translator.'

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()

        if 'text' not in data:
            print('Missing "text" parameter')
            return jsonify({'error': 'Missing "text" parameter'}), 400

        text_to_translate = data['text']
        translated_text = GoogleTranslator(source='auto', target='fr').translate(text_to_translate)

        return jsonify({'translated_text': translated_text})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
