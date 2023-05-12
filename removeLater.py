import pandas as pd

# Read the CSV files
published = pd.read_csv("/Users/danicantabella/Desktop/SDM/Labs/Lab3/data/belongs-to.csv")
volume = pd.read_csv("/Users/danicantabella/Desktop/SDM/Labs/Lab3/data/is-from.csv")

combined_df = pd.concat([published["paperID"],published["venueID"], published["venueID"]], axis=1)
new = pd.DataFrame()
for i in published["venueID"]:
    # print(i)
    new = pd.concat([new, volume[volume["editionID"]==i]["conferenceID"]], axis=0)
new.to_csv("/Users/danicantabella/Desktop/SDM/Labs/Lab3/data/newww.csv", index=False)
# combined_df = pd.concat([combined_df, new], axis=1)
combined_df.to_csv("/Users/danicantabella/Desktop/SDM/Labs/Lab3/data/submittedInConference.csv", index=False)
