import json
import requests

# Read user preferences from file
def load_user_data(filename="user_info.json"):
    with open(filename, "r") as file:
        return json.load(file)

user_data = load_user_data()

# Extract user data
def getUserCity(data):
    return data["location"]["city"]

def getUserCountry(data):
    return data["location"]["country"]

def getUserBeginDate(data):
    return data["dates"]["beginning"] + "T00:00:00Z"

def getUserEndDate(data):
    return data["dates"]["end"] + "T00:00:00Z"

# API Key and Endpoint
API_KEY = "dDWSsjMPLJbXiRcAzXzd1NzPiwJf1q4p"
url = "https://app.ticketmaster.com/discovery/v2/events.json"

# Extracted User Information
userCity = getUserCity(user_data)
userCountry = getUserCountry(user_data)
userBeginDate = getUserBeginDate(user_data)
userEndDate = getUserEndDate(user_data)

# API Query Parameters
params = {
    "apikey": API_KEY,
    "city": userCity,
    "countryCode": userCountry,
    "startDateTime": userBeginDate,
    "endDateTime": userEndDate,
    "size": 100
}

# Make API Request
response = requests.get(url, params=params)
events_list = []

if response.status_code == 200:
    data = response.json()

    if "_embedded" in data and "events" in data["_embedded"]:
        events = data["_embedded"]["events"]

        for event in events:
            name = event.get("name", "No name available")
            date = event.get("dates", {}).get("start", {}).get("localDate", "No date available")
            venue = event.get("_embedded", {}).get("venues", [{}])[0].get("name", "No venue available")
            event_id = event.get("id", "No id available")
            event_url = event.get("url", "No URL available")
            event_info = event.get("info", "No information available")

            # Handle missing price
            price_range = event.get("priceRanges", [{}])[0]
            price = (price_range.get("min", 0) + price_range.get("max", 0)) / 2 if "min" in price_range and "max" in price_range else 0

            # Create a new dictionary for each event
            event_data = {
                "event_name": name,
                "date": date,
                "venue": venue,
                "price": price,
                "url": event_url,
                "info": event_info,
                "city": userCity,
                "country": userCountry  
            }

            events_list.append(event_data)

            # Print event details
            print(f"Event: {name}, ID: {event_id}")
            print(f"Date: {date}")
            print(f"Venue: {venue}")
            print(f"Avg Price: {price:.2f}$" if price > 0 else "No price found.")
            print(f"URL: {event_url}")
            print(f"Info: {event_info}")
            print("-" * 40)

    else:
        print("No events found.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(f"Response: {response.text}")
