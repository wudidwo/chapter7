import os

def run(**args):
    print("[*] IN dirlister moudle.")
    files = os.listdir(".")

    return str(files)