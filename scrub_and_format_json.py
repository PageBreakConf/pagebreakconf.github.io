import csv
import json
import re

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
list_type = sys.argv[3]
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    data = {}     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        counter = 1
        for rows in csvReader:
            key = counter
            data[key] = rows
            counter += 1
    return data

def clean_data(data):
    skip = ["Email", "Registered", "Phone", "Notes", "SubmittedSessions", "Owner", "NeedsTravelAssistance", "TravelAssistanceAmount", "Attachments", "WebsiteStatus", "Emailed", "ResponsibleTeamMember", "Submitter"]
    newdict = []
    newdict2 = []
    for item in data:
        new_item = {}
        for j, w in data[item].items():
            neww = w
            newj = j
            newj = re.sub("\\\ufeff", "", newj)
            newj = re.sub("[^a-zA-Z0-9]", "", newj)
            if newj not in skip:
                if newj == "Sortindex":
                  if neww == "" or neww is None:
                    neww = "100"
                elif newj == "Headshot":
                  neww = re.sub("^.*\(", "", neww)
                  neww = re.sub("\)", "", neww)
                new_item[newj] = neww
        if list_type == "sessions" and re.match("2", new_item["Sortindex"]) is not None:
            newdict2.append(new_item)
        else:
            newdict.append(new_item)
    # write the output
    data = parse_data(newdict)
    if len(newdict2) > 0:
        data2 = parse_data(newdict2)
        filepath1 = re.sub("\.json", "1.json", jsonFilePath)
        filepath2 = re.sub("\.json", "2.json", jsonFilePath)
        write_data(data, filepath1)
        write_data(data2, filepath2)
    else:
        write_data(data, jsonFilePath)
    return data

def parse_data(newdict):
    parsed_data = json.dumps(newdict, indent=4, ensure_ascii=False)
    parsed_data = re.sub(r"\u201c", '&ldquo;', parsed_data)
    parsed_data = re.sub(r"\u201d", '&rdquo;', parsed_data)
    parsed_data = re.sub(r"\u2019", "'", parsed_data)
    parsed_data = re.sub(r"\xa0", " ", parsed_data)
    parsed_data = re.sub(r"\u2014", '&#8212;', parsed_data)
    parsed_data = re.sub(r"\u2013", '&#8211;', parsed_data)
    parsed_data = re.sub(r"\xe7", '&ccedil;', parsed_data)
    parsed_data = re.sub("\\\\n", "<br />", parsed_data) 
    return parsed_data 

def write_data(data, filepath):
  with open(filepath, 'w', encoding='utf-8') as jsonf:
      jsonf.write(data)
  return

csvFilePath = input_file
jsonFilePath = output_file
 
# Call the make_json function
data = make_json(csvFilePath, jsonFilePath)
data = clean_data(data)

