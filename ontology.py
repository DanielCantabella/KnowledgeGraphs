import tbox
from abox import *

#Classes
g.add((tbox.paper,RDF.type, RDFS.Class))
g.add((tbox.review,RDF.type, RDFS.Class))
g.add((tbox.author,RDF.type, RDFS.Class))
g.add((tbox.reviewer,RDF.type, RDFS.Class))
g.add((tbox.publication,RDF.type, RDFS.Class))
g.add((tbox.editor,RDF.type, RDFS.Class))
g.add((tbox.chair,RDF.type, RDFS.Class))
g.add((tbox.venue,RDF.type, RDFS.Class))
g.add((tbox.journal,RDF.type, RDFS.Class))
g.add((tbox.conference,RDF.type, RDFS.Class))
g.add((tbox.volume,RDF.type, RDFS.Class))
g.add((tbox.proceeding,RDF.type, RDFS.Class))
g.add((tbox.area,RDF.type, RDFS.Class))

#Properties
g.add((tbox.submits,RDF.type, RDF.Property))
g.add((tbox.hasReview,RDF.type, RDF.Property))
g.add((tbox.reviews,RDF.type, RDF.Property))
g.add((tbox.writes,RDF.type, RDF.Property))
g.add((tbox.assigns,RDF.type, RDF.Property))
g.add((tbox.handlesConference,RDF.type, RDF.Property))
g.add((tbox.handlesJournal,RDF.type, RDF.Property))
g.add((tbox.isRelatedTo,RDF.type, RDF.Property))
g.add((tbox.includes,RDF.type, RDF.Property))
g.add((tbox.has,RDF.type, RDF.Property))
g.add((tbox.fromJournal,RDF.type,RDF.Property)) #
g.add((tbox.fromConference,RDF.type,RDF.Property)) #

#Attributes (also properties)
g.add((tbox.back_up_text, RDF.type, RDF.Property))
g.add((tbox.accepted, RDF.type, RDF.Property))
g.add((tbox.name_author, RDF.type, RDF.Property))
g.add((tbox.type, RDF.type, RDF.Property))
g.add((tbox.updated, RDF.type, RDF.Property))
g.add((tbox.url, RDF.type, RDF.Property))
g.add((tbox.doi, RDF.type, RDF.Property))
g.add((tbox.abstract, RDF.type, RDF.Property))
g.add((tbox.title, RDF.type, RDF.Property))
g.add((tbox.publicationDate, RDF.type, RDF.Property))
g.add((tbox.startDate, RDF.type, RDF.Property))
g.add((tbox.endDate, RDF.type, RDF.Property))
g.add((tbox.year, RDF.type, RDF.Property))
g.add((tbox.volumeNr, RDF.type, RDF.Property))
g.add((tbox.conference_type, RDF.type, RDF.Property))
g.add((tbox.name, RDF.type, RDF.Property))
g.add((tbox.issn, RDF.type, RDF.Property))


print(g.serialize())
g.serialize(destination="ontology.ttl", format="ttl")