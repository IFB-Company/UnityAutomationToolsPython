import os

CLASS_NAME_CS = 'SceneSwitcher'
DEFAULT_NAMESPACE_CS = 'UAT_Generated'

FUNCS_BODY_KEY = '[FUNC]'

def generateFullSceneSwitcherClassByScenesList_CS(scenesAbsPathCollection):
    classBody = generateSceneSwitcherClassBody(CLASS_NAME_CS)
    
    return ''

def generateSceneSwitcherClassBody(className):
    lines = [
            'using UnityEditor;',
            '\nusing UnityEditor.SceneManagement;',
            '\nusing UnityEngine;',
            '\n',
            f'\nnamespace {DEFAULT_NAMESPACE_CS}',
            '\n{',
            f'\n\tpublic class {className} : MonoBehaviour',
            '\n\t{',
            f'\n\t\t{FUNCS_BODY_KEY}',
            '\n\t}',
            '\n}'
        ]
    returnData = ''
    for line in lines:
        returnData += line
    return returnData

def generateEditorFunctionForScene_CS(toolPath, fullScenePath):
    croppedPath = cropFullScenePathForRelativeInUnity(fullScenePath)
    pureSceneName = getSceneNameByCroppedPath(croppedPath)

    funcText = ''
    menuItemAttr = generateAttributeForSceneSwitchFunc_CS(toolPath, pureSceneName)
    funcName = generateLoadFunctionName_CS(pureSceneName)

    pasteFlag = '[f]'
    openSceneUnityFuncName = f'EditorSceneManager.OpenScene("{pasteFlag}");'
    openSceneUnityFuncName = openSceneUnityFuncName.replace(pasteFlag, croppedPath)

    funcText += '\n\t' + menuItemAttr
    funcText += f'\n\tstatic void {funcName}'
    funcText += '\n\t{'
    funcText += f'\n\t\t{openSceneUnityFuncName}'
    funcText += '\n\t}'

    return funcText

def generateLoadFunctionName_CS(pureSceneName):
    return 'Load_' + pureSceneName + '()'

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