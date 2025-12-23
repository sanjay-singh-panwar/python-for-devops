import requests
import json

def api_data_fetcher():
    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract meaningful information
        joke_data = {
            "setup": data["setup"],
            "punchline": data["punchline"]
        }

        # Save to JSON file
        with open("output.json", "a") as file:
            json.dump(joke_data, file, indent=4)

        print("Joke saved successfully to output.json")
        print("Setup:", joke_data["setup"])
        print("Punchline:", joke_data["punchline"])

    else:
        print("Failed to fetch joke. Status code:", response.status_code)

api_data_fetcher()