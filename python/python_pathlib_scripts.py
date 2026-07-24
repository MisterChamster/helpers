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


def rename_node(
        node_path: Path, new_name: str, new_ext: str|None = None
        ) -> None:
    new_filepath = node_path.with_stem(new_name)
    if new_ext is not None:
        new_filepath.with_suffix(new_ext)
    node_path.rename(new_filepath)


class Recurrer:
    iter: int

    def recurrer_setup(self, dir_path: Path) -> int:
        self.iter = 0
        self.__recurrer(dir_path)
        return self.iter

    def __recurrer(self, dir_path: Path) -> None:
        self.iter += 1
        dirs_list = get_dirs_from_dir(dir_path)
        for dir_path in dirs_list:
            self.__recurrer(dir_path)
