import datetime
from dateutil.relativedelta import relativedelta
from typing import Text, Dict, Any, List, Union
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction
from rasa_sdk.forms import FormAction
from access_database import InMemoryGraph

def get_entity_from_data(data):

    graph_database = InMemoryGraph()
    return graph_database.get_entity_from_data(data)

def get_attribute_from_entity(entity_type):

    graph_database = InMemoryGraph()
    return graph_database.get_attribute_from_entity(entity_type)

def get_attribute_from_data(entity_type, data):

    graph_database = InMemoryGraph()
    return graph_database.get_attribute_from_data(entity_type, data)

def get_output(entity_type,attribute,data,data_attribute):

    graph_database = InMemoryGraph()
    return graph_database.get_output(entity_type, attribute, data, data_attribute)

def get_output_list(entity_type,attribute, data):

    graph_database = InMemoryGraph()
    return graph_database.get_output_list(entity_type, attribute, data)

def check_data_attribute(entity_type,attribute,data,data_attribute):

    graph_database = InMemoryGraph()
    return graph_database.check_data_attribute(entity_type, attribute, data, data_attribute)

def get_list_output(entity_type,data,data_attribute):

    graph_database = InMemoryGraph()
    return graph_database.get_list_output(entity_type, data, data_attribute)

def mention_mapping(mention):

    graph_database = InMemoryGraph()
    return graph_database.mention_mapping(mention)

def entity_mapping(entity_type):

    graph_database = InMemoryGraph()
    return graph_database.entity_mapping(entity_type)

def attribute_mapping(attribute):

    graph_database = InMemoryGraph()
    return graph_database.attribute_mapping(attribute)

def check_date_from_entity(entity_type):

    graph_database = InMemoryGraph()
    return graph_database.check_date_from_entity(entity_type)

def check_day_from_entity(entity_type):

    graph_database = InMemoryGraph()
    return graph_database.check_day_from_entity(entity_type)

def get_output_from_date(entity_type,data,start_date,end_date):

    graph_database = InMemoryGraph()
    return graph_database. get_output_from_date(entity_type,data,start_date,end_date)

def to_str(entity: Dict[Text, Any], entity_keys: Union[Text, List[Text]]) -> Text:
    """
    Converts an entity to a string by concatenating the values of the provided
    entity keys.

    :param entity: the entity with all its attributes
    :param entity_keys: the name of the key attributes
    :return: a string that represents the entity
    """
    if isinstance(entity_keys, str):
        entity_keys = [entity_keys]

    v_list = []
    for key in entity_keys:
        _e = entity
        for k in key.split("."):
            _e = _e[k]

        if "balance" in key or "amount" in key:
            v_list.append(f"{str(_e)} €")
        elif "date" in key:
            v_list.append(_e.strftime("%d.%m.%Y (%H:%M:%S)"))
        else:
            v_list.append(str(_e))
    return ", ".join(v_list)

