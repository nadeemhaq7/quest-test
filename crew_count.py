import requests

# Define the base URL for the SWAPI
base_url = "https://swapi.dev/api"

# Send a GET request to retrieve the list of starships
starships_response = requests.get(f"{base_url}/starships/")
starships_data = starships_response.json()

# Filter and print starships with crews between 3 and 100 (excluding invalid values)
for starship in starships_data["results"]:
    crew = starship["crew"]
    
    # Handle "unknown" crew counts and exclude values with hyphens or commas
    if crew != "unknown" and "-" not in crew and "," not in crew:
        crew_count = int(crew)
        if 3 <= crew_count <= 100:
            print("Starship Name:", starship["name"])
            print("Crew:", crew_count)
            print("-----")
