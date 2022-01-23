# Add our dependencies
import csv
import os

# Retrive Data
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)
    


# 1. Total number of votes
# 2. Complete list of candidates
# 3. Percentage of votes for per candiate
# 4. Total number of votes per candidate 
# 5. Winner of election based on popular vote