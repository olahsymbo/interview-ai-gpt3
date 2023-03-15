# Interview-AI-GPT3

A simple chatbot built using OpenAI GPT-3. We used a dataset from another repo as explained in this [Article](https://medium.com/@olahsymbo/fine-tuning-openai-gpt-3-to-build-custom-chatbot-fe2dea524561)  

### Update: 

Added ChatGPT and an approach to handle conversation drift

## Getting Started
Create a virtual environment and install the dependencies

```
virtualenv .virtualenv
source .virtualenv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file and place OpenAI API Key in the file, e.g

``` 
OPENAI_KEY=REPLACE-WITH-KEY-FROM-OPENAI
```

### Finetuning the model

Simply run:

``` 
python helpers/trainer.py
```

### Test the model

Run:

``` 
python helpers/inference.py
```
You can always change the input text

### Test the model with Flask

Run:

``` 
python app.py
```

Example request:

```
curl --location 'http://127.0.0.1:5000/chat_openai_no_drift' \
--header 'Content-Type: application/json' \
--data '{
    "text": "what is linked list",
    "session_id": "KJN=87aGNw"
}'
```
