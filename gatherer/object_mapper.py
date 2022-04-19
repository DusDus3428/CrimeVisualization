import crime_dto
import constants
from datetime import datetime


def transform_la_crime_data_into_crime_objects(data_json, api_name, api_url) -> list[crime_dto.Crime]:
    crimes = []

    for crime_json in data_json:
        source_details = crime_dto.SourceDetails(constants.LOS_ANGELES_API_PORTAL_NAME, api_name, api_url)

        crime_details = crime_dto.CrimeDetails(
            crime_json['crm_cd_desc'] if 'crm_cd_desc' in crime_json else '',
            crime_json['weapon_desc'] if 'weapon_desc' in crime_json else '',
            crime_json['status_desc'] if 'status_desc' in crime_json else '',
            crime_json['premis_desc'] if 'premis_desc' in crime_json else ''
        )

        victim_details = crime_dto.VictimDetails(
            int(crime_json['vict_age']) if 'vict_age' in crime_json else 0,
            crime_json['vict_sex'] if 'vict_sex' in crime_json else '',
            crime_json['vict_descent'] if 'vict_descent' in crime_json else ''
        )

        date_and_time_details = crime_dto.DateAndTimeDetails(
            datetime.strptime(crime_json['date_rptd'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d'),
            datetime.strptime(crime_json['date_occ'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d'),
            datetime.strptime(crime_json['time_occ'], '%H%M').time().strftime('%I:%M%p')
        )

        coordinates = crime_dto.Coordinates(
            float(crime_json['lat']) if 'lat' in crime_json else 0.0,
            float(crime_json['lon']) if 'lon' in crime_json else 0.0
        )

        location_details = crime_dto.LocationDetails(
            crime_json['location'] if 'location' in crime_json else 0.0,
            crime_json['area_name'] if 'area_name' in crime_json else 0.0,
            coordinates
        )

        crime = crime_dto.Crime(
            constants.LOS_ANGELES_NAME,
            source_details,
            crime_details,
            victim_details,
            date_and_time_details,
            location_details
        )

        crimes.append(crime)

    return crimes
