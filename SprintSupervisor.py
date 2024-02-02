import random
import math

class WeekPlanner:
    def __init__(self):
        self.schedule = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }

    def add_task(self, task=None, story_points=None):
        if task is None:
            task = input("Enter task: ")
        if story_points is None:
            while True:
                try:
                    story_points = int(input("Enter story points: "))
                    if story_points <= 0:
                        print("Story points must be a positive integer.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for story points.")

        if story_points <= 0:
            print("Invalid story points. Task not added.")
            return

        # Check if there are any available time slots
        available_slots = any(5 - sum(sp for _, sp in self.schedule[day]) > 0 for day in self.schedule.keys())
        if not available_slots:
            print("There is no availability time-slot for this task.")
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
        for day, tasks in self.schedule.items():
            print(f"{day}:")
            if tasks:
                for task, sp in tasks:
                    hours_needed = math.ceil(sp * 1.2)
                    if hours_needed == 6:
                        hours = ["10:00-12:00", "01:00-05:00"]
                    elif hours_needed >= 4:
                        hours = ["01:00-05:00"]
                    elif hours_needed >= 2:
                        hours = ["10:00-12:00"]
                    print(f"\t- {task} ({sp} story points) - Hours: {', '.join(hours)}")
            else:
                print("\tNo tasks")
            print()

    def shuffle_schedule(self):
        days = list(self.schedule.keys())
        for day, tasks in self.schedule.items():
            for task in tasks:
                new_day = random.choice(days)
                if new_day != day:
                    self.schedule[new_day].append(task)
                    self.schedule[day].remove(task)

if __name__ == "__main__":
    planner = WeekPlanner()
    while True:
        print("1) Add Task")
        print("2) Show Current Schedule")
        print("3) Shuffle The Calendar")
        print("4) Exit")
        choice = input("Select an option: ")

        if choice == "1":
            planner.add_task()
        elif choice == "2":
            planner.show_schedule()
        elif choice == "3":
            planner.shuffle_schedule()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
