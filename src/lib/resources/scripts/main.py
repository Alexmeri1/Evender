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

    "countryCode": userCountry,

    "startDateTime": userBeginDate,
    
    "endDateTime": userEndDate,

    #constant 100 first events

    "size": 100
}

# Make the API request
response = requests.get(url, params=params)
print("\n")

def getAvgPrice(eventId):
    urlForPrice = (f"https://app.ticketmaster.com/discovery/v2/events/{eventId}.json?apikey=dDWSsjMPLJbXiRcAzXzd1NzPiwJf1q4p")
    minimum = 0
    maximum = 0
    responseForAvg = requests.get(urlForPrice)
    if responseForAvg.status_code == 200:
        data = responseForAvg.json()
        if "priceRanges" in data and "min" in data["priceRanges"][0] and "max" in data["priceRanges"][0]:
            minimum = data["priceRanges"][0]["min"]
            maximum = data["priceRanges"][0]["max"]
            averagePrice = (maximum + minimum) / 2.0
            return averagePrice
        else:
            return 0
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return 0




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
            event_id = event["id"]
            price = getAvgPrice(event_id)

            print(f"Event: {name}, with ID {event_id}")     
            print(f"Date: {date}")
            print(f"Venue: {venue}")
            if(price > 0):
                print(f"The average price is around: {price:.2f}$")
            else:
                print("Sadly no price was found.")
            print("-" * 40)
    else:
        print("No events found.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(f"Response: {response.text}")


