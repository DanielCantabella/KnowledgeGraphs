import random
import csv
import tbox
from utils import *


if __name__ == "__main__":
#LOAD TBOX
#crear funcio que inici tbox.py
    # subprocess.run(["python3", "tbox.py"])
#LOAD DATA PROPERTIES
#ABOX PAPERS
    diccIsPoster = {}
    with open('./data/papers-processed.csv', newline='', encoding='utf-8') as papers:
        reader = csv.DictReader(papers)
        for paper in reader:
            data = [paper['corpusid'], paper['title'],
                    getAbstractData(paper['corpusid']), paper['DOI'], paper['url'],
                    paper['updated'], random.choice(["short paper", "full paper", "poster", "demo paper"])]
            if data[6]=="poster" and data[0] not in diccIsPoster:
                diccIsPoster[data[0]] = True
            correctedPaperData = correctPaperData(data)
            loadPapers(correctedPaperData)

#ABOX REVIEWS
    with open('./data/reviewed-by.csv', newline='') as reviews:
        reader = csv.DictReader(reviews)
        for review in reader:
            data = [review['paperID'],review['reviewerID'],review['grade'],review['review']]
            correctedReviewData = correctReviewData(data)
            loadReviews(correctedReviewData)
#ABOX PUBLICATIONS
    diccAprovedPapers, diccNumberReviewers = getRevisions()
    with open('./data/papers-processed.csv', newline='',encoding='utf-8') as publications:
        reader = csv.DictReader(publications)
        for publication in reader:
            if diccNumberReviewers[publication['corpusid']] >= 2 and diccAprovedPapers[publication['corpusid']] > 0:
                data = [publication['corpusid'], publication['publicationdate']]
                correctedPublicationData = correctPublicationData(data)
                loadPublications(correctedPublicationData)

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
#ABOX REVIEWS
    with open('./data/reviewed-by.csv', newline='') as reviews:
        reader = csv.DictReader(reviews)
        for review in reader:
            data = [review['paperID'],review['reviewerID'],review['grade'],review['review']]
            correctedReviewData = correctReviewData(data)
            loadReviews(correctedReviewData)

#ABOX  CHAIRS
    with open('./data/chairs.csv', newline='') as chairs:
        reader = csv.DictReader(chairs)
        for chair in reader:
            data = [chair['chairID']]
            correctedChairsData = correctChairEditorData(data)
            loadChairs(correctedChairsData)
#ABOX EDITORS
    with open('./data/editors.csv', newline='') as editors:
        reader = csv.DictReader(editors)
        for editor in reader:
            data = [editor['editorID']]
            correctedEditorsData = correctChairEditorData(data)
            loadEditors(correctedEditorsData)

#LOAD OBJECT PROPERTIES
# WRITES
    with open('./data/written-by.csv', newline='') as writes:
        reader = csv.DictReader(writes)
        for write in reader:
            data = [write['authorID'],write['paperID']]
            correctedWrittenData = correctPropertiesData(data)
            loadRelations(correctedWrittenData[0], tbox.writes, correctedWrittenData[1])
# REVIEWS, SUBMITS & HAS_REVIEW
    with open('./data/reviewed-by.csv', newline='') as submits:
        reader = csv.DictReader(submits)
        for submit in reader:

            data = [submit['reviewerID'],submit['paperID']]
            correctedReviewedData = correctPropertiesData(data)
            g.add((EX[correctedReviewedData[0]], RDF.type, tbox.reviewer)) #Add reviewers first
            loadRelations(correctedReviewedData[0], tbox.reviews, correctedReviewedData[1])

            data = [submit['reviewerID'], str(submit['paperID']) + '-' + str(submit['reviewerID'])]  # review id is paperID-reviewerID
            correctedSubmittedData = correctPropertiesData(data)
            loadRelations(correctedSubmittedData[0], tbox.submits, correctedSubmittedData[1])

            data = [submit['paperID'], str(submit['paperID'])+'-'+str(submit['reviewerID'])] #review id is paperID-reviewerID
            correctedReviewData = correctPropertiesData(data)
            loadRelations(correctedReviewData[0], tbox.hasReview, correctedReviewData[1])
# IS_RELATED_TO
    #Paper
    with open('./data/related-to.csv', newline='') as relates:
        reader = csv.DictReader(relates)
        for relate in reader:
            data = [relate['paperID'],str(relate['keyword']).replace(' ', '_')]
            correctedRelatedData = correctPropertiesData(data)
            loadRelations(correctedRelatedData[0], tbox.paperRelatedTo, correctedRelatedData[1])
    #Journal
    with open('./data/journalsAreas.csv', newline='') as relates:
        reader = csv.DictReader(relates)
        for relate in reader:
            data = [relate['journalID'],str(relate['area']).replace(' ', '_')]
            correctedRelatedData = correctPropertiesData(data)
            loadRelations(correctedRelatedData[0], tbox.journalRelatedTo, correctedRelatedData[1])
    #Conference
    with open('./data/conferencesAreas.csv', newline='') as relates:
        reader = csv.DictReader(relates)
        for relate in reader:
            data = [relate['conferenceID'],str(relate['area']).replace(' ', '_')]
            correctedRelatedData = correctPropertiesData(data)
            loadRelations(correctedRelatedData[0], tbox.conferenceRelatedTo, correctedRelatedData[1])

