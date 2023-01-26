import os
import logging

import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from helpers.inference import generate_response

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
