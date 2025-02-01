import json

json_data = '''
{
    "userName": "Alex M",
    "location": {
        "city": "Montreal",
        "country": "CA"
    },
    "dates": {
        "beginning": "2025-02-01",
        "end": "2025-02-03"
    },
    "groupSize": 10
}
'''
data = json.loads(json_data)

def getUserCity():
    return data["location"]["city"]
   
def getUserCountry():
    return data["location"]["country"]

def getUserBeginDate():
    dateOfUser = data["dates"]["beginning"] + "T00:00:00Z"
    return str(dateOfUser)

def getUserEndDate():
    dateOfUser = data["dates"]["end"] + "T00:00:00Z"
    return str(dateOfUser)

def getGroupSize():
    return data["groupSize"]



""" 

{

userData: { 

    location: Array[null || String City, null || String Country (US OR CA)],
    groupSize: int,
    beginData: Array[Begin (YYYY-MM-DD), End (YYYY-MM-DD)],


    }

}

"""