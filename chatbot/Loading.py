import csv
import json
import glob, os, sys
import nltk
from nltk.corpus import wordnet

entity_type = ""
data = ""
attribute = ""
mention = ""

id = "CB16036"
exist = 0

folder = ["/","/Public Information/",f"/Private Information/{id}/"]

for amount in folder:
    if amount == f"/Private Information/{id}/":
        for x in os.listdir(f'C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base/Private Information/'):
            if id == x:
                exist = 1
        if exist == 0:
            print("ID doesn't exist")
            sys.exit()

    os.chdir(f'C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base{amount}')
    for file in glob.glob("*.csv"):
        file = file.replace('.csv', '')
        csvFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base{amount}{file}.csv"
        jsonFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base{amount}{file}.json"
        lookupDataPath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/data/lookup_tables/data.txt"
        lookupAttributePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/data/lookup_tables/attribute.txt"
        lookupEntityTypePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/data/lookup_tables/entity.txt"
        lookupMentionPath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/data/lookup_tables/mention.txt"

        arr = []
        synonyms = []
        antonyms = []
        entity_type_temp = []
        data_temp = []
        attribute_temp = []
        mention_temp = []

        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for csvRow in csvReader:
                for csvColumn in csvRow:
                    if isinstance(csvRow[csvColumn], str):
                        csvRow[csvColumn] = csvRow[csvColumn].lower()
                arr.append(csvRow)

            for i in arr:
                for j in i:
                    if file == "entity_mapping":
                        if j == "mention_key":
                            entity_type_temp.append(i[j])
                            for syn in wordnet.synsets(i[j]):
                                for l in syn.lemmas():
                                    synonyms.append(l.name())
                        for i in set(synonyms):
                            entity_type_temp.append(i)

                    elif file == "attribute_mapping":
                        if j == "mention_key":
                            attribute_temp.append(i[j])
                            for syn in wordnet.synsets(i[j]):
                                for l in syn.lemmas():
                                    synonyms.append(l.name())
                        for i in set(synonyms):
                            attribute_temp.append(i)

                    elif file == "mention_mapping":
                        if j == "mention_key":
                            mention_temp.append(i[j])
                            for syn in wordnet.synsets(i[j]):
                                for l in syn.lemmas():
                                    synonyms.append(l.name())
                        for i in set(synonyms):
                            mention_temp.append(i)
                    else:
                        data_temp.append(i[j])

        for i in set(attribute_temp):
            attribute += f"{i}\n"
        for i in set(mention_temp):
            mention += f"{i}\n"
        for i in set(entity_type_temp):
            entity_type += f"{i}\n"
        for i in set(data_temp):
            data += f"{i}\n"

        with open(jsonFilePath, 'w')as jsonFile:
            jsonFile.write(json.dumps(arr, indent=4))

f = open(lookupDataPath, "w")
f.write(data)
f.close()
f = open(lookupAttributePath, "w")
f.write(attribute)
f.close()
f = open(lookupEntityTypePath, "w")
f.write(entity_type)
f.close()
f = open(lookupMentionPath, "w")
f.write(mention)
f.close()

""""
arr = []

csvFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base/mention_mapping.csv"
jsonFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base/mention_mapping.json"

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath, 'w')as jsonFile:
    jsonFile.write(json.dumps(arr, indent=4))

arr = []

csvFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base/entity_mapping.csv"
jsonFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base/entity_mapping.json"

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath, 'w')as jsonFile:
    jsonFile.write(json.dumps(arr, indent=4))

arr = []

csvFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base/attribute_mapping.csv"
jsonFilePath = f"C:/Users/USER/PycharmProjects/CRS Chatbot/knowledge_base/attribute_mapping.json"

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath, 'w')as jsonFile:
    jsonFile.write(json.dumps(arr, indent=4))
"""""