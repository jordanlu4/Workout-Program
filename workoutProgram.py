def interface():

    print("+" + "-" * (15) + "+")
    print("| " + "Workout Today" + " |")
    print("+" + "-" * (15) + "+")

def print_workout_plan(first, second, last):
    print(f"Workout:\n1. {first}\n2. {second}\n3. {last}")

def chest():
    first = "Incline Bench Press (Smith Machine)"
    second = "Flat Bench Press (Dumbell)"
    last = "Pec Deck Flys (Pec Machine)"

    chest_exercises = {
        "Incline Bench Press (Smith Machine)": ["Incline Bench Press (Dumbell)", "Incline Bench Press (Barbell)"],
        "Neutral Pec Deck Flys (Machine)": ["Neutral Pec Flys (Cable)", "Neutral Pec Flys (Dumbell)"],
        "Flat Bench Press (Dumbell)": ["Flat Bench Press (Barbell)", "Flat Bench Press (Machine)"]
    }

    while True:
        print(f"Workout:\n1. {first}\n2. {second}\n3. {last}")
        user_in = input("\nStart: Start Workout\nSwap: Swap an exercise\nPlease choose 'Start' or 'Swap': ").lower()

        if user_in == "swap":
            swap_choice = input("Which exercise would you like to swap? (1, 2, or 3): ")
            if swap_choice in ["1", "2", "3"]:
                chosen_exercise = first if swap_choice == "1" else second if swap_choice == "2" else last

                print(f"Alternatives for {chosen_exercise}:")
                for i, alternative in enumerate(chest_exercises[chosen_exercise], 1):
                    print(f"{i}. {alternative}")

                alternative_choice = input("Please choose an alternative: ")
                try:
                    alternative_choice = int(alternative_choice) - 1
                    new_exercise = chest_exercises[chosen_exercise][alternative_choice]

                    if swap_choice == "1":
                        first = new_exercise
                    elif swap_choice == "2":
                        second = new_exercise
                    elif swap_choice == "3":
                        last = new_exercise
                except (ValueError, IndexError):
                    print("Invalid choice.")
                    continue  # Stay in the loop for another swap or start

            else:
                print("Invalid choice.")
                continue  # Stay in the loop for another swap or start

        elif user_in == "start":
            print(f"{first}\nSet 1: 8 Repetitions at 60% Intensity\nSet 2: 8-12 Repetitions at 80% Intensity\nSet 3: To Failure, but Minimum 6 Repetitions\nSet 4: To Failure, but Minimum 8 Repetitions")
            print(f"{second}\nSet 1: To Failure, but Minimum 8 Repetitions\nSet 2: To Failure, but Minimum 8 Repetitions")
            print(f"{last}\nSet 1: To Failure, but Minimum 8 Repetitions\nSet 2: To Failure, but Minimum 8 Repetitions")
            
            break  # Exit the loop to start the workout

        else:
            print("Invalid input. Please choose 'Start' or 'Swap'.")




