import argparse
import os
import stat
import datetime

def get_file_info(file_name, options):
    if not os.path.exists(file_name):
        print("File does not exist")
        return

    file_stats = os.stat(file_name)

    if options.size:
        print(f"Size(B): {file_stats.st_size}")

    if options.permissions:
        permissions = stat.filemode(file_stats.st_mode)
        print(f"Permissions: {permissions}")

    if options.owner:
        owner = file_stats.st_uid
        print(f"Owner: {owner}")

    if options.last_modified:
        last_modified_time = datetime.datetime.fromtimestamp(file_stats.st_mtime)
        print(f"Last Modified: {last_modified_time}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get information about a file")
    parser.add_argument("file_name", help="Name of the file")
    parser.add_argument("--size", "-s", action="store_true", help="Print file size")
    parser.add_argument("--permissions", "-p", action="store_true", help="Print file permissions")
    parser.add_argument("--owner", "-o", action="store_true", help="Print file owner")
    parser.add_argument("--last-modified", "-m", action="store_true", help="Print last modified time")

    args = parser.parse_args()
    get_file_info(args.file_name, args)
