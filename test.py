import tkinter as tk
from tkinter import ttk, messagebox

class WorkoutApp:
    def __init__(self, root):
        self.root = root
        root.title("Workout Program")

        # Workout schedule
        self.workout_schedule = {
            "monday": "legs",
            "tuesday": "chest",
            "wednesday": "pull",
            "thursday": "rest",
            "friday": "arms",
            "saturday": "legs",
            "sunday": "rest",
        }

        # Workout options
        self.workouts = {
            "legs": self.legs,
            "chest": self.chest,
            "arms": self.arms,
            "pull": self.pull,
            "rest": self.rest,
        }

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Dropdown for selecting the day
        self.day_var = tk.StringVar()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_dropdown = ttk.Combobox(self.root, textvariable=self.day_var, values=days)
        day_dropdown.grid(column=0, row=0)

        # Start Workout Button
        start_button = tk.Button(self.root, text="Start Workout", command=self.start_workout)
        start_button.grid(column=1, row=0)

        # Workout Details Text
        self.workout_details = tk.Text(self.root, height=15, width=50)
        self.workout_details.grid(column=0, row=1, columnspan=2)

    def start_workout(self):
        day = self.day_var.get().lower()
        if day in self.workout_schedule:
            workout_routine = self.workout_schedule[day]
            self.workouts[workout_routine]()
        else:
            messagebox.showinfo("Error", "Please select a valid day.")

    def legs(self):
        # Example exercise data
        self.workout_details.delete(1.0, tk.END)
        self.workout_details.insert(tk.END, "Legs Workout:\n1. Squat (Hack)\n2. Hamstring Extensions (Machine)\n3. Quad Extensions (Machine)\n4. Hip Adductors (Machine)\n")

    def chest(self):
        self.workout_details.delete(1.0, tk.END)
        self.workout_details.insert(tk.END, "Chest Workout:\n1. Incline Bench Press (Smith Machine)\n2. Flat Bench Press (Dumbbell)\n3. Pec Deck Flys (Pec Machine)\n")

    def arms(self):
        self.workout_details.delete(1.0, tk.END)
        self.workout_details.insert(tk.END, "Arms Workout:\n1. Bicep Curl (Dumbbell)\n2. Tricep Pushdown (Rope)\n3. Shoulder Flys (Cable)\n")

    def pull(self):
        self.workout_details.delete(1.0, tk.END)
        self.workout_details.insert(tk.END, "Pull Workout:\n1. Neutral Grip Lateral Pull-Downs\n2. Preacher Curls (Machine)\n3. Shoulder Flys (Cable)\n")

    def rest(self):
        self.workout_details.delete(1.0, tk.END)
        self.workout_details.insert(tk.END, "Rest Day: Take it easy, maybe some light cardio or stretching.\n")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutApp(root)
    root.mainloop()
