import gzip
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import pandas as pd

file_name='pubmed22n1115.xml.gz'
output_file = file_name.replace('gz', '')
path='Pubmed_Data/'

def unzip_xml_files(file_name):
    op = open(path + output_file, "w", encoding="utf-8")
    with gzip.open(path + file_name, "rb") as ip_byte:
        op.write(ip_byte.read().decode('utf-8'))

def read_xml_file(file_name):
    #xml_file=open(file_name,'r',encoding="utf-8")
    #soup = BeautifulSoup(xml_file, 'lxml')
    tree=ET.parse(file_name)
    root=tree.getroot()
    articles=root.findall('PubmedArticle')
    pubmed_article_list=[]
    for article in articles[:1000]:
        article_dict={}
        medline=article.find('MedlineCitation')
        article=medline.find('Article')
        pmid=medline.find('PMID').text
        article_dict['PMID']=pmid
        try:
            article_title = article.find('ArticleTitle')
            article_title_text = article_title.text
            abstrcat_text = article.find('Abstract').find('AbstractText').text
            article_dict['abstract']=abstrcat_text
            pubmed_article_list.append(article_dict)
        except Exception as e:
            print(e)

    article_df=pd.DataFrame(pubmed_article_list)
    csv_file=output_file.replace('.xml','.csv')
    article_df.to_csv(csv_file)

read_xml_file(path+output_file)