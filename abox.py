import tbox
from tbox import *
from rdflib.namespace import RDFS, RDF, XSD, Namespace
from rdflib import Graph, URIRef, Literal, BNode
import csv
import datetime
from datetime import datetime
import random
from tbox import g
import subprocess

def loadPublications(data): #[id, title, publicationDate, abstract, DOI, URL, updated, type]
    id = EX[data[0]]
    titleAtt = Literal(data[1], datatype=XSD.string)
    publicationDateAtt = Literal(data[2], datatype=XSD.date)
    abstractAtt = Literal(data[3], datatype=XSD.string)
    doiAtt = Literal(data[4], datatype=XSD.string)
    urlAtt = Literal(data[5], datatype=XSD.string)
    updatedAtt = Literal(data[6], datatype=XSD.dateTimeStamp)
    typeAtt = Literal (data[7], datatype=XSD.string)

    if data[0] is not None: #id
        g.add((id,RDF.type,tbox.publication))
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

def loadAuthors(data): #[id, name]
    id = EX[data[0]]
    nameAtt = Literal(data[1], datatype=XSD.string)

    if data[0] is not None: #id
        g.add((id,RDF.type,tbox.author))
    if data[1] is not None: #name
        g.add((id,tbox.name,nameAtt))
def correctAuthorData(data):
    numFields = len(data)
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [0,1]: #id, name
                data[i] = str(data[i])
        else:
            data[i] = None
    return data

def loadVolumes(data): #[id, year, volume_number_of_the_year]
    id = EX[data[0]]
    yearAtt = Literal(data[1], datatype=XSD.integer)
    volumeNrAtt = Literal(data[2], datatype=XSD.integer)

    if data[0] is not None:  # id
        g.add((id, RDF.type, tbox.volume))
    if data[1] is not None:  # year
        g.add((id, tbox.year, yearAtt))
    if data[2] is not None:  # volume_number_of_the_year
        g.add((id, tbox.volumeNr, volumeNrAtt))
def correctVolumeData(data):
    numFields = len(data)
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [0]: #id
                data[i] = str(data[i])
            elif i in [1,2]:#year, volume_number_of_the_year
                data[i] = int(data[i])
        else:
            data[i] = None
    return data

def loadAreas(data):
    areaName = EX[data[0]]
    if data[0] is not None:  # areaName
        g.add((areaName, RDF.type, tbox.area))
def correctAreaData(data):
    numFields = len(data)
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [0]: # areaName
                data[i] = str(data[i].replace(' ','_')) #eg. artificial intelligence -> artificial_intelligence
        else:
            data[i] = None
    return data

def loadProceedings(data):
    id = EX[data[0]]
    startDateAtt = Literal(data[1], datatype=XSD.date)
    endDateAtt = Literal(data[2], datatype=XSD.date)

    if data[0] is not None:  # id
        g.add((id, RDF.type, tbox.proceeding))
    if data[1] is not None:  # startDate
        g.add((id, tbox.startDate, startDateAtt))
    if data[2] is not None:  # endDate
        g.add((id, tbox.endDate, endDateAtt))
def correctProceedingData(data):
    numFields = len(data)
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [0]: #id
                data[i] = str(data[i])
            elif i in [1,2]: #startTime, endTime
                data[i] = datetime.strptime(data[i], '%Y-%m-%d').date()
        else:
            data[i] = None
    return data

def loadConferences(data): #[id, name, issn, url, type]
    id = EX[data[0]]
    nameAtt = Literal(data[1], datatype=XSD.string)
    issnAtt = Literal(data[2], datatype=XSD.string)
    urlAtt = Literal(data[3], datatype=XSD.string)
    typeAtt = Literal(data[4], datatype=XSD.string)

    if data[0] is not None:  # id
        g.add((id, RDF.type, tbox.conference))
    if data[1] is not None:  # name
        g.add((id, tbox.name, nameAtt))
    if data[2] is not None:  # issn
        g.add((id, tbox.issn, issnAtt))
    if data[3] is not None:  # url
        g.add((id, tbox.url, urlAtt))
    if data[4] is not None:  # type
        g.add((id, tbox.conference_type, typeAtt))
