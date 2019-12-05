import logging
import json
import glob, os
import datetime

from typing import List, Dict, Any, Optional, Text
#from datetime import date, datetime
from grakn.client import GraknClient
from dateutil.parser import parse

logger = logging.getLogger(__name__)


class KnowledgeBase(object):

    def get_entities(
        self,
        entity_type: Text,
        attributes: Optional[List[Dict[Text, Text]]] = None,
        limit: int = 5,
    ) -> List[Dict[Text, Any]]:

        raise NotImplementedError("Method is not implemented.")

    def get_attribute_of(
        self, entity_type: Text, key_attribute: Text, entity: Text, attribute: Text
    ) -> List[Any]:

        raise NotImplementedError("Method is not implemented.")

    def validate_entity(
        self, entity_type, entity, key_attribute, attributes
    ) -> Optional[Dict[Text, Any]]:

        raise NotImplementedError("Method is not implemented.")

class InMemoryGraph(KnowledgeBase):
            """
            If you don't want to use a graph database and you just have a few data points, you
            can also store your domain knowledge, for example, in a dictionary.
            This class is an example class that uses a python dictionary to encode some domain
            knowledge about banks.
            """
            ## Load Data From Json

            def __init__(self):

                global ID
                ID = "CB16036"

            def get_attribute_from_entity(self, entity_type: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json','')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())

                for i in input :
                    if i == entity_type :
                        for j in input[i]:
                            key_value_list = j
                            return key_value_list

                return None

            def get_attribute_from_data(self, entity_type: Text, data: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json','')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if data.lower() in i[j].lower():
                            return j
                return None

            def get_data_from_entity(self, entity_type: Text, data: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json','')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if i[j].lower() == data.lower():
                            return j
                return None

            def get_entity_from_data(self, data: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json','')
                        database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{file}.json"
                        input = json.loads(open(database).read())
                        for i in input:
                            for j in i:
                                if data.lower() in i[j].lower() :
                                    return file
                return None

            def get_output(self, entity_type: Text, attribute: Text, data: Text, data_attribute: Text) -> Text:

                output = []

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json','')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())

                for i in input :
                    print(i)
                    for j in i :
                        if j == data_attribute:
                            if data.lower() in i[j].lower():
                                output.append(i)

                return output

            def get_output_list(self, entity_type: Text, attribute: Text, data: Text) -> Text:

                output_list = []
                list_output = []

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json', '')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if i[j].lower() == data.lower():
                            if attribute is None:
                                for k in i:
                                    if i[k] == "":
                                        str = f"{k} : Empty"
                                    else:
                                        str = f"{j} : {i[k]}"
                                    output_list.append(str)
                            else:
                                if i[j] == "":
                                    str = f"{j} : Empty"
                                else:
                                    str = f"{j} : {i[attribute]}"
                                output_list.append(str)

                            return output_list
                return []

            def get_list_output(self, entity_type: Text, data: Text, data_attribute: Text) -> Text:

                list_output = []
                print(entity_type)
                print(data)
                print(data_attribute)

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json', '')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())

                for i in input:
                    print("data")
                    print(data)
                    print("i[data_attribute]")
                    print(i[data_attribute])
                    if data.lower() in i[data_attribute].lower():
                        list_output.append(i)

                return list_output

            def check_data_attribute(self, entity_type: Text, attribute: Text, data: Text, data_attribute: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json', '')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if j == attribute:
                            if data.lower() in i[j].lower():
                                return data_attribute, attribute
                for i in input:
                    for j in i:
                        if j == data_attribute:
                            if data.lower() in i[j].lower():
                                return attribute, data_attribute

                return attribute, None

            def mention_mapping(self, mention: Text) -> Text:

                database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base/mention_mapping.json"
                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if i[j].lower() in mention.lower():
                            return i["mapping_key"];

                return None

            def entity_mapping(self, entity_type: Text) -> Text:

                entity_refer = []
                database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base/entity_mapping.json"
                input = json.loads(open(database).read())
                for i in input:
                    if entity_type.lower() == i["mention_key"]:
                        entity_refer.append (i["mapping_key"])

                return entity_refer

            def attribute_mapping(self, attribute: Text) -> Text:

                database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base/attribute_mapping.json"
                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if i[j].lower() in attribute.lower():
                            return i["mapping_key"];

                return None

            def check_date_from_entity(self, entity_type: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json', '')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if is_date(i[j]):
                            return 1
                return 0

            def check_day_from_entity(self, entity_type: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json', '')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())
                for i in input:
                    for j in i:
                        if i[j] == "monday" or i[j] == "tuesday" or i[j] == "wednesday" or i[j] == "thursday" or i[j] == "friday" or i[j] == "saturday" or i[j] == "sunday" :
                            return 1
                return 0

            def get_output_from_date(self, entity_type: Text, data: Text, start_date: Text, end_date: Text) -> Text:

                global ID

                directory = ["/", "/Public Information/", f"/Private Information/{ID}/"]
                for n in directory:
                    os.chdir(f'C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}')
                    for file in glob.glob("*.json"):
                        file = file.replace('.json', '')
                        if file == entity_type:
                            database = f"C:/Users/USER/PycharmProjects/CRS chatbot/knowledge_base{n}{entity_type}.json"

                input = json.loads(open(database).read())
                output = []
                data = data.strftime('%d/%m/%Y')

                for i in input:
                    i[start_date] = datetime.datetime.strptime(i[start_date], '%d/%m/%Y').strftime('%d/%m/%Y')
                    i[end_date] = datetime.datetime.strptime(i[end_date], '%d/%m/%Y').strftime('%d/%m/%Y')

                    if i[start_date] <= data <= i[end_date]:
                        output.append(i)

                return output


def is_date(string, fuzzy=False):

    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False