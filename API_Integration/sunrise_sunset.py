import requests
import bcrypt
import re
from datetime import datetime
import pytz

def register():
    print("User Registration")
    name = input("Enter your name: ")

    while True:
        email = input("Enter your email address: ")
        if re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            break  
        else:
            print("Invalid email format. Please enter a valid email (e.g., user@example.com).")
            return
    
    password = input("Enter your password: ").encode('utf-8')
    if len(password)>7:
        if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-+_!@#$%^&*.,?]).+$', password.decode('utf-8')):

            salt=bcrypt.gensalt(rounds=12)
            hash_pass=bcrypt.hashpw(password,salt)
        else:
            print("Password is invalid (must contain number, upper, lower and special characters!! )")
            return
    else:
        print("Password should be 8 char long!! ")
        return
    
    security_answer = input("What is your friend's name? : ").strip()
    with open("login.csv", 'a') as file:
        file.write(f"{name},{email},{hash_pass.decode('utf-8')},{security_answer}\n")
    
    print("Registration Done")

def get_coordinates(city_name):
    api_key = 'ad2b88cfd26c71c33a66c3691393635f'  
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"

    try:
        response = requests.get(geocode_url)

        if response.status_code == 200:
            location_data = response.json()
            if location_data and isinstance(location_data, list) and len(location_data) > 0:
                latitude = location_data[0]['lat']
                longitude = location_data[0]['lon']
                return latitude, longitude
            else:
                print("Invalid location. No data found for the specified city./n")
                return None, None
        else:
            print(f"Error {response.status_code}: Failed to retrieve location data.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}. Please check your internet connection and try again./n")
        return None, None

def convert_utc_to_local(utc_time):
    utc_time = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%S+00:00')
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone()
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

def get_sunrise_sunset_data(latitude, longitude):
    api_url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()['results']
            
            local_sunrise = convert_utc_to_local(data['sunrise'])
            local_sunset = convert_utc_to_local(data['sunset'])
            local_noon = convert_utc_to_local(data['solar_noon'])
            
            print(f"Sunrise Time (local): {local_sunrise}")
            print(f"Sunset Time (local): {local_sunset}")
            print(f"Day Length: {data['day_length']} seconds")
            print(f"Solar Noon (local): {local_noon}")
        else:
            print(f"Error {response.status_code}: Failed to retrieve data.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}. Please check your internet connection and try again./n")

def login():
    print("User Login")
    n = 5
    while n > 0:
        print(f"You have {n} attempts remaining")
        email = input("Enter your email address: ")
        password = input("Enter your password: ").encode('utf-8')
        with open("login.csv", 'r') as file:
            for line in file:
                details = line.strip().split(",")
                stored_email = details[1]
                stored_password = details[2].encode('utf-8')

                if email == stored_email:
                    if bcrypt.checkpw(password, stored_password):
                        print(f"Welcome {details[0]}! You have successfully logged in.")

                        city_name = input("Enter the city name for sunrise/sunset data: ")
                        latitude, longitude = get_coordinates(city_name)
                        if latitude is not None and longitude is not None:
                            get_sunrise_sunset_data(latitude, longitude)  # Call the new function here
                            return

                    else:
                        print("User Credentials are not correct!!!")
        n -= 1

    print("You exceeded your attempts!! Restart this for login")

def forget():
    email = input("Enter your email address: ")

    update_password = []
    updated = False

    with open("login.csv", 'r') as file:
        for line in file:
            details = line.strip().split(",")
            stored_email = details[1]
            stored_answer = details[3]
        
            if email == stored_email:
                updated = True
                
                security_answer = input("Enter the answer to the security question: ")
                if security_answer.strip().lower() == stored_answer.strip().lower():
                    print("Answer is correct. You can now reset your password.")

                    while True:
                        password = input("Enter new password: ").encode('utf-8')
                        if len(password) >= 8:
                            newPass = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
                            details[2] = newPass
                            updated = True
                            break
                        else:
                            print("Password should be at least 8 characters long!")
                else:
                    print("Security answer is incorrect.")
                    return
            update_password.append(",".join(details))
    
    with open("login.csv", 'w') as file:
        for line in update_password:
            file.write(line + "\n")
    
    if updated:
        print("Password updated Successfully!")
    else:
        print("Email not matched!! ")

while True:
    print("1. Registration\n2. Login\n3. Forget Password\n4. Exit")
    n = int(input("Enter your choice: "))

    if n == 1:
        register()
    elif n == 2:
        login()
    elif n == 3:
        forget()
    elif n == 4:
        exit()
    else:
        print("Enter choice between (1-4)")