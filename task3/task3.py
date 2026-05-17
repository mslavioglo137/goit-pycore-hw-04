import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)

def print_directory_structure(path, indent=""):
    try:
        for item in path.iterdir():

            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}")

                print_directory_structure(item, indent + "    ")

            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")

    except PermissionError:
        print(f"{indent}{Fore.RED}Access denied: {path}")


def main():
    if len(sys.argv) < 2:
        print("Please provide directory path.")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print("Path does not exist.")
        return

    if not directory.is_dir():
        print("Path is not a directory.")
        return

    print(f"{Fore.YELLOW}📦 {directory.name}")

    print_directory_structure(directory)


if __name__ == "__main__":
    main()