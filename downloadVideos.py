import urllib.request

with open("videoUrls.txt", 'r') as file:
    videoData = file.readlines()
    videoData = [video.rstrip() for video in videoData]

videoUrls = [url.split(',') for url in videoData]

for url in videoUrls:
    print(f"Downloading {url[0]}...", end='', flush=True)
    urllib.request.urlretrieve(url[1], f"Videos/{url[0]}.mp4")
    print("finished")