# INCLUDES
    diccInProceeding={}
    with open('./data/belongs-to.csv', newline='') as includes: #proceeding includes publication
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['venueID'],include['paperID']]
            if diccNumberReviewers[data[1]] >= 2 and diccAprovedPapers[data[1]] > 0:
                diccInProceeding[data[1]] = True # Not really necessary. We have the constraint made in our csv files, but just in case we add more data.
                correctedIncludedData = correctPropertiesData(data)
                loadRelations(correctedIncludedData[1], tbox.includedInProceeding, correctedIncludedData[0])

    with open('./data/published-in.csv', newline='') as includes: #volume includes publication
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['venueID'],include['paperID']]
            if diccNumberReviewers[data[1]] >= 2 and diccAprovedPapers[data[1]] > 0 and data[1] not in diccIsPoster and data[1] not in diccInProceeding:
                correctedIncludedData = correctPropertiesData(data)
                loadRelations(correctedIncludedData[1], tbox.includedInVolume, correctedIncludedData[0])

# FROM_CONFERENCE
    with open('./data/is-from.csv', newline='') as includes: #proceeding subClassOf conference
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['editionID'],include['conferenceID']]
            correctedReviewedData = correctPropertiesData(data)
            loadRelations(correctedReviewedData[0], tbox.fromConference, correctedReviewedData[1])

# FROM_JOURNAL
    with open('./data/volume-from.csv', newline='') as includes: #volume subClassOf journal
        reader = csv.DictReader(includes)
        for include in reader:
            data = [include['volumeID'], include['journalID']]
            correctedReviewedData = correctPropertiesData(data)
            loadRelations(correctedReviewedData[0], tbox.fromJournal, correctedReviewedData[1])
            # loadRelations(correctedReviewedData[0], RDFS.subClassOf, correctedReviewedData[1])

# ASSIGNS
    with open('./data/affiliated-to.csv', newline='') as assigns:
        reader = csv.DictReader(assigns)
        for assign in reader:
            if assign['type'] == "editor": #editors
                data = [assign['affiliation'],assign['authorID']]
                correctedReviewedData = correctPropertiesData(data)
                loadRelations(correctedReviewedData[0], tbox.editorAssigns, correctedReviewedData[1])
            else: #chair
                data = [assign['affiliation'], assign['authorID']]
                correctedReviewedData = correctPropertiesData(data)
                loadRelations(correctedReviewedData[0], tbox.chairAssigns, correctedReviewedData[1])

# HANDLES_CONFERENCES
    with open('./data/handlesConferences.csv', newline='') as handles: #proceeding subClassOf conference
        reader = csv.DictReader(handles)
        for handle in reader:
            for i in range(1,len(handle)):
                chairID = 'chairID'+str(i)
                data = [handle[chairID],handle['conferenceID']]
                correctedReviewedData = correctPropertiesData(data)
                loadRelations(correctedReviewedData[0], tbox.handlesConference, correctedReviewedData[1])

# HANDLES_JOURNALS
    with open('./data/handlesJournals.csv', newline='') as handles: #proceeding subClassOf conference
        reader = csv.DictReader(handles)
        for handle in reader:
            for i in range(1,len(handle)):
                editorID = 'editorID'+str(i)
                data = [handle[editorID],handle['journalID']]
                correctedReviewedData = correctPropertiesData(data)
                loadRelations(correctedReviewedData[0], tbox.handlesJournal, correctedReviewedData[1])

# IS_SUBMITTED_TO
# Journals
    with open('./data/submittedInJournal.csv', newline='') as submissions: #proceeding subClassOf conference
        reader = csv.DictReader(submissions)
        for submission in reader:
            data = [submission["paperID"], submission["journalID"]]
            correctedSubmittedData = correctPropertiesData(data)
            loadRelations(correctedSubmittedData[0], tbox.isSubmittedToJournal, correctedSubmittedData[1])

# Conferences
    with open('./data/submittedInConference.csv', newline='') as submissions: #proceeding subClassOf conference
        reader = csv.DictReader(submissions)
        for submission in reader:
            data = [submission["paperID"], submission["conferenceID"]]
            correctedSubmittedData = correctPropertiesData(data)
            loadRelations(correctedSubmittedData[0], tbox.isSubmittedToConference, correctedSubmittedData[1])

print(g.serialize())
g.serialize(destination="abox.ttl", format="ttl")