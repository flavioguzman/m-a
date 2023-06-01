import json
import requests

def load_indications():
    """
    Reads the JSON data from 'data.json' and sends a POST request for each
    record to the 'indications' endpoint of the WordPress API.

    Returns:
    None
    """
    try:
        # Open the JSON file and load the data
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Specify the API endpoint
        api_endpoint = 'http://localhost/wordpress/index.php/wp-json/jet-cct/indications'

        # Your WordPress username and password
        username = 'flavio'
        password = 'djHS Nn3f F6XC TCys eSSC mVtA'

        # For each record in the data, send a POST request to the API
        for record in data:
            # Extract the data to be sent with the POST request
            payload = {
                'fda_indication': record['fda_use']
            }

            # Check if the entry already exists
            response = requests.get(api_endpoint, auth=(username, password))

            if response.status_code == 200:
                # Get the existing data from the response
                existing_data = response.json()
                # Check if the entry already exists in the data
                if any(entry['fda_indication'] == payload['fda_indication'] for entry in existing_data):
                    print(f"Entry with fda_indication '{payload['fda_indication']}' already exists. Skipping.")
                    continue

            # Send the POST request
            response = requests.post(api_endpoint, data=payload, auth=(username, password))

            # Check if the POST request was successful
            if response.status_code != 201:
                print(f"Error: Status code {response.status_code}, text: {response.text}")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    load_indications()
