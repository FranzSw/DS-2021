import requests
import shutil
import os

folder = "images"


def download_image():
    url = "https://aws.random.cat/meow"
    response = requests.get(url)
    json = response.json()
    image_url = json["file"]
    image_name = image_url.split("/")[-1]
    print(image_url)

    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        path = os.path.join(folder, image_name)
        with open(path, "wb") as f:
            shutil.copyfileobj(r.raw, f)

        print("Image sucessfully downloaded: ", path)
        size = r.headers["content-length"]
        return int(size)
    else:
        print("Image couldn't be downloaded")
        return 0


def main():
    # Download 20 images
    minSize, maxSize, avgSize = 0, 0, 0
    for i in range(1, 20):
        size = download_image()
        if size > maxSize:
            maxSize = size
        # Also overwrite minSize if it's the first image / previous failed
        if size < minSize or minSize == 0:
            minSize = size
        avgSize += size
    avgSize /= 20

    # Save the results to a file
    with open(os.path.join(folder, "_meta.txt"), "w") as f:
        f.write(
            "Min size (bytes): {}\nMax size: {}\nAverage size: {}".format(
                minSize, maxSize, avgSize
            )
        )


main()
