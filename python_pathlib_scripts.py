from pathlib import Path
from typing import Literal


def get_dirs_from_dir(
    dir_path: Path,
    sort_it:  bool = True
) -> list[Path]:
    dirs_list = [node for node in dir_path.iterdir()
                 if node.is_dir()]
    if sort_it:
        dirs_list.sort()

    return dirs_list


def get_files_from_dir(
    dir_path: Path,
    sort_it:  bool = True
) -> list[Path]:
    files_list = [node for node in dir_path.iterdir()
                 if node.is_file()]
    if sort_it:
        files_list.sort()

    return files_list


def get_nodes_from_dir(
    dir_path: Path,
    node_type: Literal["file", "dir"],
    sort_it: bool = True
) -> list[Path]:
    if node_type == "file":
        nodes_list = [node for node in dir_path.iterdir()
                     if node.is_file()]
    elif node_type == "dir":
        nodes_list = [node for node in dir_path.iterdir()
                     if node.is_dir()]
    if sort_it:
        nodes_list.sort()

    return nodes_list


def get_filetype_files_from_dir(
    dir_path: Path,
    file_type: str = ".jpg",
    sort_it:  bool = True
) -> list[Path]:
    files_list = [node for node in dir_path.iterdir()
                 if (node.is_file() and
                     node.suffix == file_type)]
    if sort_it:
        files_list.sort()

    return files_list


def is_filetype_in_dir(
        dir_path: Path, file_type: str = ".jpg") -> bool:
    for node in dir_path.iterdir():
        if (node.is_file() and
            node.suffix == file_type and
            not node.name.startswith(".")):
            return True
    return False
