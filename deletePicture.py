import os

if __name__ == "__main__":
    path = "D:/MyProject/python/testLOL/picture"
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            os.remove(path + '/' + file)
