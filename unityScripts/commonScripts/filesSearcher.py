import os

def findFilesByType(path, fileExtension):
    data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fileExtension):
                filePath = os.path.join(root, file)
                data.append(filePath)
    return data