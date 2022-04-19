import requests
import constants
import object_mapper
import json


def main():
    data = requests.get(constants.LOS_ANGELESE_CRIMES_2020_TO_PRESENT_URL).text
    crimes = object_mapper.transform_la_crime_data_into_crime_objects(json.loads(data),
                                                                      constants.LOS_ANGELESE_CRIMES_2020_TO_PRESENT_NAME,
                                                                      constants.LOS_ANGELESE_CRIMES_2020_TO_PRESENT_URL)
    print(crimes[0])


if __name__ == '__main__':
    main()
