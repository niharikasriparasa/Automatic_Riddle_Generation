import pandas as pd
from rdflib import Graph,Namespace
from rdflib.namespace import FOAF,RDF,RDFS,OWL
from rdflib import Literal,URIRef,RDF,RDFS
import re
df=pd.read_excel(r'C:\Users\Niharika Sri Parasa\Downloads\list-animals-world-611j.xls',encoding="utf-8")


url="http://dbpedia.org/resource/"
g=Graph()
dict={'subject':[],'predicate':[],'object':[]}
concepts=['Animal','Amphibian','Reptile','Fish','Bird','Mammal','Insect','Crustacean','Eukaryote','Crustacean','Mollusc','Plant','Species']
#for animal in df['Animal'].unique():
for animal in concepts:
    if 'nan' not in str(animal):
        resource=url+animal
        print(resource)
        g.parse(resource)
        for s,p,o in g.triples((URIRef(resource),URIRef('http://dbpedia.org/ontology/abstract'),None)):
          if o.language =="en":
             dict['subject'].append(animal)
             dict['predicate'].append('abstract')
             dict['object'].append(o.value)
        for s,p,o in g.triples((URIRef(resource),RDF.type,None)):
            dict['subject'].append(animal)
            dict['predicate'].append('type')
            #regex = "\/rc\/(.*)'"
            dict['object'].append(o)
print(dict)
df=pd.DataFrame.from_dict(dict)
df.to_excel('animal(200+)_conceptdef.xlsx')
#df.to_csv('Animal_triples(200+).csv')