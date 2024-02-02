import random
import math
import tkinter as tk
from tkinter import simpledialog

class WeekPlannerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Week Planner")
        
        self.schedule = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }

        self.create_widgets()

    def create_widgets(self):
        self.task_label = tk.Label(self.master, text="Task:")
        self.task_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.task_entry = tk.Entry(self.master)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.story_points_label = tk.Label(self.master, text="Story Points:")
        self.story_points_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.story_points_entry = tk.Entry(self.master)
        self.story_points_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=2, columnspan=2, padx=5, pady=5)
        
        self.show_schedule_button = tk.Button(self.master, text="Show Current Schedule", command=self.show_schedule)
        self.show_schedule_button.grid(row=3, columnspan=2, padx=5, pady=5)
        
        self.shuffle_schedule_button = tk.Button(self.master, text="Shuffle The Calendar", command=self.shuffle_schedule)
        self.shuffle_schedule_button.grid(row=4, columnspan=2, padx=5, pady=5)
        
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=5, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        story_points = int(self.story_points_entry.get())
        
        if story_points <= 0:
            tk.messagebox.showerror("Error", "Story points must be a positive integer.")
            return

        # Split task if it's greater than 5 story points
        while story_points > 0:
            day = random.choice(list(self.schedule.keys()))
            if day in self.schedule:
                max_points = 5 - sum(sp for _, sp in self.schedule[day])
                if max_points <= 0:
                    continue  # Skip if the day is already full
                if story_points >= max_points:
                    self.schedule[day].append((task, max_points))
                    story_points -= max_points
                else:
                    self.schedule[day].append((task, story_points))
                    story_points = 0

    def show_schedule(self):
        schedule_text = ""
        for day, tasks in self.schedule.items():
            schedule_text += f"{day}:\n"
            if tasks:
                for task, sp in tasks:
                    hours_needed = math.ceil(sp * 1.2)
                    if hours_needed == 6:
                        hours = ["10:00-12:00", "01:00-05:00"]
                    elif hours_needed >= 4:
                        hours = ["01:00-05:00"]
                    elif hours_needed >= 2:
                        hours = ["10:00-12:00"]
                    schedule_text += f"\t- {task} ({sp} story points) - Hours: {', '.join(hours)}\n"
            else:
                schedule_text += "\tNo tasks\n"
        
        tk.messagebox.showinfo("Current Schedule", schedule_text)

    def shuffle_schedule(self):
        days = list(self.schedule.keys())
        for day, tasks in self.schedule.items():
            for task in tasks:
                new_day = random.choice(days)
                if new_day != day:
                    self.schedule[new_day].append(task)
                    self.schedule[day].remove(task)


def main():
    root = tk.Tk()
    app = WeekPlannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
