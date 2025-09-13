import shutil
import os

def clear_public():
    shutil.rmtree("public", ignore_errors=True)
    os.mkdir("public")

def copy_dir_to_public(path):
    content = os.listdir(path)
    print(content)
    for item in content:
        if os.path.isdir(os.path.join(path, item)):
            copy_dir_to_public(os.path.join(path, item))
        if os.path.isfile(os.path.join(path, item)):
            dir_path = os.path.join(path.replace("static", "public"))
            file_path = os.path.join(path.replace("static", "public"), item)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            shutil.copy(os.path.join(path, item), file_path)




def main():
    copy_dir_to_public("static")


if __name__ == "__main__":
    main()