class ActionFAQ(FormAction):

    def name(self):
        return "action_query_FAQ"

    def run(self, dispatcher, tracker, domain):

        stage = tracker.get_slot("stage")
        confirm_entity_type = None

        if stage == "confirm_stage":

            print("Run Action FAQ confirm stage :")

            entity_refer = tracker.get_slot("confirm_entity_list")
            entity_type = tracker.get_slot("entity_type")
            mention = tracker.get_slot("mention")

            print("Detected Entity Type :")
            print(entity_type)
            print("Detected Given Mention :")
            print(mention)
            if mention is not None:
                mention_refer = int(mention_mapping(mention))


            if entity_type is None and mention is None:

                dispatcher.utter_message(
                    f"Sorry, I don't understand what do you mean."
                )

                return [SlotSet("entity_type", None),
                        SlotSet("attribute", None),
                        SlotSet("data", None),
                        SlotSet("data_attribute", None),
                        SlotSet("mention", None),
                        SlotSet("mention_date", None),
                        SlotSet("confirm_entity_list",None),
                        SlotSet("confirm_entity_type",None),
                        SlotSet("confirm_attribute",None),
                        SlotSet("confirm_data",None),
                        SlotSet("confirm_data_attribute",None),
                        SlotSet("confirm_mention_date",None),
                        SlotSet("stage",None)]

            elif entity_type is not None and mention is None:

                for i in entity_refer:
                    if entity_type == i:
                        confirm_entity_type = entity_type
                        stage = None

                if confirm_entity_type is None:
                    dispatcher.utter_message(
                        f"Sorry, I don't understand what do you mean."
                    )

                    return [SlotSet("entity_type", None),
                            SlotSet("attribute", None),
                            SlotSet("data", None),
                            SlotSet("data_attribute", None),
                            SlotSet("mention", None),
                            SlotSet("mention_date", None),
                            SlotSet("confirm_entity_list", None),
                            SlotSet("confirm_entity_type", None),
                            SlotSet("confirm_attribute", None),
                            SlotSet("confirm_data", None),
                            SlotSet("confirm_data_attribute", None),
                            SlotSet("confirm_mention_date", None),
                            SlotSet("stage", None)]

            else:

                confirm_entity_type = entity_refer[mention_refer]
                stage = None

        if stage is None:

            print("Run Action FAQ :")

            entity_type = tracker.get_slot("entity_type")
            attribute = tracker.get_slot("attribute")
            data = tracker.get_slot("data")
            data_attribute = tracker.get_slot("data_attribute")
            mention = tracker.get_slot("mention")
            mention_date = tracker.get_slot("mention_date")

            if confirm_entity_type is not None:
                entity_type = confirm_entity_type
                attribute = tracker.get_slot("confirm_attribute")
                data = tracker.get_slot("confirm_data")
                data_attribute = tracker.get_slot("confirm_data_attribute")
                mention = None
                mention_date = tracker.get_slot("confirm_mention_date")

            print("Detected Entity Type :")
            print(entity_type)
            print("Detected Attribute :")
            print(attribute)
            print("Detected Given Information :")
            print(data)
            print("Detected Given Information's Attribute :")
            print(data_attribute)
            print("Detected Given Mention :")
            print(mention)
            print("Detect Given Date Mention :")
            print(mention_date)

            if mention_date is not None:
                if entity_type is None and data is None:
                    dispatcher.utter_message(
                        f"I Sorry, I don't' understand your request, can you rephrase?"
                        )

                    return [SlotSet("entity_type", None),
                            SlotSet("attribute", None),
                            SlotSet("data", None),
                            SlotSet("data_attribute", None),
                            SlotSet("mention", None),
                            SlotSet("mention_date", None),
                            SlotSet("confirm_entity_list", None),
                            SlotSet("confirm_entity_type", None),
                            SlotSet("confirm_attribute", None),
                            SlotSet("confirm_data", None),
                            SlotSet("confirm_data_attribute", None),
                            SlotSet("confirm_mention_date", None),
                            SlotSet("stage", None)]

                elif entity_type is None and data is not None :
                    entity_type = get_entity_from_data(data)
                    print("Re-Detected Entity Type :")
                    print(entity_type)
                    if entity_type is None:
                        dispatcher.utter_message(
                            f"I Sorry, I don't' understand your request, can you rephrase?"
                            )

                        return [SlotSet("entity_type", None),
                                SlotSet("attribute", None),
                                SlotSet("data", None),
                                SlotSet("data_attribute", None),
                                SlotSet("mention", None),
                                SlotSet("mention_date", None),
                                SlotSet("confirm_entity_list", None),
                                SlotSet("confirm_entity_type", None),
                                SlotSet("confirm_attribute", None),
                                SlotSet("confirm_data", None),
                                SlotSet("confirm_data_attribute", None),
                                SlotSet("confirm_mention_date", None),
                                SlotSet("stage", None)]
                else:
                    if confirm_entity_type is None:
                        entity_refer = entity_mapping(entity_type)
                        if entity_refer != []:
                            if len(entity_refer) > 1:
                                string = f"I just detected there are {len(entity_refer)} entities, which one do you refer to?\n"
                                for i in range(len(entity_refer)):
                                    string += f"Entity {i+1} :\n- entity name : {entity_refer[i]}\n"

                                dispatcher.utter_message(
                                    string
                                    )

                                return [SlotSet("entity_type", None),
                                        SlotSet("attribute", None),
                                        SlotSet("data", None),
                                        SlotSet("data_attribute", None),
                                        SlotSet("mention", None),
                                        SlotSet("mention_date", None),
                                        SlotSet("confirm_entity_list",entity_refer),
                                        SlotSet("confirm_entity_type",None),
                                        SlotSet("confirm_attribute",attribute),
                                        SlotSet("confirm_data",data),
                                        SlotSet("confirm_data_attribute",data_attribute),
                                        SlotSet("confirm_mention_date",mention_date),
                                        SlotSet("stage", "confirm_stage")]

                        else:
                            entity_type = entity_refer[0]
                            print("Adjusted Entity Type :")
                            print(entity_type)

                IsDate = check_date_from_entity(entity_type)
                IsDay = check_day_from_entity(entity_type)
                if IsDate != 1:
                    dispatcher.utter_message(
                        f"I am sorry, it seems like {entity_type} has no date data for your request."
                        )

                    return [SlotSet("entity_type", None),
                            SlotSet("attribute", None),
                            SlotSet("data", None),
                            SlotSet("data_attribute", None),
                            SlotSet("mention", None),
                            SlotSet("mention_date", None),
                            SlotSet("confirm_entity_list", None),
                            SlotSet("confirm_entity_type", None),
                            SlotSet("confirm_attribute", None),
                            SlotSet("confirm_data", None),
                            SlotSet("confirm_data_attribute", None),
                            SlotSet("confirm_mention_date", None),
                            SlotSet("stage", None)]

                else:

                    mention_refer = mention_mapping(mention_date)
                    today = datetime.datetime.today().weekday()

                    if int(mention_refer) == 29: #next week
                        list_output = []
                        days = 8 - today
                        for i in range(7):
                            day = datetime.datetime.now() + datetime.timedelta(days=days+today+i)
                            list_output += get_output_from_date(entity_type,day,"start date","end date")
                    elif int(mention_refer) == 30: #this week
                        list_output = []
                        days = today
                        for i in range(7):
                            day = datetime.datetime.now() + datetime.timedelta(days=days-today+i)
                            list_output += get_output_from_date(entity_type,day,"start date","end date")
                    elif int(mention_refer) == 31: #last week
                        list_output = []
                        days = today - (today+1)
                        for i in range(7):
                            day = datetime.datetime.now() + datetime.timedelta(days=days-i)
                            list_output += get_output_from_date(entity_type,day,"start date","end date")
                    elif int(mention_refer) == 32: #next month
                        list_output = []
                        for i in range(32):
                            day = datetime.datetime.now() + relativedelta(months=1, day=i)
                            list_output += get_output_from_date(entity_type,day,"start date","end date")
                    elif int(mention_refer) == 33: #this month
                        list_output = []
                        for i in range(32):
                            day = datetime.datetime.now() + relativedelta(months=0, day=i)
                            list_output += get_output_from_date(entity_type,day,"start date","end date")
                    elif int(mention_refer) == 34: #last month
                        list_output = []
                        for i in range(32):
                            day = datetime.datetime.now() + relativedelta(months=-1, day=i)
                            list_output += get_output_from_date(entity_type,day,"start date","end date")
                    else:
                        if int(mention_refer) >= 8:
                            #weekday = []
                            #for i in range(7):
                            days = int(mention_refer) - 15 - today
                        elif int(mention_refer) >= 5 and int(mention_refer) < 8:
                            days = int(mention_refer)- 6
                        else:
                            dispatcher.utter_message(
                                f"I did not found the correct day in your request, can you repeat?"
                            )

                            return [SlotSet("entity_type", None),
                                    SlotSet("attribute", None),
                                    SlotSet("data", None),
                                    SlotSet("data_attribute", None),
                                    SlotSet("mention", None),
                                    SlotSet("mention_date", None),
                                    SlotSet("confirm_entity_list", None),
                                    SlotSet("confirm_entity_type", None),
                                    SlotSet("confirm_attribute", None),
                                    SlotSet("confirm_data", None),
                                    SlotSet("confirm_data_attribute", None),
                                    SlotSet("confirm_mention_date", None),
                                    SlotSet("stage", None)]

                        day = datetime.datetime.now() + datetime.timedelta(days=days)
                        list_output = get_output_from_date(entity_type,day,"start date","end date")

                    if list_output != []:
                        output_num = len(list_output)
                        list_count = 0
                        threshold = - len(list_output) + 5 + list_count
                        threshold_output = list_output[:threshold]
                        for i in range(len(list_output[:list_count])):
                            threshold_output.pop(0)
                        output = threshold_output
                        string = f"I found {output_num} results related to your request :\n"
                        n = 1
                        for i in output:
                            string += f"\nResult {n} :\n"
                            n += 1
                            for j in i:
                                if i[j] == "":
                                    string += f"- {j} : Empty\n"
                                else:
                                    string += f"- {j} : {i[j]}\n"

                        if output_num > 5:
                            string += f"I can show you only 5 results, please let me know if you want to see the next results or previous results."

                        dispatcher.utter_message(
                            string
                         )
                    else:
                        dispatcher.utter_message(
                            f"I did not found any related result to your request."
                            )

                    #day = day.strftime("%d-%b-%Y")
                return [SlotSet("entity_type", None),
                        SlotSet("attribute", None),
                        SlotSet("data", None),
                        SlotSet("data_attribute", None),
                        SlotSet("mention", None),
                        SlotSet("mention_date", None),
                        SlotSet("confirm_entity_list", None),
                        SlotSet("confirm_entity_type", None),
                        SlotSet("confirm_attribute", None),
                        SlotSet("confirm_data", None),
                        SlotSet("confirm_data_attribute", None),
                        SlotSet("confirm_mention_date", None),
                        SlotSet("list_count", list_count),
                        SlotSet("list_entity_type", entity_type),
                        SlotSet("list_attribute", None),
                        SlotSet("list_output", list_output),
                        SlotSet("stage", None)]

            if data is None:

                if mention is None:
                    dispatcher.utter_template("utter_ask_brand", tracker)

                    return [SlotSet("entity_type", None),
                            SlotSet("attribute", None),
                            SlotSet("data", None),
                            SlotSet("data_attribute", None),
                            SlotSet("mention", None),
                            SlotSet("mention_date", None),
                            SlotSet("confirm_entity_list", None),
                            SlotSet("confirm_entity_type", None),
                            SlotSet("confirm_attribute", None),
                            SlotSet("confirm_data", None),
                            SlotSet("confirm_data_attribute", None),
                            SlotSet("confirm_mention_date", None),
                            SlotSet("stage", None)]

                else:

                    mention_refer = int(mention_mapping(mention))
                    print("Mention Refer to :")
                    print(mention_refer)
                    list_output = tracker.get_slot("list_output")

                    if list_output is None:
                        dispatcher.utter_message(
                            f"I Sorry, I don't' understand your request, can you rephrase?"
                            )

                        return [SlotSet("entity_type", None),
                                SlotSet("attribute", None),
                                SlotSet("data", None),
                                SlotSet("data_attribute", None),
                                SlotSet("mention", None),
                                SlotSet("mention_date", None),
                                SlotSet("confirm_entity_list", None),
                                SlotSet("confirm_entity_type", None),
                                SlotSet("confirm_attribute", None),
                                SlotSet("confirm_data", None),
                                SlotSet("confirm_data_attribute", None),
                                SlotSet("confirm_mention_date", None),
                                SlotSet("stage", None)]

                    else:
                        output = list_output[mention_refer]

                        print("Output:")
                        print(output)
                        string = f"Here is the result for what you wanted :\n"

                        attribute = attribute_mapping(attribute)

                        if attribute is not None:
                            string += f"Result:\n- {attribute} : {output[attribute]}\n"
                        else:
                            string += f"Result:\n"
                            for j in output:
                                if output[j] == "":
                                    string += f"- {j} : Empty\n"
                                else:
                                    string += f"- {j} : {output[j]}\n"

                        dispatcher.utter_message(
                            string
                        )

                        return [SlotSet("entity_type", None),
                                SlotSet("attribute", None),
                                SlotSet("data", None),
                                SlotSet("data_attribute", None),
                                SlotSet("mention", None),
                                SlotSet("mention_date", None),
                                SlotSet("confirm_entity_list", None),
                                SlotSet("confirm_entity_type", None),
                                SlotSet("confirm_attribute", None),
                                SlotSet("confirm_data", None),
                                SlotSet("confirm_data_attribute", None),
                                SlotSet("confirm_mention_date", None),
                                SlotSet("stage", None)]

            if entity_type is None:
                entity_type = get_entity_from_data(data)
                print("Re-Detected Entity Type :")
                print(entity_type)
                if entity_type is None:
                    dispatcher.utter_message(
                        f"I Sorry, I don't' understand your request, can you rephrase?"
                        )

                    return [SlotSet("entity_type", None),
                            SlotSet("attribute", None),
                            SlotSet("data", None),
                            SlotSet("data_attribute", None),
                            SlotSet("mention", None),
                            SlotSet("mention_date", None),
                            SlotSet("confirm_entity_list", None),
                            SlotSet("confirm_entity_type", None),
                            SlotSet("confirm_attribute", None),
                            SlotSet("confirm_data", None),
                            SlotSet("confirm_data_attribute", None),
                            SlotSet("confirm_mention_date", None),
                            SlotSet("stage", None)]
            else:

                    entity_refer = entity_mapping(entity_type)
                    if entity_refer != []:
                        if len(entity_refer) > 1 and confirm_entity_type is None:
                            string = f"I just detected there are {len(entity_refer)} entities, which one do you refer to?\n"
                            for i in range(len(entity_refer)):
                                string += f"Entity {i + 1} :\n- entity name : {entity_refer[i]}\n"

                            dispatcher.utter_message(
                                string
                            )

                            return [SlotSet("entity_type", None),
                                    SlotSet("attribute", None),
                                    SlotSet("data", None),
                                    SlotSet("data_attribute", None),
                                    SlotSet("mention", None),
                                    SlotSet("mention_date", None),
                                    SlotSet("confirm_entity_list",entity_refer),
                                    SlotSet("confirm_entity_type",None),
                                    SlotSet("confirm_attribute",attribute),
                                    SlotSet("confirm_data",data),
                                    SlotSet("confirm_data_attribute",data_attribute),
                                    SlotSet("confirm_mention_date",mention_date),
                                    SlotSet("stage","confirm_stage")]

                        else:
                            entity_type = entity_refer[0]
                            print("Adjusted Entity Type :")
                            print(entity_type)


            if attribute is not None and data_attribute is not None:
                attribute, data_attribute = check_data_attribute(entity_type, attribute, data, data_attribute)
                print("Re-detected attribute and data attribute:")
                print(attribute)
                print(data_attribute)

            if data_attribute is None:
                data_attribute = get_attribute_from_data(entity_type, data)

            list_output = get_output(entity_type, attribute, data, data_attribute)

            if list_output != []:

                output_num = len(list_output)
                list_count = 0
                threshold = - len(list_output) + 5 + list_count
                threshold_output = list_output[:threshold]
                for i in range(len(list_output[:list_count])):
                    threshold_output.pop(0)
                output = threshold_output

                string = f"I found {output_num} results related to your request :\n\n"

                n = 1
                for i in output:
                    string += f"\nResult {n} :\n\n"
                    n += 1
                    for j in i:
                        attribute = attribute_mapping(attribute)
                        if attribute is None:
                            if i[j] == "":
                                string += f"- {j} : Empty\n\n"
                            else:
                                string += f"- {j} : {i[j]}\n\n"
                        else:
                            if j == attribute:
                                if i[j] == "":
                                    string += f"- {j} : Empty\n\n"
                                else:
                                    string += f"- {j} : {i[attribute]}\n\n"

                if output_num > 5:
                    string += f"I can show you only 5 results, please let me know if you want to see the next results or previous results."
                dispatcher.utter_message(
                    string
                )
                return [SlotSet("entity_type", None),
                        SlotSet("attribute", None),
                        SlotSet("data", None),
                        SlotSet("data_attribute", None),
                        SlotSet("mention", None),
                        SlotSet("mention_date", None),
                        SlotSet("confirm_entity_list", None),
                        SlotSet("confirm_entity_type", None),
                        SlotSet("confirm_attribute", None),
                        SlotSet("confirm_data", None),
                        SlotSet("confirm_data_attribute", None),
                        SlotSet("confirm_mention_date", None),
                        SlotSet("list_count", list_count),
                        SlotSet("list_entity_type", entity_type),
                        SlotSet("list_attribute", attribute),
                        SlotSet("list_output", list_output),
                        SlotSet("stage", None)]
            else:
                dispatcher.utter_message(
                    f"I did not found any related result to your request."
                )

                return [SlotSet("entity_type", None),
                        SlotSet("attribute", None),
                        SlotSet("data", None),
                        SlotSet("data_attribute", None),
                        SlotSet("mention", None),
                        SlotSet("mention_date", None),
                        SlotSet("confirm_entity_list", None),
                        SlotSet("confirm_entity_type", None),
                        SlotSet("confirm_attribute", None),
                        SlotSet("confirm_data", None),
                        SlotSet("confirm_data_attribute", None),
                        SlotSet("confirm_mention_date", None),
                        SlotSet("stage", None)]

