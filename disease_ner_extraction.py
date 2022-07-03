import numpy as np
import pandas as pd
import en_ner_bc5cdr_md
csv_file='pubmed22n1115.csv'
data=pd.read_csv(csv_file)
data = data.dropna()
import spacy
nlp_bc = en_ner_bc5cdr_md.load()

phrases=['treatment of', 'treatment', 'cause', 'to treat','to cure','side effect','cure','prevent']
docs=spacy.load('en_core_web_sm')
def get_entity_from_spacy(article,nlp_bc):
    doc = nlp_bc(article)
    ent_bc = {}
    for x in doc.ents:
        ent_bc[x.text] = x.label_
    return ent_bc

abstract_list=data['abstract'].to_list()
for abstract in abstract_list:
    abs=docs(abstract)
    for sent in abs.sents:
        sentence=sent.text
        for phs in phrases:
            if phs in sentence:
                ent_bc=get_entity_from_spacy(sentence,nlp_bc)
                result={'sent': sentence,'relation':phs}
                result.update(ent_bc)
                print(result)




