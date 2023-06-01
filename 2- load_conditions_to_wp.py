import json
import requests
from requests.auth import HTTPBasicAuth

def load_conditions():
    """
    Reads the JSON data from 'data.json' and sends a POST request for each
    record to the 'conditions' endpoint of the WordPress API.

    Returns:
    None
    """
    try:
        # Open the JSON file and load the data
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Specify the API endpoint
        api_endpoint = 'http://localhost/wordpress/index.php/wp-json/jet-cct/conditions'
        
        # Specify the application password for the WP API
        username = 'flavio'
        password = 'djHS Nn3f F6XC TCys eSSC mVtA'
        auth = HTTPBasicAuth(username, password)
        
        # For each record in the data, send a POST request to the API
        for record in data:
            # Extract the data to be sent with the POST request
            payload = {
                'cct_status': 'publish',
                'condition_name': record['name'],
                'cct_author_id': '1'
            }

            # Send the POST request
            response = requests.post(api_endpoint, data=payload, auth=(username, password))

            # Check if the POST request was successful
            if response.status_code != 201:
                print(f"Error: Status code {response.status_code}, text: {response.text}")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    load_conditions()
