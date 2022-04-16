import requests
import constants

def main():
    response = requests.get(constants.LOS_ANGELESE_CRIMES_2020_TO_PRESENT_URL)
    response_json = response.json()

if __name__ == '__main__':
    main()