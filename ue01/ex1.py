import requests
import shutil
import os


def download_image():
    url = "https://aws.random.cat/meow"
    folder = "images"
    response = requests.get(url)
    json = response.json()
    image_url = json["file"]
    image_name = image_url.split("/")[-1]
    print(image_url)

    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        path = os.path.join(folder, image_name)
        # Open a local file with wb ( write binary ) permission.
        with open(path, "wb") as f:
            shutil.copyfileobj(r.raw, f)

        print("Image sucessfully Downloaded: ", path)
    else:
        print("Image Couldn't be retreived")


def main():
    for i in range(1, 20):
        download_image()


main()
