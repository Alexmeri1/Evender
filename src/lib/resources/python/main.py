import requests
import information

# Replace with your Ticketmaster API key
API_KEY = "dDWSsjMPLJbXiRcAzXzd1NzPiwJf1q4p"

# API endpoint for event search
url = "https://app.ticketmaster.com/discovery/v2/events.json"

# Parameters for the API request

userCity = information.getUserCity()
userCountry = information.getUserCountry()
userBeginDate =  information.getUserBeginDate()
userEndDate = information.getUserEndDate()
userPartySize = information.getUserBeginDate()

params = {
    #My key
    "apikey": API_KEY,

    #Prefered city
    "city": userCity,

    #Canada
    "countryCode": userCountry,

    "startDateTime": userBeginDate,
    
    "endDateTime": userEndDate,

    #constant 100 first events

    "size": 100
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:

    data = response.json()

    # Check if there are events in the response
    if "_embedded" in data and "events" in data["_embedded"]:
        events = data["_embedded"]["events"]

        # Print event details
        for event in events:
            name = event.get("name", "No name available")
            date = event.get("dates", {}).get("start", {}).get("localDate", "No date available")
            venue = event.get("_embedded", {}).get("venues", [{}])[0].get("name", "No venue available")
            print(f"Event: {name}")
            print(f"Date: {date}")
            print(f"Venue: {venue}")
            print("-" * 40)
    else:
        print("No events found.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(f"Response: {response.text}")