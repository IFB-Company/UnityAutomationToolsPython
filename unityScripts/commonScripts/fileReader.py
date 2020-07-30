def readFile(path):
    print("Try read file by path: " + str(path))
    fileText = ''
    try:
        with open(path,'r') as file:
            fileText = file.read()

    except Exception:
        return ''
    return fileText