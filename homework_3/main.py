import os
import pathlib
from pathlib import Path


def read_sorted_files():
    catalog_path = Path(pathlib.Path.cwd(), "sorted")
    files_dict = {}
    for file in os.listdir(catalog_path):
        with open(Path(pathlib.Path.cwd(), "sorted", file), encoding='utf-8') as f:
            files_dict[len(f.readlines())] = Path(pathlib.Path.cwd(), "sorted", file)
    sorted_dict = dict(sorted(files_dict.items()))
    for key in sorted_dict:
        with open(sorted_dict[key], encoding='utf-8') as file:
            print(os.path.basename(sorted_dict[key]))
            with open(sorted_dict[key], encoding='utf-8') as f:
                print(len(f.readlines()))
            print(file.read())


read_sorted_files()




