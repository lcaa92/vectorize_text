import requests
import os


PAGES = [
    "https://en.wikipedia.org/wiki/UEFA_Champions_League",
    "https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica",
    "https://en.wikipedia.org/wiki/UEFA_Nations_League",
    "https://en.wikipedia.org/wiki/UEFA_European_Championship",
    "https://en.wikipedia.org/wiki/FIFA_World_Cup"
]

OUTPUT_FOLDER = 'output_data'

if __name__ == '__main__':
    print('Starting')

    # create output_foled if not exists

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for page in PAGES:
        resp = requests.get(page)

        print(resp.text)
        filename = page.split('/')[-1]

        with open(f"{OUTPUT_FOLDER}/{filename}.html", "w") as f:
            f.write(resp.text)
