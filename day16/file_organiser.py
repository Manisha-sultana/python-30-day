import argparse
import shutil
from pathlib import Path


def organise_files(folder, dry_run=False):
    folder = Path(folder)

    if not folder.is_dir():
        raise NotADirectoryError(f"Folder not found: {folder}")

    for file_path in folder.iterdir():
        if not file_path.is_file():
            continue

        # Do not move this running script.
        if file_path.resolve() == Path(__file__).resolve():
            continue

        extension = file_path.suffix.lower().lstrip(".")
        folder_name = extension if extension else "no_extension"
        destination_folder = folder / folder_name
        destination = destination_folder / file_path.name

        # Do not overwrite an existing file.
        if destination.exists():
            print(f"Skipped (already exists): {file_path.name}")
            continue

        if dry_run:
            print(f"Would move: {file_path.name} -> {folder_name}/")
        else:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {folder_name}/")


def main():
    parser = argparse.ArgumentParser(
        description="Organise files by extension."
    )
    parser.add_argument("folder", help="Folder path to organise")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned moves without moving files"
    )
    args = parser.parse_args()

    try:
        organise_files(args.folder, args.dry_run)
    except (NotADirectoryError, PermissionError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()