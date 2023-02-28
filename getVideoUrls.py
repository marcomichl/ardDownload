import json
import requests
from bs4 import BeautifulSoup

def getVideoData(url):
    htmlSite = requests.get(url, allow_redirects=True).text

    soup = BeautifulSoup(htmlSite, 'html.parser')

    script = soup.find('script', id="fetchedContextValue")
    js = json.loads(script.text)[0][1]

    title = js["data"]["title"][-8:-1].replace('/', '_')
    videoUrlArray = js["data"]["widgets"][0]["mediaCollection"]["embedded"]["streams"][0]["media"]
    videoUrl = None
    for quality in videoUrlArray:
        if quality["forcedLabel"] == "Full HD":
            videoUrl = quality["url"]
    if videoUrl == None:
        print(f"Failed for {title}, searchig for 720p")
        for quality in videoUrlArray:
            if quality["_quality"] == 3:
                videoUrl = quality["_stream"]
    if videoUrl == None:
        print(f"No HD quality for {title}.")
    return title, videoUrl

with open("siteUrls.txt") as file:
    siteUrls = file.readlines()
    siteUrls = [siteUrl.rstrip() for siteUrl in siteUrls]

videoUrls = []
for url in siteUrls:
    videoUrls.append(getVideoData(url))

with open("videoUrls.txt", 'w') as file:
    for data in videoUrls:
        file.write(f"{data[0]},{data[1]}\n")
        print(f"Wrote {data[0]}")