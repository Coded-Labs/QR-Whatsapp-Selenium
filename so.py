from pathlib import Path

import os

class NotExistPath(Exception):...


def exists_file(func):
    def file(*args, **kwargs):
        if os.path.exists(*args, **kwargs):
            func(*args, **kwargs)
        else:
            raise NotExistPath("Path not found")
    return file


# PATH Windows
@exists_file
def add_PATH_windows(path:Path) -> bool:
    """
    Add a path to the PATH variable in Windows
    """
    os.environ["PATH"] += os.pathsep + path.__str__()
    return True

@exists_file
def delete_path_windows(path:str|Path) -> bool:
    """
    Delete a path to the PATH variable in Windows
    """
    try:
        os.environ["PATH"] = os.environ["PATH"].replace(path.__str__(), "")
        return True
    except Exception as e:
        raise e