from dataclasses import dataclass


@dataclass
class SourceDetails:
    api_name: str
    api_page_url: str
    api_url: str


@dataclass
class CrimeDetails:
    crime_type: str
    weapon_used: str
    status: str
    crime_scene: str


@dataclass
class VictimDetails:
    age: int
    sex: str
    decent: str


@dataclass
class DateAndTimeDetails:
    report_date: str
    incident_date: str
    incident_time: str


@dataclass
class Coordinates:
    latitude: float
    longitude: float


@dataclass
class LocationDetails:
    address: str
    area: str
    coordinates: Coordinates


@dataclass
class Crime:
    city: str
    portal_name: str
    portal_url: str
    source_details: SourceDetails
    crime_details: CrimeDetails
    victim_details: VictimDetails
    date_and_time_details: DateAndTimeDetails
    location_details: LocationDetails