def correctConferenceData(data):
    numFields = len(data)
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [0,1,2,3,4]:  # id
                data[i] = str(data[i])
        else:
            data[i] = None
    return data

def loadJournals(data):
    id = EX[data[0]]
    nameAtt = Literal(data[1], datatype=XSD.string)
    issnAtt = Literal(data[2], datatype=XSD.string)
    urlAtt = Literal(data[3], datatype=XSD.string)

    if data[0] is not None:  # id
        g.add((id, RDF.type, tbox.journal))
    if data[1] is not None:  # name
        g.add((id, tbox.name, nameAtt))
    if data[2] is not None:  # issn
        g.add((id, tbox.issn, issnAtt))
    if data[3] is not None:  # url
        g.add((id, tbox.url, urlAtt))
def correctJournalData(data):
    numFields = len(data)
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [0,1,2,3]:
                data[i] = str(data[i])
        else:
            data[i] = None
    return data

def loadDecisions(data):
    id = EX[data[0]]
    acceptedAtt = Literal(data[1], datatype=XSD.boolean)
    back_up_textAtt = Literal(data[2], datatype=XSD.string)

    if data[0] is not None:  # id
        g.add((id, RDF.type, tbox.decision))
    if data[1] is not None:  # accepted
        g.add((id, tbox.accepted, acceptedAtt))
    if data[2] is not None:  # back_up_text
        g.add((id, tbox.back_up_text, back_up_textAtt))
def correctDecisionData(data): #paperId, reviewerID, grade, review
    numFields = len(data)
    newData=[str(data[0]+"-"+data[1]), "accepted", "back_up_text"] #id is paperId-reviewerID
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [2]: #accepted
                if int(data[i]) > 2: #if grade > 2 approved
                    newData[i-1] = True
                else:
                    newData[i-1] = False
            elif i in [3]: #paperId, reviewerID, review
                newData[i-1] = str(data[i])
        else:
            newData[i] = None
    return newData

def loadRelations(subject, predicate, object):
    if subject is not None and object is not None:  # id
        g.add((EX[subject], predicate, EX[object]))
def correctPropertiesData(data):
    numFields = len(data)
    for i in range(0, numFields):
        if bool(data[i]) == True:
            if i in [0, 1]:
                data[i] = str(data[i])
        else:
            data[i] = None
    return data


if __name__ == "__main__":
#LOAD TBOX
#crear funcio que inici tbox.py
    # subprocess.run(["python3", "tbox.py"])
#LOAD CLASSES
#ABOX PUBLICATIONS
    with open('./data/papers-processed.csv', newline='') as publications:
        reader = csv.DictReader(publications)
        for publication in reader:
            data = [publication['corpusid'], publication['title'], publication['publicationdate'],
                    getAbstractData(publication['corpusid']), publication['DOI'], publication['url'],
                    publication['updated'], random.choice(["short paper", "full paper", "poster", "demo paper"])]
            correctedPaperData = correctPaperData(data)
            loadPublications(correctedPaperData)
#ABOX AUTHORS
    with open('./data/authors-sample.csv', newline='') as authors:
        reader = csv.DictReader(authors)
        for author in reader:
            data = [author['authorid'], author['name']]
            correctedAuthorData = correctAuthorData(data)
            loadAuthors(correctedAuthorData)
#ABOX VOLUME
    with open('./data/volume-from.csv', newline='') as volumes:
        reader = csv.DictReader(volumes)
        for volume in reader:
            data = [volume['volumeID'], volume['year'], volume['volume']]
            correctedVolumeData = correctVolumeData(data)
            loadVolumes(correctedVolumeData)
#ABOX AREA
    with open('./data/keywords.csv', newline='') as areas:
        reader = csv.DictReader(areas)
        for area in reader:
            data = [area['keyword']]
            correctedAreaData = correctAreaData(data)
            loadAreas(correctedAreaData)
#ABOX PROCEEDINGS
    with open('./data/is-from.csv', newline='') as proceedings:
        reader = csv.DictReader(proceedings)
        for proceeding in reader:
            data = [proceeding['editionID'],proceeding['startDate'],proceeding['endDate']]
            correctedProceedingData = correctProceedingData(data)
            loadProceedings(correctedProceedingData)
