import os


def generateEditorFunctionForScene_CS(fullScenePath):
    croppedPath = cropFullScenePathForRelativeInUnity(fullScenePath)
    pureSceneName = getSceneNameByCroppedPath(croppedPath)

def generateAttributeForSceneSwitchFunc_CS(toolPath, pureSceneName):
    toolPathForAttr = os.path.join(toolPath, pureSceneName)
    attr = f'[MenuItem("{toolPathForAttr}")]'
    return attr

def getSceneNameByCroppedPath(croppedPath):
    sceneName = os.path.basename(croppedPath)
    sceneName = sceneName.split('.')[0]
    return sceneName

def cropFullScenePathForRelativeInUnity(fullScenePath):
    splitted = fullScenePath.split('/')
    croppedPath = ''
    isStartAppend = False
    for path in splitted:
        if path == 'Assets':
            isStartAppend = True

        if isStartAppend:
            croppedPath = os.path.join(croppedPath, path)

    return croppedPath

def generateFile(path, fileName, fileContent):
    if os.path.exists(path) == False:
        os.mkdir(path)
    fullPath = os.path.join(path, fileName)
    scriptFile = open(fullPath, 'w')
    scriptFile.write(fileContent)
    scriptFile.close()
    return fullPath