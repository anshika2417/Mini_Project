olympic_records = []
def addDetails():
    print("Please enter data countrywise for the past five olympics")
    data=1
    while data<=5:
        print("Olympic",data)
        country=input("Country: ")
        year=int(input("Year: "))
        record=int(input("No. of medal records to enter: "))
        data+=1
        r=1
        while(r<=record):
            print("Medal record",r)
            name=input("Athlete Name: ")
            event=input("Event: ")
            medal=input("Medal (Gold/Silver/Bronze): ")

            value = {
                'country' : country,
                'year' : year,
                'records' : record,
                'name' : name,
                'event' : event,
                'medal' : medal
            }
            olympic_records.append(value)
            print("Record added successfully.\n")
            r+=1

def showDetails():
    if not olympic_records:
        print("No records available.\n")
    else:
        for value in olympic_records:
            print(f"Country: {value['country']}, Year: {value['year']}, Athlete: {value['name']}, "
                  f"Event: {value['event']}, Medal: {value['medal']}")


def medalCount():
    country_medals = {}

    for value in olympic_records:
        if value['medal'] != 'None':
            country_medals[value['country']] = country_medals.get(value['country'], 0) + 1

    for country, count in country_medals.items():
        print(f"{country}: {count} medals")


def performance():
    athlete_name = input("Enter athlete's name to search: ")
    athlete_records = [value for value in olympic_records if value['name'] == athlete_name]

    if athlete_records:
        for value in athlete_records:
            print(f"Event: {value['event']}, Year: {value['year']}, Medal: {value['medal']}")
    else:
        print("No records found for this athlete.\n")

def eventDetails():
    event_name = input("Enter event name to view details: ")
    event_records = [value for value in olympic_records if value['event'] == event_name]

    if event_records:
        for value in event_records:
            print(f"Athlete: {value['name']}, Year: {value['year']}, Country: {value['country']}, Medal: {value['medal']}")
    else:
        print("No records found for this event.\n")

def statistics():
    total_events = len(olympic_records)
    total_medals = len([record for record in olympic_records if record['medal'] != 'None'])
    
    gold_medals = len([record for record in olympic_records if record['medal'] == 'Gold'])
    silver_medals = len([record for record in olympic_records if record['medal'] == 'Silver'])
    bronze_medals = len([record for record in olympic_records if record['medal'] == 'Bronze'])

    print(f"Total Events: {total_events}")
    print(f"Total Medals: {total_medals}")
    print(f"Gold Medals: {gold_medals}")
    print(f"Silver Medals: {silver_medals}")
    print(f"Bronze Medals: {bronze_medals}\n")

while True:
    print("\n\t\t\t--Olympics Data Explorer--\n")
    print("1. Add Details")
    print("2. View Details")
    print("3. View medal count by country")
    print("4. Search Athele Performance")
    print("5. View Event Details")
    print("6. View Statistics")
    print("7. Exit")

    n=int(input("Select your choice: "))
    if n==1:
        addDetails()
    elif n==2:
        showDetails()
    elif n==3:
        medalCount()
    elif n==4:
        performance()
    elif n==5:
        eventDetails()
    elif n==6:
        statistics()
    elif n==7:
        break


