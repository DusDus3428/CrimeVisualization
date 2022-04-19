# Python Crime Data Gatherer 
This program gathers crime data from open data portals for a select number of cities in the USA.

## A Unified Object Structure
Since the data is gathered from multiple sources it is important to define a uniform object structure for storing purposes.
So, once the data is fetched all entries will be mapped to this object structure:
```
{
    "city": "string",
    "source_details": {
        "portal_name": "string",
        "api_name": "string",
        "url": "string"
    },
    "crime_details": {
        "crime_type": "string",
        "weapon_used": "string",
        "status": "string",
        "crime_scene": "string"
    },
    "victim_details": {
        "age": 0,
        "sex": "string",
        "descent": "string"
    },
    "date_and_time_details": {
        "report_date": 'YYYY-MM-DD',
        "incident_date": 'YYYY-MM-DD',
        "incident_time": '00:00.000'
    },
    "location_details" : {
        "address": "string",
        "area": "string",
        "coordinates": {
            "latitude": 0.0000,
            "longitude": 0.0000
        }
    }
}
```