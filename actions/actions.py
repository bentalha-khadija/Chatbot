from typing import Text, List, Any, Dict
# import json, re, jsonlines
import re
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateClientForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_client_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""
        if len(str(slot_value))<=40:
            return {"name": slot_value}
        dispatcher.utter_message(text=f"{slot_value} est tres long pour un nom")
        return {"name": None}

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email` value."""
        if re.match(r"[^@]+@[^@]+\.[^@]+", slot_value):
            return {"email": slot_value}
        dispatcher.utter_message(text=f"{slot_value} n'est pas valide")
        return {"email": None}

    def validate_phone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `phone` value."""
        if len(str(slot_value))<=14:
            return {"phone": slot_value}
        dispatcher.utter_message(text=f"{slot_value} est tres long pour un numero de telephone")
        return {"phone": None}

    def validate_comment(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        dispatcher.utter_message(text="Votre commentaire est enregistré")
        return {"comment": slot_value}
    # def submit(
    #     self,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> List[EventType]:
    #     """Define what the form has to do
    #         after all required slots are filled"""
    #     # export the form reponses into a json file 
    #     # and save it in the current directory 
    #     # with the name `responses.json` using jsonlines
    #     with jsonlines.open('responses.json', mode='w') as writer:
    #         writer.write(tracker.current_slot_values())
    #     return []
    