def arms():
    bicep1 = "Bicep Curl (Dumbell)"
    tricep1 = "Tricep Pushdown (Rope)"
    shoulder = "Shoulder Flys (Cable)"
    bicep2 = "Hammer Curl (Dumbell)"
    tricep2 = "Overhead Tricep Extension (Cable)"

    arm_exercises = {
        "Bicep Curl (Dumbell)": ["Bicep Curl (Barbell)", "Bicep Curl (Cable)"],
        "Tricep Pushdown (Rope)": ["Tricep Pushdown (Cable)"],
        "Shoulder Flys (Cable)": ["Shoulder Flys (Dumbell)"],
        "Overhead Tricep Extension (Cable)": ["Overhead Tricep Extension (Bar Extension)", "Overhead Tricep Extension (Rope)"],
        "Hammer Curl (Dumbell)": ["Hammer Curl (Cable)"]
    }

    while True:
        print(f"Workout:\n1. {bicep1}\n2. {tricep1}\n3. {shoulder}\n4. {bicep2}\n5. {tricep2}")
        user_in = input("\nStart: Start Workout\nSwap: Swap an exercise\nPlease choose 'Start' or 'Swap': ").lower()

        if user_in == "swap":
            swap_choice = input("Which exercise would you like to swap? (1, 2, 3, 4, or 5): ")
            if swap_choice in ["1", "2", "3", "4", "5"]:
                chosen_exercise = {
                    "1": bicep1,
                    "2": tricep1,
                    "3": shoulder,
                    "4": bicep2,
                    "5": tricep2
                }[swap_choice]

                print(f"Alternatives for {chosen_exercise}:")
                for i, alternative in enumerate(arm_exercises[chosen_exercise], 1):
                    print(f"{i}. {alternative}")

                alternative_choice = input("Please choose an alternative: ")
                try:
                    alternative_choice = int(alternative_choice) - 1
                    new_exercise = arm_exercises[chosen_exercise][alternative_choice]

                    if swap_choice == "1":
                        bicep1 = new_exercise
                    elif swap_choice == "2":
                        tricep1 = new_exercise
                    elif swap_choice == "3":
                        shoulder = new_exercise
                    elif swap_choice == "4":
                        bicep2 = new_exercise
                    elif swap_choice == "5":
                        tricep2 = new_exercise
                except (ValueError, IndexError):
                    print("Invalid choice.")
                    continue  # Stay in the loop for another swap or start

            else:
                print("Invalid choice.")
                continue  # Stay in the loop for another swap or start

        elif user_in == "start":
            # Here you can add the specific sets and repetitions for each exercise
            print(f"{bicep1}\nSet 1: ")
            print(f"{tricep1}\nSet 1")
            print(f"{shoulder}\nSet 1")
            print(f"{bicep2}\nSet 1")
            print(f"{tricep2}\nSet 1")

            break  # Exit the loop to start the workout

        else:
            print("Invalid input. Please choose 'Start' or 'Swap'.")

arms()
# def legs():
# def rest():
# def pull():    

def build():
    workout = {
    "monday": "legs",
    "tuesday": "chest",
    "wednesday": "pull",
    "thursday": "rest",
    "friday": "arms",
    "saturday": "legs",
    "sunday": "rest",
    }           
    while True:
        day = input("What day of the week is it?\n").lower()

        # Check if the input is a valid day
        if day in workout:
            todays_workout = workout[day]  # Use a different variable name here
            print(f"Since it's {day.capitalize()}, I would usually do {todays_workout}.")

            alternative = input(f"Would you like to hit {todays_workout} today?\n").lower()
            while alternative not in ["no", "yes"]:
                alternative = input("Is that a yes or no?\n").lower()
            
            new_workout = todays_workout  # Initialize new_workout with todays_workout

            if alternative == "no":
                new_workout = input("What would you like to hit then?\nLegs\nChest\nArms\nPull\nRest\nChoose one of the following: ").lower()
                while new_workout not in ["legs", "chest", "arms", "pull", "rest"]:
                    new_workout = input("Please choose from Legs, Chest, Arms, Pull, Rest:\n").lower()

                if new_workout == "legs":
                    # print("legs")
                    legs()  
                elif new_workout == "chest":
                    chest()
                    # print("chest")  
                elif new_workout == "pull":
                    pull()     
                    # print("pull")         
                elif new_workout == "arms":
                    arms() 
                    # print("arms")     
                elif new_workout == "rest":
                    rest() 
                    # print("rest")    
            
            if alternative == "yes":
                print(f"Alright, then we'll hit {todays_workout} today.\n") 
                todays_workout()  # Call the appropriate workout function
            else:
                print(f"Alright, then we'll hit {new_workout} today.\n")
                new_workout()  # Call the appropriate workout function

            break  # Exit the loop only if a valid day was entered
        else:
            print("That's not a valid day of the week. Please enter a valid day.")

build()