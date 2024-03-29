# coding=utf-8
import os
import sys

def clean_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)

def main():
    if len(sys.argv) != 2:
        print("Usage: clean-folder <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    clean_folder(folder_path)

if __name__ == '__main__':
    main()

