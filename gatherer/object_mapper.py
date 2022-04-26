import crime_dto
import constants
from datetime import datetime


# This method resolves the victims sex in order to increase the readability in the UI
# The mapping values are taken from https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8
def resolve_la_crime_victim_sex(victim_sex) -> str:
    resolved_victim_sex = ''

    match victim_sex:
        case 'F':
            resolved_victim_sex = 'Female'
        case 'M':
            resolved_victim_sex = 'Male'
        case 'X':
            resolved_victim_sex = 'Unknown'

    return resolved_victim_sex


# This method resolves the victims decent in order to increase the readability in the UI
# The mapping values are taken from https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8
def resolve_la_crime_victim_decent(victim_decent) -> str:
    resolved_victim_decent = ''

    match victim_decent:
        case 'A':
            resolved_victim_decent = 'Asian'
        case 'B':
            resolved_victim_decent = 'Black'
        case 'C':
            resolved_victim_decent = 'Chinese'
        case 'D':
            resolved_victim_decent = 'Cambodian'
        case 'F':
            resolved_victim_decent = 'Filipino'
        case 'G':
            resolved_victim_decent = 'Guamanian'
        case 'H':
            resolved_victim_decent = 'Hispanic/Latin/Mexican'
        case 'I':
            resolved_victim_decent = 'Native American/Native Alaskan'
        case 'J':
            resolved_victim_decent = 'Japanese'
        case 'K':
            resolved_victim_decent = 'Korean'
        case 'L':
            resolved_victim_decent = 'Laotian'
        case 'P':
            resolved_victim_decent = 'Pacific Islander'
        case 'S':
            resolved_victim_decent = 'Samoan'
        case 'U':
            resolved_victim_decent = 'Hawaiian'
        case 'V':
            resolved_victim_decent = 'Vietnamese'
        case 'Z':
            resolved_victim_decent = 'Indian'
        case 'W':
            resolved_victim_decent = 'White'
        case 'O':
            resolved_victim_decent = 'Other'
        case 'X':
            resolved_victim_decent = 'Unknown'

    return resolved_victim_decent


# This method maps the data objects we receive from the Los Angeles Open Data to the uniform data object
# that will be used in the frontend
def transform_la_crime_data_into_crime_objects(data_json, api_name, api_url) -> list[crime_dto.Crime]:
    crimes = []

    for crime_json in data_json:
        source_details = crime_dto.SourceDetails(api_name, constants.LOS_ANGELESE_CRIMES_2020_TO_PRESENT_URL, api_url)

        crime_details = crime_dto.CrimeDetails(
            crime_json['crm_cd_desc'] if 'crm_cd_desc' in crime_json else '',
            crime_json['weapon_desc'] if 'weapon_desc' in crime_json else '',
            crime_json['status_desc'] if 'status_desc' in crime_json else '',
            crime_json['premis_desc'] if 'premis_desc' in crime_json else ''
        )

        victim_details = crime_dto.VictimDetails(
            int(crime_json['vict_age']) if 'vict_age' in crime_json else 0,
            resolve_la_crime_victim_sex(crime_json['vict_sex']) if 'vict_sex' in crime_json else '',
            resolve_la_crime_victim_decent(crime_json['vict_descent']) if 'vict_descent' in crime_json else ''
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
            crime_json['location'] if 'location' in crime_json else '',
            crime_json['area_name'] if 'area_name' in crime_json else '',
            coordinates
        )

        crime = crime_dto.Crime(
            constants.LOS_ANGELES_NAME,
            constants.LOS_ANGELES_PORTAL_NAME,
            constants.LOS_ANGELES_PORTAL_URL,
            source_details,
            crime_details,
            victim_details,
            date_and_time_details,
            location_details
        )

        crimes.append(crime)

    return crimes
