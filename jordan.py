import requests
import json
import time
import random

TOKEN = "" 
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def start_workout(chat_id):
    # Logic to start the workout based on the day and any swaps made
    return "Starting workout..."


# Define a dictionary to hold the chat state and other necessary information
chat_states = {}

def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            state = chat_states.get(chat_id, 'start')

            if state == 'start':
                if text.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                    workout_message = get_workout_for_day(text.lower())
                    send_message(workout_message, chat_id)
                    chat_states[chat_id] = 'confirm_workout'
                else:
                    send_message("What day of the week is it? Please enter a day to get your workout plan.", chat_id)

            elif state == 'confirm_workout':
                if text.lower() == 'yes':
                    # Assume that the workout details are a multi-line string
                    workout_details = get_workout_details(chat_id)
                    send_message(workout_details, chat_id)
                    chat_states[chat_id] = 'workout_details'
                elif text.lower() == 'no':
                    send_message("Which day would you like to workout then? Please enter the day.", chat_id)
                    chat_states[chat_id] = 'start'
                else:
                    send_message("Do you want to proceed with this workout? Reply with 'yes' or 'no'.", chat_id)

            elif state == 'workout_details':
                if text.lower() == 'start':
                    # Here, you can include details about starting the workout
                    send_message("Great, let's start the workout!", chat_id)
                    # You may transition to another state or end the interaction
                elif text.lower() == 'swap':
                    send_message("Which exercise would you like to swap? Please enter the number.", chat_id)
                    chat_states[chat_id] = 'swap_exercise'
                else:
                    send_message("Please reply with 'start' to begin the workout or 'swap' to swap an exercise.", chat_id)

            elif state == 'swap_exercise':
                # Add logic to handle swapping of exercises
                # This could include presenting options and confirming the swap
                # ...
                pass

            # ... handle other states as needed ...

        except KeyError:
            continue

def get_workout_details(chat_id):
    # Retrieve the day from the chat_states
    day = chat_states.get(chat_id, {}).get("workout_day")

    # Define workout plans for each day
    workouts = {
        "monday": "Legs workout: [list exercises for legs]",
        "tuesday": "Chest workout: [list exercises for chest]",
        "wednesday": "Pull workout: [list exercises for pull]",
        "thursday": "Rest day: Take it easy, maybe some light cardio or stretching.",
        "friday": "Arms workout: [list exercises for arms]",
        "saturday": "Legs workout: [list exercises for legs]",
        "sunday": "Rest day: Time to relax and recover."
    }

    # Return the workout for the specified day
    return workouts.get(day, "No workout found for this day.")

def get_workout_for_day(day):
    workout = {
        "monday": "legs",
        "tuesday": "chest",
        "wednesday": "pull",
        "thursday": "rest",
        "friday": "arms",
        "saturday": "legs",
        "sunday": "rest",
    }

    # Check if the input is a valid day
    if day.lower() in workout:
        todays_workout = workout[day.lower()]
        message = f"Since it's {day.capitalize()}, I would do {todays_workout} today. Would you like to do that?"
    else:
        message = "That's not a valid day of the week. Please enter a valid day."

    return message

def get_updates(last_update_id):
    url = URL + "getUpdates?timeout=100"
    if last_update_id:
        url += "&offset={}".format(last_update_id)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    return max(int(update["update_id"]) for update in updates["result"])

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()