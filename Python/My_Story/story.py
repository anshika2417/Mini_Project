import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def dataLoad():
    data = pd.read_csv("C:/Users/anshi/OneDrive/Desktop/PROJECTS/Mini_Project/Python/My_Story/MyStory.csv")
    return data

def dataInfo():
    data = dataLoad()
    print("Dataset Information:")
    data.info()
    rows = int(input("\nEnter the number of rows you want to see: "))
    choice = input("Do you want to see the first or last rows? (Enter 'first' or 'last'): ").strip().lower()
    if choice == "first":
        print(f"\nFirst {rows} Rows of the Dataset:")
        print(data.head(rows))
    elif choice == "last":
        print(f"\nLast {rows} Rows of the Dataset:")
        print(data.tail(rows))
    else:
        print("Invalid choice. Please enter 'first' or 'last'.\n")

def average():
    data = dataLoad()
    date = input("Enter the date (dd-mm-yyyy): ")
    filtered = data[data["Date"] == date]
    if len(filtered) > 0:
        apps = ["YouTube", "Spotify", "WhatsApp", "LPUTouch", "Chrome", "Phone", "Snapchat", "Instagram", "LinkedIn"]
        average = filtered[apps].mean(axis=1).values[0]
        print(f"Average Screen Time for {date} is {average:.2f} minutes")
        plt.figure(figsize=(10, 5))
        sns.barplot(x=apps, y=filtered[apps].mean(), palette='viridis')
        plt.title(f"Average Screen Time per App on {date}")
        plt.xlabel("Apps")
        plt.ylabel("Average Time (minutes)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No data for that date.\n")

def totalTime():
    
    data = dataLoad()
    apps = ["YouTube", "Spotify", "WhatsApp", "LPUTouch", "Chrome", "Phone", "Snapchat", "Instagram", "LinkedIn"]
    total_time_per_app = data[apps].sum()
    print(f"\nTotal Screen Time across all dates:")
    for app, time in total_time_per_app.items():
        print(f"\t{app}: {time} minutes")

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=total_time_per_app.index, y=total_time_per_app.values, marker='o')
    plt.title("Total Screen Time per App Across All Dates")
    plt.xlabel("Apps")
    plt.ylabel("Total Time (minutes)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def summary():
    data = dataLoad()
    date = input("Enter the date (dd-mm-yyyy): ")
    filtered = data[data["Date"] == date]
    if len(filtered) > 0:
        apps = ["YouTube", "Spotify", "WhatsApp", "LPUTouch", "Chrome", "Phone", "Snapchat", "Instagram", "LinkedIn"]
        summary = filtered[apps].iloc[0]
        print(f"Screen Time Summary for {date}:")
        print(summary)
    else:
        print("No data for that date.\n")


def overallUsage():
    data = dataLoad()
    apps = ["YouTube", "Spotify", "WhatsApp", "LPUTouch", "Chrome", "Phone", "Snapchat", "Instagram", "LinkedIn"]
    data['TotalScreenTime'] = data[apps].sum(axis=1)
    
    choice = int(input("Do you want to see the day with the highest or lowest overall screen time? (Press 1 = 'highest' or 2 = 'lowest'):"))
    
    
    if choice == 1:
        max_day = data['TotalScreenTime'].idxmax()
        max_date = data.loc[max_day, 'Date']
        max_time = data.loc[max_day, 'TotalScreenTime']
        print(f"The day with the highest overall screen time is {max_date} with {max_time:.2f} minutes.\n")
        
    elif choice == 2:
        min_day = data['TotalScreenTime'].idxmin()
        min_date = data.loc[min_day, 'Date']
        min_time = data.loc[min_day, 'TotalScreenTime']
        print(f"The day with the lowest overall screen time is {min_date} with {min_time:.2f} minutes.\n")
        
    else:
        print("Invalid choice. Please enter '1' or '2'.\n")

while True:
    print("\n<------------------------------------->")
    print("1. Show Data Information")
    print("2. Calculate Average Screen Time")
    print("3. Calculate Total Screen Time")
    print("4. Show Screen Time Summary")
    print("5. Show Day with Overall Screen Time")
    print("6. Exit\n")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        dataInfo()
    elif choice == "2":
        average()
    elif choice == "3":
        totalTime()
    elif choice == "4":
        summary()
    elif choice == "5":
        overallUsage()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Please choose a valid option (1-6).\n")