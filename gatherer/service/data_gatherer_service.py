import requests
import json
from util import object_mapper
from model import api_details, crime_data


def gather_crime_data_from_portal(api: api_details.ApiDetails) -> list[crime_data.CrimeData]:
    retrieved_crime_data = requests.get(api.url).text
    return object_mapper.transform_la_crime_data_into_crime_objects(json.loads(retrieved_crime_data), api.name, api.url)
