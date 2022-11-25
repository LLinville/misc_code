from pathlib import Path

def first_available_path(path_format, start=0, max=999):
    for i in range(start, max + 1):
        path = path_format.format(i)
        if not Path(path).exists():
            return path
    else:
        return None
