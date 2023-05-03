from rdflib.namespace import RDFS, RDF, XSD, Namespace
from rdflib import Graph, URIRef, Literal, BNode

g = Graph()
EX = Namespace('http://example.org/')
g.bind('ex', EX) #Bind prefix to namespace


review = EX.review # http://example.org/review/
submits = EX.submits
reviewer = EX.reviewer
assigns = EX.assigns
editor = EX.editor
handlesConference = EX.handlesConference
handlesJournal = EX.handlesJournal
journal = EX.journal
volume = EX.volume
venue = EX.venue
has = EX.has
reviews = EX.reviews
paper = EX.paper
conference_type = EX.conference_type
area = EX.area
conference = EX.conference
writes = EX.writes
author = EX.author
chair = EX.chair
proceeding = EX.proceeding
year = EX.year
publication = EX.publication
includes = EX.includes
isRelatedTo = EX.isRelatedTo
hasReview = EX.hasReview
fromJournal = EX.fromJournal
fromConference = EX.fromConference

#Attributes
#Review
accepted = EX.accepted
back_up_text = EX.back_up_text
#Paper
type = EX.type
title = EX.title
updated = EX.updated
url = EX.url #Repeated
doi = EX.doi
abstract = EX.abstract
publicationDate = EX.publicationDate
#Author
name_author = EX.name_author
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
# url = EX.url #Repeated

# Triples
g.add((submits, RDFS.range, review))
g.add((submits, RDFS.domain, reviewer))
g.add((reviews, RDFS.domain, reviewer))
g.add((reviews, RDFS.range, paper))
g.add((assigns, RDFS.range, reviewer))
g.add((assigns, RDFS.domain, editor))
g.add((handlesJournal, RDFS.domain, editor))
g.add((handlesJournal, RDFS.range, journal))
g.add((volume, RDFS.subClassOf, journal))
# g.add((fromJournal, RDFS.domain, volume)) #Another option but volumes as subClassesOf journals is better
# g.add((fromJournal, RDFS.range, journal)) #Another option but volumes as subClassesOf journals is better
g.add((includes, RDFS.domain, volume))
g.add((journal, RDFS.subClassOf, venue))
g.add((has, RDFS.domain, venue))
g.add((has, RDFS.range, paper))
g.add((conference, RDFS.subClassOf, venue))
g.add((writes, RDFS.domain, author))
g.add((writes, RDFS.range, paper))
g.add((assigns, RDFS.domain, chair))
g.add((handlesConference, RDFS.domain, chair))
g.add((handlesConference, RDFS.range, conference))
g.add((isRelatedTo, RDFS.range, area))
g.add((isRelatedTo, RDFS.domain, paper))
g.add((isRelatedTo, RDFS.domain, journal))
g.add((isRelatedTo, RDFS.domain, conference))
g.add((proceeding, RDFS.subClassOf, conference))
# g.add((fromConference, RDFS.domain, proceeding)) #Another option but proceedings as subClassesOf conferences is better
# g.add((fromConference, RDFS.range, conference)) #Another option but proceedings as subClassesOf conferences is better
g.add((includes, RDFS.range, publication))
g.add((includes, RDFS.domain, proceeding))
g.add((reviewer, RDFS.subClassOf, author))
g.add((hasReview, RDFS.range, review))
g.add((hasReview, RDFS.domain, paper))

#Attributes
##Review
g.add((accepted, RDFS.domain, review))
g.add((accepted, RDFS.range, XSD.boolean))
g.add((back_up_text, RDFS.domain, review))
g.add((back_up_text, RDFS.range, XSD.string))
#Paper
g.add((type, RDFS.domain, paper))
g.add((type, RDFS.range, XSD.string))
g.add((updated, RDFS.domain, paper))
g.add((updated, RDFS.range, XSD.dateTimeStamp))
g.add((url, RDFS.domain, paper))
g.add((url, RDFS.range, XSD.string))
g.add((doi, RDFS.domain, paper))
g.add((doi, RDFS.range, XSD.string))
g.add((abstract, RDFS.domain, paper))
g.add((abstract, RDFS.range, XSD.string))
g.add((title, RDFS.domain, paper))
g.add((title, RDFS.range, XSD.string))
#Publication
g.add((publicationDate, RDFS.domain, publication))
g.add((publicationDate, RDFS.range, XSD.date))
#Author
g.add((name, RDFS.domain, author))
g.add((name, RDFS.range, XSD.string))
#Volume
g.add((year, RDFS.domain, volume))
g.add((year, RDFS.range, XSD.integer))
g.add((volumeNr, RDFS.domain, volume))
g.add((volumeNr, RDFS.range, XSD.integer))
#Proceedings
g.add((startDate, RDFS.domain, proceeding))
g.add((startDate, RDFS.range, XSD.date))
g.add((endDate, RDFS.domain, proceeding))
g.add((endDate, RDFS.range, XSD.date))
#Conference
g.add((conference_type, RDFS.domain, conference))
g.add((conference_type, RDFS.range, XSD.string))
g.add((name, RDFS.domain, conference))
g.add((name, RDFS.range, XSD.string))
g.add((issn, RDFS.domain, conference))
g.add((issn, RDFS.range, XSD.string))
g.add((url, RDFS.domain, conference))
g.add((url, RDFS.range, XSD.string))
#Journal
g.add((name, RDFS.domain, journal))
g.add((name, RDFS.range, XSD.string)) #Repeated if we name it the same as in confernces
g.add((issn, RDFS.domain, journal))
g.add((issn, RDFS.range, XSD.string)) #Repeated if we name it the same as in confernces
g.add((url, RDFS.domain, journal))
g.add((url, RDFS.range, XSD.string)) #Repeated if we name it the same as in confernces
#Area
g.add((area, RDFS.range, XSD.string))


# print(g.serialize())
v = g.serialize(format="nt")
g.serialize(destination="tbox.ttl", format="ttl")
# print(len(g))








