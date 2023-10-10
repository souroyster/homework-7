import os
import shutil
from setuptools import setup

def clean_folder(folder_path):
    # Ваш код для очищення папки тут
    pass


setup(
    name="clean_folder",
    version="0.1",
    packages=["clean_folder"],
    entry_points={
        "console_scripts": [
            "clean-folder=clean_folder.clean:clean_folder",
        ],
    },
)

if __name__ == "__main__":
    folder_path = input("Введіть шлях до папки для очищення: ")
    clean_folder(folder_path)