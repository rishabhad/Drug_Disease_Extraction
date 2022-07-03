# import os
# os.environ["CURL_CA_BUNDLE"]=""
# from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline
# model =  AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
# tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
# nlp = pipeline('ner', model=model, tokenizer=tokenizer)
# text='Ovarian cancer is seventh most common cancer in women worldwide.'
# output=nlp(text)
# print(output)

from transformers import pipeline
classifier = pipeline("sentiment-analysis")
classifier("We are very happy to show you the 🤗 Transformers library.")