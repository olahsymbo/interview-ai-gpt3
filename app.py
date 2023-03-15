import os
import logging
import traceback

import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from helpers.inference_chatgpt import generate_response_chatgpt, generate_response_chatgpt_no_drift

load_dotenv()

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')

app.debug = True


@app.route("/chat_openai", methods=['POST'])
def get_bot_response_chatgpt():
    if request.method == 'POST':
        output_text = []
        try:
            user_text = request.get_json()["text"]
            output_text = generate_response_chatgpt(user_text)
            return jsonify({"message": str(output_text)}), 200

        except Exception as error:
            logging.error([error])
            # return jsonify(traceback.format_exc())
            return jsonify({}), 400
    else:
        return jsonify(success=False), 500


session = {"session_id": ""}
interview_history = []


@app.route("/chat_openai_no_drift", methods=['POST'])
def get_bot_response_chatgpt_no_drift():
    if request.method == 'POST':
        output_text = []
        try:
            user_text = request.get_json()["text"]
            session_id = request.get_json()["session_id"]
            print(session_id)
            print(session["session_id"])
            if session_id == session["session_id"]:
                output_text = generate_response_chatgpt_no_drift(user_text, interview_history)
                interview = {
                    "question": user_text,
                    "answer": output_text
                }
                interview_history.append(interview)
            else:
                session["session_id"] = session_id
                interview_history2 = []
                output_text = generate_response_chatgpt_no_drift(user_text, interview_history2)
                interview = {
                    "question": user_text,
                    "answer": output_text
                }
                interview_history2.append(interview)

            return jsonify({"message": str(output_text),
                            "error": None,
                            "status": 200}), 200

        except Exception as error:
            logging.error([error])
            # return jsonify(traceback.format_exc())
            return jsonify({"error": "can't to process the input questions",
                            "status": 400}), 400
    else:
        return jsonify(success=False), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0")
