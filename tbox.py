from rdflib.namespace import RDFS, RDF, XSD, Namespace
from rdflib import Graph, URIRef, Literal, BNode

g = Graph()
# accepted = BNode()
# buck_up_text = BNode()
# decision = BNode()
# submit = BNode()
# reviewer = BNode()
# assigns = BNode()
# editor = BNode()
# handles = BNode()
# journal = BNode()
# volume = BNode()
# venue = BNode()
# to = BNode()
# reviews = BNode()
# paper = BNode()
# conference_type = BNode() #rdf:type?
# area = BNode()
# conference = BNode()
# submits = BNode()
# author = BNode()
# assigns = BNode() #Repeated
# chair = BNode()
# # handles = BNode() # Repeated
# proceedings = BNode()
# year = BNode()

EX = Namespace('http://example.org/')

accepted = EX.accepted  # http://example.org/accepted/
buck_up_text = EX.buck_up_text
decision = EX.decision
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
type = EX.type

g.add((accepted, RDFS.range, XSD.boolean))
g.add((accepted, RDFS.domain, decision))
g.add((buck_up_text, RDFS.range, XSD.string))
g.add((buck_up_text, RDFS.domain, decision))
g.add((submit, RDFS.range, decision))
g.add((submit, RDFS.domain, reviewer))
g.add((reviewer, RDFS.domain, reviews))
g.add((reviews, RDFS.range, paper))
g.add((assigns, RDFS.range, reviewer))
g.add((editor, RDFS.domain, assigns))
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
g.add((year, RDFS.domain, proceedings))
g.add((year, RDFS.range, XSD.integer))
g.add((XSD.string, RDFS.domain, area))
g.add((conference_type, RDFS.domain, conference))
g.add((conference_type, RDFS.range, XSD.string))
g.add((type, RDFS.domain, paper))
g.add((type, RDFS.range, XSD.string))

print(g.serialize())
v = g.serialize(format="nt")
g.serialize(destination="tbox.ttl")








