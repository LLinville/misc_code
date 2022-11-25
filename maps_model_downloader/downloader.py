from pathlib import Path
import os
from EarthReverseEngineeringUtils.octant_to_latlong import LatLonBox

from EarthReverseEngineeringUtils.find_overlaps import find_overlaps
from misc.file_utils import first_available_path

exporter_path = "\"C:/Users/Eracoy/Google Drive/Coding/Python projects/misc_code/maps_model_downloader/earth-reverse-engineering/exporter\""

base_directory = "H:/3d/models/photogrammetry/earthExporterDownloads/chunks"


bounds_name = 'whole_park'

reuse_directory = True
if not reuse_directory:
    save_directory = first_available_path(base_directory + "/{}")
else:
    save_directory = base_directory + f"/{bounds_name}"

bounds = {
    'whole_park':  (37.797368, -119.728486, 37.700, -119.477087),
    'wide_elcap': (37.741824, -119.642688, 37.729782, -119.620848),
    'face_elcap': (37.7265, -119.641358, 37.7265)
}

coords = bounds[bounds_name]

level = 18

overlaps = find_overlaps(LatLonBox(north=coords[0], south=coords[2], west=coords[1], east=coords[3]), 30)
# overlaps = {
#     level: chunks for level, chunks in overlaps.items()
#     if level in levels_to_download
# }
# chunks_to_download = [
#     20527070735256,
#     20527070735257
# ]

starting_chunk_depth = min([15, level, max(overlaps.keys())])
chunks_to_download = [chunk.path for chunk in overlaps[starting_chunk_depth]]

chunks_to_download = [str(chunk) for chunk in chunks_to_download]




level_path = save_directory + f"/level_{level}"
os.system(f"node {exporter_path}/dump_obj.js {len(chunks_to_download)} {' '.join(chunks_to_download)} {level} \"{level_path}\"")

# for level, chunk_id in chunks_to_download:
#
#     level_path = save_directory + f"/level_{level}"
#     if Path(level_path).exists() and not reuse_directory:
#         print(f"Path already exists: {level_path}")
#         break
#     # Path(level_path).mkdir(parents=True, exist_ok=True)
#     os.system(f"node {exporter_path}/dump_obj.js {chunk_ids[0]} {chunk_ids[1]} {level} \"{level_path}\"")


