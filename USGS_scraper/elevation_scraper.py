import requests
import urllib.request
from bs4 import BeautifulSoup
from time import sleep

# "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/NM_NRCS_MiddleRioGrande_2017_D18/TIFF/USGS_1M_13_x28y382_NM_NRCS_MiddleRioGrande_2017_D18.tif"

base_path = "https://thor-f5.er.usgs.gov/ngtoc/metadata/waf/elevation/1_meter/geotiff/"
page = requests.get(base_path)

soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all("a")

directories = [link.attrs['href'][:-1] for link in links]
directories = [d for d in directories if d[0] not in ['?', '/']]

paths_to_download = []

for directory in directories:
    print(f"Opening {directory}")
    sleep(5)
    directory_path = base_path + directory
    page = requests.get(directory_path)
    links = BeautifulSoup(page.content, 'html.parser').find_all('a')
    paths = [link.attrs['href'].split('.')[0] for link in links]
    paths = [p for p in paths if p[0] not in ['?', '/']]

    for path in paths:
        paths_to_download.append(f"https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/{directory}/TIFF/{path}.tif")

with open("to_download.txt", "a") as outfile:
    outfile.writelines('\n'.join(paths_to_download))


