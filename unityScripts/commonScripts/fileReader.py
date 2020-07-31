def readFile(path):
    fileText = ''
    try:
        with open(path,'r') as file:
            fileText = file.read()

    except Exception:
        return ''
    return fileText