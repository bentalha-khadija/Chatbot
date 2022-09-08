from typing import Text, List, Any, Dict
import json, re
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateClientForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_client_form"

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""

        # validate a text if it is email or not using regex
        text =  slot_value
        if re.match(r"[^@]+@[^@]+\.[^@]+", text):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text="Veuilez entrer une adresse email valide")
            return {"email": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        """Define what the form has to do
            after all required slots are filled"""
        # export the form reponses into a json file 
        # and save it in the current directory 
        # with the name `responses.json`
        with open("responses.json", "w") as outfile:
            json.dump(tracker.form_slots_to_validate(), outfile)
        dispatcher.utter_message(text=f"Thanks for your order!")
        return []
    
