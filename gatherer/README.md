# Python Crime Data Gatherer 
This program gathers crime data from open data portals for a select number of cities in the USA.

## A Unified Object Structure
Since the data is gathered from multiple sources it is important to define a uniform object structure for storing purposes.
So, once the data is fetched all entries will be mapped to this object structure:
```
{
    "city": "string",
    "sourceDetails": {
        "name": "string",
        "url": "string"
    },
    "crimeDetails": {
        "crimeType": "string",
        "weaponsUsed": "string",
        "status": "string",
        "crimeScene": "string"
    },
    "victimDetails": {
        "age": 0,
        "sex": "string",
        "descent": "string"
    },
    "dateAndTimeDetails": {
        "reportDate": 'YYYY-MM-DDT:00:00.000',
        "incidentDate": 'YYYY-MM-DDT00:00.000',
        "incidentTime": '00:00.000'
    },
    "locationDetails" : {
        "address": "string",
        "area": "string",
        "coordinates": {
            "latitude": 0.0000,
            "longetude": 0.0000
        }
    }
}
```