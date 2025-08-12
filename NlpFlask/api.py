import nlpcloud

client = nlpcloud.Client("finetuned-llama-3-70b", "your api key", gpu=True)


import requests

def Sentiment_Analysis(text):
    try:
        return client.sentiment(text)
    except requests.exceptions.HTTPError as e:
        if "429" in str(e):
            return {"error": "Rate limit exceeded. Please try again later."}
        else:
            raise

def ner(text,target):
    try:
        return client.entities(text,searched_entity=target )
    except requests.exceptions.HTTPError as e:
        if "429" in str(e):
            return {"error": "Rate limit exceeded. Please try again later."}
        else:
            raise

def Code_Generation(text):
    try:
        return client.code_generation(text)
    except requests.exceptions.HTTPError as e:
        if "429" in str(e):
            return {"error": "Rate limit exceeded. Please try again later."}
        else:
            raise


