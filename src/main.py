import os
import shutil
from generate import generate_pages_recursive

source_directory = "static"
destination_directory = "public"
content_directory = "/content"
template = "template.html"

def copy_directory(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        item_src = os.path.join(src, item)

        if os.path.isfile(item_src):
            shutil.copy(item_src, os.path.join(dst, item))
        elif os.path.isdir(item_src):
            copy_directory(item_src, os.path.join(dst, item))

def main():
    if not os.path.exists(source_directory):
        raise Exception("Source files not located")
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)

    copy_directory(source_directory, destination_directory)

    generate_pages_recursive(content_directory, template, destination_directory)

main()