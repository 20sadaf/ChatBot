from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionGetExamDates(Action):
    def name(self):
        return "action_get_exam_dates"

    def run(self, dispatcher, tracker, domain):
        exam_dates = {
            "AI": "June 15, 2024",
            "Python": "May 28, 2024",
            "Data Science": "July 10, 2024"
        }
        response = "Here are the upcoming exam dates:\n"
        for course, date in exam_dates.items():
            response += f"{course}: {date}\n"
        dispatcher.utter_message(text=response)
        return []

class ActionRandomMotivation(Action):
    def name(self):
        return "action_random_motivation"

    def run(self, dispatcher, tracker, domain):
        quotes = [
            "Keep pushing forward!",
            "Never give up on learning!",
            "Success is the sum of small efforts."
        ]
        dispatcher.utter_message(text=random.choice(quotes))
        return []
