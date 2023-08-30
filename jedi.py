import requests

# Define the base URL for the SWAPI
base_url = "https://swapi.dev/api"

# Send a GET request to retrieve the list of films
films_response = requests.get(f"{base_url}/films/")
films_data = films_response.json()

# Search for the film with title "Return of the Jedi"
target_film = None
for film in films_data["results"]:
    if film["title"] == "Return of the Jedi":
        target_film = film
        break

if target_film:
    # Get the list of ship URLs that appeared in the target film
    ship_urls = target_film["starships"]

    # Fetch ship data from the retrieved URLs
    ships = []
    for ship_url in ship_urls:
        ship_response = requests.get(ship_url)
        ship_data = ship_response.json()
        ships.append(ship_data)

    # Print the list of ships
    for ship in ships:
        print("Ship Name:", ship["name"])
        print("******")
else:
    print("Film 'Return of the Jedi' not found in SWAPI.")
