import requests
import json
import urllib
import time

def get_ratings(name):
    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{name}"
    result = requests.get(url, headers={
        'x-rapidapi-host': 'imdb-internet-movie-database-unofficial.p.rapidapi.com',
        'x-rapidapi-key': '22e110fec9msh31ddf964854d045p183004jsnc60cd67c9606'
    })

    result = json.loads(result.content)
    if isinstance(result, list):
        return -1
    return result['rating']


if __name__ == "__main__":
    with open('names', 'r') as file:
        names = file.readlines()

    with open('output', 'a') as outfile:
        for name in names:
            name = name.strip("\n")
            time.sleep(2)
            rating = get_ratings(name)
            if rating == -1:
                outfile.write(f"multiplefirst '{name}': {rating}\n")
            elif rating:
                outfile.write(f"found '{name}': {rating}\n")
            else:
                outfile.write(f"not found {name}\n")

            print(f"name: {name}, rating: {rating}")
            outfile.flush()