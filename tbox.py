from rdflib.namespace import RDFS, RDF, XSD, Namespace
from rdflib import Graph, URIRef, Literal, BNode

g = Graph()
EX = Namespace('http://example.org/')
g.bind('ex', EX) #Bind prefix to namespace


decision = EX.decision # http://example.org/decision/
submit = EX.submit
reviewer = EX.reviewer
assigns = EX.assigns
editor = EX.editor
handles = EX.handles
journal = EX.journal
volume = EX.volume
venue = EX.venue
to = EX.to
reviews = EX.reviews
paper = EX.paper
conference_type = EX.conference_type
area = EX.area
conference = EX.conference
submits = EX.submits
author = EX.author
chair = EX.chair
proceedings = EX.proceedings
year = EX.year

#Attributes
#Decision
accepted = EX.accepted
buck_up_text = EX.buck_up_text
#Paper
type = EX.type
title = EX.title
updated = EX.updated
url = EX.url #Repeated
doi = EX.doi
abstract = EX.abstract
publicationDate = EX.publicationDate
#Author
name = EX.name #Repeated
#Volume
year = EX.year
#Proceedings
startDate = EX.startDate
endDate = EX.endDate
#Conference/ Journal
name = EX.name #Repeated
issn = EX.issn
conferenceType = EX.conferenceType #Only for conferences
url = EX.url #Repeated

# Triples
g.add((submit, RDFS.range, decision))
g.add((submit, RDFS.domain, reviewer))
g.add((reviews, RDFS.domain, reviewer))
g.add((reviews, RDFS.range, paper))
g.add((assigns, RDFS.range, reviewer))
g.add((assigns, RDFS.domain, editor))
g.add((handles, RDFS.domain, editor))
g.add((handles, RDFS.range, journal))
g.add((volume, RDFS.domain, journal))
g.add((volume, RDFS.range, paper))
g.add((venue, RDFS.subClassOf, journal))
g.add((to, RDFS.domain, venue))
g.add((to, RDFS.range, paper))
g.add((venue, RDFS.subClassOf, conference))
g.add((assigns, RDFS.range, reviewer))
g.add((submits, RDFS.domain, author))
g.add((submits, RDFS.range, paper))
g.add((assigns, RDFS.domain, chair))
g.add((handles, RDFS.domain, chair))
g.add((handles, RDFS.range, conference))
g.add((area, RDFS.domain, paper))
g.add((area, RDFS.domain, journal))
g.add((area, RDFS.domain, conference))
g.add((proceedings, RDFS.domain, conference))
g.add((proceedings, RDFS.range, paper))

#Attributes
##Decision
g.add((accepted, RDFS.domain, decision))
g.add((accepted, RDFS.range, XSD.boolean))
g.add((buck_up_text, RDFS.domain, decision))
g.add((buck_up_text, RDFS.range, XSD.string))
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
g.add((publicationDate, RDFS.domain, paper))
g.add((publicationDate, RDFS.range, XSD.date))
#Author
g.add((name, RDFS.domain, author))
g.add((name, RDFS.range, XSD.string))
#Volume
g.add((year, RDFS.domain, volume))
g.add((year, RDFS.range, XSD.integer))
#Proceedings
g.add((startDate, RDFS.domain, proceedings))
g.add((startDate, RDFS.range, XSD.date))
g.add((endDate, RDFS.domain, proceedings))
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
g.add((XSD.string, RDFS.domain, area))


# print(g.serialize())
v = g.serialize(format="nt")
g.serialize(destination="tbox.ttl", format="ttl")
# print(len(g))








