# Interview-AI-GPT3

A simple chatbot built using OpenAI GPT-3. 

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
python helpers/trainers.py
```

### Test the model

Run:

``` 
python helpers/inference.py
```
You can always change the input text