from rdflib.namespace import RDFS, RDF, XSD, Namespace
from rdflib import Graph, URIRef, Literal, BNode

g = Graph()
EX = Namespace('http://www.semanticweb.org/danicantabella/ontologies/2023/4/SDM_Lab3/')
g.bind('ex', EX) #Bind prefix to namespace


review = EX.review # http://www.semanticweb.org/danicantabella/ontologies/2023/4/SDM_Lab3/review/
submits = EX.submits
reviewer = EX.reviewer
editor = EX.editor
handlesConference = EX.handlesConference
handlesJournal = EX.handlesJournal
journal = EX.journal
volume = EX.volume
venue = EX.venue
has = EX.has
reviews = EX.reviews
paper = EX.paper
conference_type = EX.conferenceType
area = EX.area
conference = EX.conference
writes = EX.writes
author = EX.author
chair = EX.chair
proceeding = EX.proceeding
year = EX.year
publication = EX.publication
hasReview = EX.hasReview
fromJournal = EX.fromJournal
fromConference = EX.fromConference
human = EX.human
isSubmittedToJournal = EX.isSubmittedToJournal
isSubmittedToConference = EX.isSubmittedToConference
includedInProceeding = EX.includedInProceeding
includedInVolume = EX.includedInVolume
paperRelatedTo = EX.paperRelatedTo
journalRelatedTo = EX.journalRelatedTo
conferenceRelatedTo = EX.conferenceRelatedTo
chairAssigns = EX.chairAssigns
editorAssigns = EX.editorAssigns

#Attributes
#Review
accepted = EX.accepted
back_up_text = EX.back_up_text
#Paper
type = EX.type
title = EX.title
updated = EX.updated
url = EX.url
doi = EX.doi
abstract = EX.abstract
publicationDate = EX.publicationDate
#Author
name_human = EX.name_human
#Volume
year = EX.year
volumeNr = EX.volumeNr
#Proceedings
startDate = EX.startDate
endDate = EX.endDate
#Conference/ Journal
name = EX.name
issn = EX.issn
conferenceType = EX.conferenceType #Only for conferences
urlVenue = EX.urlVenue







