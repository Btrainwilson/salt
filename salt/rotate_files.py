#!/usr/bin/env python

import os
import sys
import shutil


def rotate_file(target_file_path, directory):
    log_file_name = ".rotation.txt"
    log_file_path = os.path.join(directory, log_file_name)

    if not os.path.isfile(target_file_path):
        print(
            f"The target file {target_file_path} does not exist. Will copy the first file in the directory."
        )

    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Read the current file from the log file
    current_file = ""
    if os.path.isfile(log_file_path):
        with open(log_file_path, "r") as log_file:
            current_file = log_file.read().strip()

    # List all files in the directory, excluding the log file
    files = sorted(
        [
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f)) and f != log_file_name
        ]
    )

    if not files:
        print("No files in the directory to rotate.")
        return

    # Find the next file to rotate
    try:
        current_index = files.index(current_file)
        next_file = files[(current_index + 1) % len(files)]
    except ValueError:
        # Current file not in list, or list is empty
        next_file = files[0]

    # Update the log file with the name of the next file
    with open(log_file_path, "w") as log_file:
        log_file.write(next_file)

    # Perform the rotation
    new_file_path = os.path.join(directory, next_file)
    shutil.copy2(new_file_path, target_file_path)
    print(f"{target_file_path} has been overwritten with {new_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rotate_file.py [target_file_path] [directory]")
        sys.exit(1)

    target_file_path = sys.argv[1]
    directory = sys.argv[2]

    rotate_file(target_file_path, directory)
