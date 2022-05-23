import constants
from service import data_gatherer_service
from model import api_details
from flask import Flask


app = Flask(__name__)

def main():
    la_portal_details = api_details.ApiDetails(
        constants.LOS_ANGELESE_CRIMES_2020_TO_PRESENT_URL,
        constants.LOS_ANGELESE_CRIMES_2020_TO_PRESENT_NAME,
        '',
        ''
    )
    crimes = data_gatherer_service.gather_crime_data_from_portal(la_portal_details)


if __name__ == '__main__':
    main()
