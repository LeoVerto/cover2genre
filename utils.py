import requests
import os
import shutil


def download_coverart(release_group: str, path: str) -> bool:
    base_url = "https://coverartarchive.org/release-group/{mbid}/front-250"
    url = base_url.format(mbid=release_group)

    r = requests.get(url, stream=True)

    if r.status_code == 200:
        pass
    elif r.status_code == 404:
        return False
    else:
        raise Exception("Invalid HTTP response code")

    file = os.path.join(path, release_group + ".png")
    with open(file, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    return True
