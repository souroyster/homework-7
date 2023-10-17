import sys
from pathlib import Path
import shutil
import unicodedata

CATEGORIES = {"Images": [".jpeg", ".png", ".jpg", ".svg"],
              "Video": [".avi", ".mp4", ".mov", ".mkv"],
              "Docs": [".docx", ".txt", ".pdf", ".rtf"],
              "Audio": [".mp3", ".wav", ".flac", ".wma"],
              "Archive": [".zip", ".gz", ".rar"]}

def normalize(name: str) -> str:
    name = unicodedata.normalize('NFD', name)  
    name = name.encode('ascii', 'ignore').decode('utf-8')  
    name = name.lower()  
    name = ''.join(['_' if not c.isalnum() else c for c in name])
    return name

def get_categories(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"

def move_file(file: Path, category: str, root_dir: Path) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = normalize(file.stem) 
    new_path = target_dir.joinpath(new_name + file.suffix)
    if not new_path.exists():
        file.replace(new_path)

def sort_folder(path: Path) -> None:
    for element in path.glob("**/*"):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path)

def delete_empty_folders(path: Path) -> None:
    for folder in path.glob("**/*"):
        if folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()

def extract_archives(path: Path) -> None:
    for archive in path.glob("**/*"):
        if archive.is_file() and archive.suffix.lower() in [".zip", ".gz", ".rar"]:
            target_dir = archive.with_suffix("")
            target_dir.mkdir(exist_ok=True)
            shutil.unpack_archive(str(archive), str(target_dir))

def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return "Folder does not exist"

    sort_folder(path)
    delete_empty_folders(path)
    extract_archives(path)

    return "All is Ok"

if __name__ == '__main__':
    print(main())
