# Task 1
import random
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["Happy", "Sad", "Energetic", "Calm", "Angry", "Bored"]
for day in range(7):
    mood_today = random.choice(moods)
    print(week[day] + "'s mood is " + mood_today)

