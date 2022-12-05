import stl

from pymesh.obj import Obj

path_to_convert = "H:\\3d\\models\\photogrammetry\\earthExporterDownloads\\chunks\\matterhorn\\level_17\\obj\\17\\model.obj"

Obj(path_to_convert)

vertex_lines = [line for line in lines if line[0] == 'v']

print(len(lines))
