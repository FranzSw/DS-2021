import json
import requests
import os
import shutil


def do_request(search_term):
    url = f"https://de1.api.radio-browser.info/json/stations/byname/{search_term}"
    response = requests.get(url)
    result = response.json()
    folder = "blub"

    if response.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        path = os.path.join(folder, search_term)
        # Open a local file with wb ( write binary ) permission.
        with open(path, "w") as f:
            pretty = json.dumps(result, indent=4)
            f.write(pretty)

        print("Data sucessfully Downloaded: ", path)
    else:
        print("Data Couldn't be retreived")

    print(json.dumps(result, indent=4))


def main():
    search_terms = ["teddy", "Fritz", "RBB", "BB Radio"]
    for search_term in search_terms:
        do_request(search_term)


main()
