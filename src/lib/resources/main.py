import requests

# Replace 'YOUR_API_KEY' with your actual Eventbrite API key
API_KEY = 'YOUR_API_KEY'
URL = 'https://www.eventbriteapi.com/v3/events/search/'

data = {
    "code": "YOUR_ACCESS_CODE",
    "client_secret": "YOUR_CLIENT_SECRET",
    "client_id": "YOUR_API_KEY",
    "grant_type": "authorization_code",
}


# Set up the headers with your API key
headers = {
    'Authorization': f'Bearer {API_KEY}',
}

# Set up any parameters for the request
params = {
    'q': 'technology',  # Search for events related to technology
    'sort_by': 'date',  # Sort by date
    'location.address': 'San Francisco',  # Location
}

# Make the GET request to the Eventbrite API
response = requests.get(URL, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    events = data['events']
    
    # Print out the names and dates of the events
    for event in events:
        name = event['name']['text']
        start = event['start']['local']
        print(f"Event: {name}, Start: {start}")
else:
    print(f"Failed to fetch events: {response.status_code}")
    print(response.text)