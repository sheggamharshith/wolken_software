# This files contains your custom actions which can be used to run
# custom Python code.
## Note : This customized and build only for the wolken-software please refer
# for further documentation   

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from TokenValidationCode import wapitest,Regex_validtor,file_saving
from requests.auth import HTTPBasicAuth
import requests
import json
from rasa_sdk.forms import FormAction


# please do follow code for you further reference  
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

######################################### This is for the initlizing the Json Text########################################### 
def file_saver(json_format):
    json_dump_out_put = json.dumps(json_format)
    requiredData = json.loads(json_dump_out_put)
    #print(requiredData["message"])
    with open("just.pdf", "w") as outfile:
        outfile.write(json_format) 
    input_string = ''
    for x in requiredData["data"]:
        print("{}".format(requiredData["data"][x])) 
    return requiredData
########################################### initlizing the custom action validation#################################


class Email(FormAction):
    """Collects Email information and adds it to the Api"""
    def name(self):
        return "Email_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "Email",
            "FirstName",
            ]
    # validating the email id if you want have any custom email id regex equation 
    # already imported the module just pass tha regex patter
    # def validate_Email(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate Email value."""

    #     if Regex_validator("<patter>",value): -----> change the regex pattern
    #         # validation succeeded, if the ducker recognize it as email
    #         return {"Email": value}
    #     else:
    #         dispatcher.utter_message(template="You have provide us with an incorrect email id format please check and try-again")
    #         # validation failed, set this slot to None, meaning the
    #         # user will be asked for the slot(Email) again
    #         return {"Email": None}

    def validate_Email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate Email value."""
        print(value)
        return {"Email": value}
    def slot_mappings(self):
        """This function will map the intent of the text"""
        return {
        "Email": [self.from_entity(entity="email"),], # This maps the duckling email id
        "FirstName":[self.from_entity(entity="FirstName"),
                    self.from_entity(intent="infrom", entity="FirstName"),
                    self.from_entity(entity="PERSON"),
                    self.from_entity(entity="FirstName"),self.from_text()
          ]
        }
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        '''This function will submit the form'''
        print("I have received the Email id: {}".format(tracker.get_latest_entity_values("Email")))
        dispatcher.utter_message("Saving your email id as {}".format(tracker.get_slot("Email")))
        return []

####################################---This form is for asking  the request id ----#################################################

class requestId(FormAction):
    """Collects request id and adds it to the Api"""
    def name(self):
        return "requestId_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "requestId"
            ]
    def slot_mappings(self):
        """This function will map the intent of the text"""
        return {
        "requestId": [self.from_entity(entity="requestId"),
                    self.from_entity(entity="requestId"),self.from_text(),]
        }
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        '''This function will submit the form'''
        print("I have received the Email id: {}".format(tracker.get_latest_entity_values("Email")))
        dispatcher.utter_message("Saving your request id as {}".format(tracker.get_slot("requestId")))
        return []
        
####################################---This for generating the token---#################################################

class GetAllStatusCode(Action):
    """ This class will do custom api and generate the token """
    """  The modules are imported from the wapitest please make sure go through the function block of the code"""
    def name(self) -> Text:
        return "action_Get_all_status_Token"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            print("this is form the get all request Generation")
            generatedToken = wapitest.login_module()
            print(generatedToken)
            dispatcher.utter_message(text="Here is you token for you validation {}".format(generatedToken))
            generatedJson = wapitest.get_All_Request(generatedToken , tracker.get_slot("Email"))
            print(generatedJson.json())
            dispatcher.utter_message(text="now geting the json for you this {}".format(generatedJson.json()))
        except Exception as e:
            dispatcher.utter_message(text="Sorry there something wrong 😖 with the token.Please contact to the management🏢")
            print("This is an error from the generate token in  action server!!!!!!!!!!!!!")
            print(e)
        return []

####################################This for generating the create request token#################################################

class CreaterequestToken(Action):
    """ This class will do custom api and generate the token """
    """  The modules are imported from the wapitest please make sure go through the function block of the code"""
    def name(self) -> Text:
        return "action_Create_request_Token"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            print("this went to the the create request token")
            generatedToken = wapitest.login_module()
            print(generatedToken)
            dispatcher.utter_message(text="Here is you token for you validation {}".format(generatedToken))
            generatedJson = wapitest.create_Request(generatedToken , tracker.get_slot("Email"),tracker.get_slot("FirstName"))
            #json_format = generatedJson.json()
            #file_saving.file_saver(json_format)
            dispatcher.utter_message(text="now geting the json for you this {}".format(generatedJson))
        except Exception as e:
            dispatcher.utter_message(text="Sorry there something wrong 😖 with the token.Please contact to the management🏢")
            print("This is an error from the create token in  custom action server")
            print(e)
        return []

####################################This for the update request token#################################################

class updaterequestToken(Action):
    """ This class will do custom api and generate the token """
    """  The modules are imported from the wapitest please make sure go through the function block of the code"""
    def name(self) -> Text:
        return "action_update_request_Token"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            print("this went to the the update request token")
            generatedToken = wapitest.login_module()
            print(generatedToken)
            dispatcher.utter_message(text="Here is you token for you validation {}".format(generatedToken))
            generatedJson = wapitest.update_request(generatedToken , tracker.get_slot("Email"),tracker.get_slot("requestId"))
            #json_format = generatedJson.json()
            dispatcher.utter_message(text="now geting the json for you this {}".format(generatedJson))
        except Exception as e:
            dispatcher.utter_message(text="Sorry there something wrong 😖 with the token.Please contact to the management🏢")
            print("This is an error form the update request in custom action server")
            print(e)
        return []

####################################This for generating the update case token#################################################

class getCaserequestToken(Action):
    """ This class will do custom api and generate the token """
    """  The modules are imported from the wapitest please make sure go through the function block of the code"""
    def name(self) -> Text:
        return "action_getcase_request_Token"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            print("this is form the getcase ticket status")
            print("this went to the the getcase request token")
            generatedToken = wapitest.login_module()
            print(generatedToken)
            dispatcher.utter_message(text="Here is you token for you validation {}".format(generatedToken))
            generatedJson = wapitest.get_case_details(generatedToken , tracker.get_slot("Email"))
            #json_format = generatedJson.json()
            #file_saving.file_saver(json_format)
            dispatcher.utter_message(text="now geting the json for you this {}".format(generatedJson.json()))
        except Exception as e:
            dispatcher.utter_message(text="Sorry there something wrong 😖 with the token.Please contact to the management🏢")
            print("This is an error from the get case details in custom action server")
        return []

####################################---This for closing  token ---#################################################

class closerequestToken(Action):
    """ This class will do custom api and generate the token """
    """  The modules are imported from the wapitest please make sure go through the function block of the code"""
    def name(self) -> Text:
        return "action_close_request_Token"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            print("this went to the the close request token")
            generatedToken = wapitest.login_module()
            print(generatedToken)
            dispatcher.utter_message(text="Here is you token for you validation {}".format(generatedToken))
            generatedJson = wapitest.close_Request(generatedToken , tracker.get_slot("Email"),tracker.get_slot("requestId"))
            #json_format = generatedJson.json()
            #file_saving.file_saver(json_format)
            dispatcher.utter_message(text="now geting the json for you this {}".format(generatedJson))
        except  Exception as e:
            dispatcher.utter_message(text="Sorry there something wrong 😖 with the token.Please contact to the management🏢")
            print("This is an error from the close request in custom action server")
            print(e)
        return []
