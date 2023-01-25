import os

import logging
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')

app.debug = True


@app.route("/chat_openai", methods=['POST'])
def get_bot_response():
    if request.method == 'POST':
        output_text = []
        try:
            user_text = request.get_json()["text"]
            output_text = generate_response(user_text)
            return jsonify({"message": str(output_text)}), 200

        except Exception as error:
            logging.error([error])
            # return jsonify(traceback.format_exc())
            return jsonify({}), 400
    else:
        return jsonify(success=False), 500


def generate_response(input_text):
    response = openai.Completion.create(
        engine="davinci:ft-personal-2023-01-25-19-20-17",
        prompt="The following is a conversation with DSA an AI assistant. "
               "DSA is an interview bot who is very helpful and knowledgeable in data structure and algorithms.\n\n"
               "Human: Hello, who are you?\n"
               "DSA: I am DSA, an interview digital assistant. How can I help you today?\n"
               "Human: {}\nDSA:".format(input_text),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " DSA:"]
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    app.run(host="0.0.0.0")