class ActionList(FormAction):

    def name(self):
        return "action_query_list"

    def run(self, dispatcher, tracker, domain):
        print("Run action list")

        if tracker.get_slot("list_count") is None or tracker.get_slot("list_decision") is None:
            dispatcher.utter_message(f"Sorry, I do not understand what do you mean.")
            return []
        else:
            list_count = tracker.get_slot("list_count")
            entity_type = tracker.get_slot("list_entity_type")
            attribute = tracker.get_slot("list_attribute")
            list_output = tracker.get_slot("list_output")
            """"
            attribute = tracker.get_slot("list_attribute")
            data = tracker.get_slot("list_data")
            data_attribute = tracker.get_slot("list_data_attribute")
            print("data_attribute")
            print(data_attribute)
        output = get_output(entity_type, attribute, data, data_attribute)
        print("Output:")
        print(output)
        """""
        output_num = len(list_output)

        if output_num > 5:

            if tracker.get_slot("list_decision") == "next":
                list_count = list_count + 5
            elif tracker.get_slot("list_decision") == "previous":
                list_count = list_count - 5

            if list_count < 0:
                list_count = 0
            if list_count == len(list_output):
                list_count -= 5

            threshold = - len(list_output) + 5 + list_count

            if threshold > 0:
                threshold *= len(list_output)
            elif threshold == 0:
                threshold = list_count + 5

            threshold_output = list_output[:threshold]

            for i in range(len(list_output[:list_count])):
                threshold_output.pop(0)

            output = threshold_output

        string = f"I found {output_num} results related to your request :\n"

        n = 1 + list_count
        for i in output:
            string += f"\nResult {n} :\n"
            n += 1
            for j in i:
                if attribute is None:
                    if i[j] == "":
                        string += f"- {j} : Empty\n"
                    else:
                        string += f"- {j} : {i[j]}\n"
                else:
                    if j == attribute:
                        if i[j] == "":
                            string += f"- {j} : Empty\n"
                        else:
                            string += f"- {j} : {i[attribute]}\n"

        if output_num > 5:
            string += f"I can show you only 5 results, please let me know if you want to see the next results or previous results."

        dispatcher.utter_message(
            string
        )

        return [SlotSet("list_count", list_count),
                SlotSet("list_entity_type", entity_type),
                SlotSet("list_attribute", attribute),
                SlotSet("list_output", list_output)]


