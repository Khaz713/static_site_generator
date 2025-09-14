import shutil
import os
import sys

from generate_page import generate_pages_recursive

def clear(dir_path):
    shutil.rmtree(dir_path, ignore_errors=True)
    os.mkdir(dir_path)

def copy_dir_to(path, to_dir):
    content = os.listdir(path)
    for item in content:
        if os.path.isdir(os.path.join(path, item)):
            copy_dir_to(os.path.join(path, item), os.path.join(to_dir, item))
        if os.path.isfile(os.path.join(path, item)):
            file_path = os.path.join(to_dir, item)
            if not os.path.exists(to_dir):
                os.mkdir(to_dir)
            shutil.copy(os.path.join(path, item), file_path)




def main():
    basepath = '/'
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    clear("docs")
    copy_dir_to("static", "docs")
    print(sys.argv)
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
