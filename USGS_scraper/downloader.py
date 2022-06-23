import urllib.request
import os
import time

storage_path = "N:/usgs-data/elevation"
urls_to_download_path = "to_download.txt"

MB = 1024 ** 2

max_bps = 2 * MB
max_bytes_downloaded = 150 * 1024 * MB
total_bytes_downloaded = 0

with open(urls_to_download_path, 'r') as urls_to_download_file:
    urls_to_download = [line.strip() for line in urls_to_download_file.readlines()]

for url in urls_to_download:
    start_time = time.time()
    print(f"\nDownloading {url}")

    file_name = url.split('/')[-1]
    directory = url.split('/')[-3]
    file_path = f"{storage_path}/{directory}/{file_name}"

    if os.path.exists(file_path):
        print(f"Skipping file {file_path}. Already found with size {os.stat(file_path).st_size // MB} mb")
        continue

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    result = urllib.request.urlretrieve(url, file_path)
    file_size = int(result[1].get('Content-Length'))
    total_bytes_downloaded += file_size
    duration = time.time() - start_time
    wait_left = file_size / max_bps - duration

    print(f"Downloaded {file_size // MB} mb in {int(duration)} sec")
    print(f"Total downloaded: {total_bytes_downloaded // MB} mb")

    if total_bytes_downloaded > max_bytes_downloaded:
        print(f"Downloaded past target of {max_bytes_downloaded // MB} mb. ({total_bytes_downloaded // MB} mb total)")
        break
    
    print(f"Waiting {int(wait_left)} sec to meet {max_bps // MB} mb/s goal")
    time.sleep(max(wait_left, 0))