#ABOX CONFERENCE
    with open('./data/conferences.csv', newline='') as conferences:
        reader = csv.DictReader(conferences)
        for conference in reader:
            data = [conference['conferenceID'],conference['conferenceName'],conference['issn'],conference['url'],
                    random.choice(["workshop", "symposium", "expert group", "regular conference"])]
            correctedConferenceData = correctConferenceData(data)
            loadConferences(correctedConferenceData)
#ABOX JOURNALS
    with open('./data/journals.csv', newline='') as journals:
        reader = csv.DictReader(journals)
        for journal in reader:
            data = [journal['venueID'],journal['journalName'],journal['issn'],journal['url']]
            correctedJournalData = correctJournalData(data)
            loadJournals(correctedJournalData)
#ABOX DECISION
    with open('./data/reviewed-by.csv', newline='') as decisions:
        reader = csv.DictReader(decisions)
        for decision in reader:
            data = [decision['paperID'],decision['reviewerID'],decision['grade'],decision['review']]
            correctedDecisionData = correctDecisionData(data)
            loadDecisions(correctedDecisionData)

#LOAD PROPERTIES
#WRITES
    with open('./data/written-by.csv', newline='') as writes:
        reader = csv.DictReader(writes)
        for write in reader:
            data = [write['authorID'],write['paperID']]
            correctedWrittenData = correctPropertiesData(data)
            loadRelations(correctedWrittenData[0], tbox.writes, correctedWrittenData[1])
#REVIEWS, SUBMITS & HAS_DECISION
    with open('./data/reviewed-by.csv', newline='') as submits:
        reader = csv.DictReader(submits)
        for submit in reader:

            data = [submit['reviewerID'],submit['paperID']]
            correctedReviewedData = correctPropertiesData(data)
            g.add((EX[correctedReviewedData[0]], RDF.type, tbox.reviewer)) #Add reviewers first
            loadRelations(correctedReviewedData[0], tbox.reviews, correctedReviewedData[1])

            data = [submit['reviewerID'], str(submit['paperID']) + '-' + str(submit['reviewerID'])]  # decision id is paperID-reviewerID
            correctedSubmittedData = correctPropertiesData(data)
            loadRelations(correctedSubmittedData[0], tbox.submits, correctedSubmittedData[1])

            data = [submit['paperID'], str(submit['paperID'])+'-'+str(submit['reviewerID'])] #decision id is paperID-reviewerID
            correctedDecisionData = correctPropertiesData(data)
            loadRelations(correctedDecisionData[0], tbox.hasDecision, correctedDecisionData[1])
#IS_RELATED_TO
    with open('./data/related-to.csv', newline='') as relates:
        reader = csv.DictReader(relates)
        for relate in reader:
            data = [relate['paperID'],str(relate['keyword']).replace(' ', '_')]
            correctedReviewedData = correctPropertiesData(data)
            loadRelations(correctedReviewedData[0], tbox.isRelatedTo, correctedReviewedData[1])
#INCLUDES
    with open('./data/belongs-to.csv', newline='') as includes: #proceeding includes publication
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['venueID'],include['paperID']]
            correctedReviewedData = correctPropertiesData(data)
            loadRelations(correctedReviewedData[0], tbox.includes, correctedReviewedData[1])

    with open('./data/published-in.csv', newline='') as includes: #volume includes publication
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['venueID'],include['paperID']]
            correctedReviewedData = correctPropertiesData(data)
            loadRelations(correctedReviewedData[0], tbox.includes, correctedReviewedData[1])

#PROCEEDINGS AND VOLUMES SUB_CLASS_OF
    with open('./data/is-from.csv', newline='') as includes: #proceeding subClassOf conference
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['editionID'],include['conferenceID']]
            correctedReviewedData = correctPropertiesData(data)
            loadRelations(correctedReviewedData[0], RDFS.subClassOf, correctedReviewedData[1])

    with open('./data/volume-from.csv', newline='') as includes: #volume subClassOf journal
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['volumeID'], include['journalID']]
            correctedReviewedData = correctPropertiesData(data)
            loadRelations(correctedReviewedData[0], RDFS.subClassOf, correctedReviewedData[1])

#CHAIRS  ??

#EDITORS ??


print(g.serialize())
g.serialize(destination="abox.ttl", format="ttl")