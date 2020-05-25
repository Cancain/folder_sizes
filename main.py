#!/usr/bin/env python3
import os

class Content:
    folders = [],
    sizes = [],

def get_folder_contents():
    found_dirs = []
    found_sizes = []

    for _, dirs, files in os.walk(".", topdown=False):

        for dir in dirs:
          found_dirs.append(dir)
          print(os.path.getsize(dir) * 4e-6)

    content = Content
    content.folders = found_dirs

    return content

def main():
    content = get_folder_contents()
    print(content.folders)

if __name__ == "__main__":
    main()
