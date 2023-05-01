import tbox
from tbox import *
from rdflib.namespace import RDFS, RDF, XSD, Namespace
from rdflib import Graph, URIRef, Literal, BNode
import csv
import datetime
from datetime import datetime
import random
import subprocess


def loadPapers(data): #[id, title, publicationDate, abstract, DOI, URL, updated, type]
    id = EX[data[0]]
    titleAtt = Literal(data[1], datatype=XSD.string)
    publicationDateAtt = Literal(data[2], datatype=XSD.date)
    abstractAtt = Literal(data[3], datatype=XSD.string)
    doiAtt = Literal(data[4], datatype=XSD.string)
    urlAtt = Literal(data[5], datatype=XSD.string)
    updatedAtt = Literal(data[6], datatype=XSD.dateTimeStamp)
    typeAtt = Literal (data[7], datatype=XSD.string)

    if data[0] is not None: #id
        g.add((id,RDF.type,tbox.paper))
    if data[1] is not None: #title
        g.add((id,tbox.title,titleAtt))
    if data[2] is not None: #publicationDate
        g.add((id,tbox.publicationDate,publicationDateAtt))
    if data[3] is not None: #abstract
        g.add((id,tbox.abstract,abstractAtt))
    if data[4] is not None: #DOI
        g.add((id,tbox.doi,doiAtt))
    if data[5] is not None: #URL
        g.add((id,tbox.url,urlAtt))
    if data[6] is not None: #updated
        g.add((id,tbox.updated,updatedAtt))
    if data[7] is not None: #type
        g.add((id,tbox.type,typeAtt))
def correctPaperData(data):
    numFields = len(data)
    for i in range(0,numFields):
        if bool(data[i]) == True:
            if i in [0,1,3,4,5,7]: #id, title, abstract, doi, url, type
               data[i] = str(data[i])
            elif i == 2: # publicationdate
                data[i] = datetime.strptime(data[i], '%Y-%m-%d').date()
            elif i == 6: #updated
                data[i] = datetime.fromisoformat(data[i].replace('Z', '+00:00'))
        else:
            data[i] = None
    return data

def getAbstractData(corpusid):
    with open('./data/abstracts-sample.csv', newline='') as abstracts:
        reader = csv.DictReader(abstracts)
        for paper in reader:
            if paper['corpusid']==corpusid:
                abstract = paper['abstract']
            else:
                abstract = None
    return abstract



if __name__ == "__main__":
#LOAD TBOX
#crear funcio que inici tbox.py
    subprocess.run(["python3", "tbox.py"])
#ABOX PAPERS
    with open('./data/papers-processed.csv', newline='') as papers:
        reader = csv.DictReader(papers)
        for paper in reader:
            data = [paper['corpusid'], paper['title'], paper['publicationdate'], getAbstractData(paper['corpusid']), paper['DOI'], paper['url'],
                    paper['updated'], random.choice(["Short paper", "Full paper", "Poster", "Demo paper"])]
            correctedPaperData = correctPaperData(data)
            loadPapers(correctedPaperData)

#ABOX AUTHORS

#ABOX VOLUME

#ABOX AREA

#ABOX PROCESSINGS

#ABOX CONFERENCE

#ABOX JOURNALS

#ABOX DECISION


print(g.serialize())
g.serialize(destination="abox.ttl", format="ttl")