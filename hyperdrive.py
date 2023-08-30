import requests

# Define the base URL for the SWAPI
base_url = "https://swapi.dev/api"

# Send a GET request to retrieve the list of ships
ships_response = requests.get(f"{base_url}/starships/")
ships_data = ships_response.json()

# Filter and print ships with a hyperdrive rating >= 1.0
for ship in ships_data["results"]:
    hyperdrive_rating = float(ship["hyperdrive_rating"]) if ship["hyperdrive_rating"] != "unknown" else 0.0
    if hyperdrive_rating >= 1.0:
        print("Ship Name:", ship["name"])
        print("Hyperdrive Rating:", hyperdrive_rating)
        print("******")