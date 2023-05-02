import random
from utils import *


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