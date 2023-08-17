#!/usr/bin/node

import requests
import sys

def get_movie_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    data = response.json()

    if "characters" in data:
        characters = data["characters"]
        for character_url in characters:
            character_response = requests.get(character_url)
            character_data = character_response.json()
            print(character_data["name"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    get_movie_characters(movie_id)
