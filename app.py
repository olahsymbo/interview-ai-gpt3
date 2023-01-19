import os

import logging
import openai
from flask import Flask, render_template, request, jsonify
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
            output_text = generate_openai_response(user_text)
            return jsonify({"message": str(output_text)}), 200

        except Exception as error:
            logging.error([error])
            # return jsonify(traceback.format_exc())
            return jsonify({}), 400
    else:
        return jsonify(success=False), 500


def generate_openai_response(input_text):
    response = openai.Completion.create(
        engine="davinci:ft-personal-2023-01-02-14-04-19",
        prompt="The following is a conversation with JAMES-ADEWOLE an AI assistant. "
               "JAMES-ADEWOLE is a career coach who is very helpful, compassionate, clever, and very friendly.\n\n"
               "JAMES-ADEWOLE is 25 years old from Nigeria.\n\n"
               "Client: Hello, who are you?\n"
               "JAMES-ADEWOLE: I am James Adewole, a career coach and digital assistant. How can I help you today?\n"
               "Client: {}\nJAMES-ADEWOLE:".format(input_text),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " James:"]
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    app.run(host="0.0.0.0")