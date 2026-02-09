import csv
from datetime import date
import os
import matplotlib.pyplot as plt

FILE_NAME = "mood_data.csv"


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Mood"])


def add_mood():
    today = date.today()
    mood = input("Enter your today's mood (Happy/Sad/Productive/Lazy/Stressed): ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, mood])

    print("Mood saved successfully!\n")

def show_history():
    with open(FILE_NAME,"r") as file:   
        reader = csv.reader(file)
        next(reader)

        print("Mood history saved successfully!!\n")

        for row in reader:
            print(row[0],"-",row[1])
        
        print()

def mood_analysis():
    mood_count = {}

    with open(FILE_NAME,"r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            mood = row[1]
        
            if mood in mood_count :
                mood_count[mood] += 1
            else:
                mood_count[mood] = 1
    print(" Mood Analysis report!! ")
    
    for mood, count in mood_count.items():
        print(mood, ":", count)

    print()

def mood_graph():
    mood_count = {}

    with open(FILE_NAME,"r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            mood = row[1]
            if mood in mood_count:
                mood_count[mood] += 1
            else:
                mood_count[mood] = 1

    moods = list(mood_count.keys())
    counts = list(mood_count.values())

    plt.bar(moods, counts)
    plt.title("Mood Tracker Graph")
    plt.xlabel("Mood")
    plt.ylabel("Days")
    plt.show()

def generate_report():
    mood_count = {}

    with open(FILE_NAME,"r") as file:
        reader = csv.reader(file)
        next(reader)

        total_days = 0

        for row in reader:
            mood = row[1]
            total_days += 1

            if mood in mood_count:
                mood_count[mood] += 1
            else:
                mood_count[mood] = 1

    if total_days == 0:
        print(" No Data available at that moment!!\n")
        return
    
    max_count = max(mood_count.values())
    min_count = min(mood_count.values())

    most_common = {mood for mood, count in mood_count.items() if count == max_count}
    least_common = {mood for mood, count in mood_count.items() if count == min_count}
    
    print("\n📝 MOOD REPORT\n")
    print("Total days tracked:", total_days)
    print("Most common mood:", most_common)
    print("Least common mood:", least_common)
    print()
    

def menu():
    while True:
        print(" Enter your choice ")
        print(" Choose 1 for add mood")
        print(" Choose 2 for History ")
        print(" Choose 3 for Mood Analysis ")
        print(" choose 4 for Mood Graph ")
        print(" choose 5 for Overall Report ")
        print(" choose 6 for Exit!! ")

        choice = input("Enter your choice : ")
    
        if choice == "1":
            add_mood()
        elif choice == "2":
            show_history()
        elif choice == "3":
            mood_analysis()
        elif choice == "4":
            mood_graph()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print(" GoodBye!! ")
        else:
            print(" Please choose correct choice 1, or  only!! ")
    
menu()


