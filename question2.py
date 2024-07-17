# Task 1
import random

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times = ["morning", "afternoon", "evening"]
moods = ["Happy", "Sad", "Energetic", "Calm", "Angry", "Bored", "Depressed", "Irritated", "Jubilant"]

for day in range(len(week)):
    for time in range(len(times)):
        mood = random.choice(moods)
        print("On {} {} you were {}.".format(week[day], times[time], mood))

