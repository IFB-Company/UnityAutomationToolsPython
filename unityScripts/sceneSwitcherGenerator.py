import os
import sys

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir


from .commonScripts import filesSearcher

TOOL_PATH = 'UAT_SceneSwitcher'
CLASS_NAME_CS = 'SceneSwitcher'
DEFAULT_NAMESPACE_CS = 'UAT_Generated'

FUNCS_BODY_KEY = '[FUNC]'

def generateFullSceneSwitcherClassByScenesList_CS(scenesAbsPathCollection):
    classBody = generateSceneSwitcherClassBody(CLASS_NAME_CS)
    splitted = classBody.split(FUNCS_BODY_KEY)
    
    fullLines = []
    fullLines.append(splitted[0])
    
    scenesAbsPaths = filesSearcher.findFilesByType(scenesAbsPathCollection, '.unity')

    for scenePath in scenesAbsPaths:
        funcBody = generateEditorFunctionForScene_CS(TOOL_PATH, scenePath)
        fullLines.append(funcBody)
        fullLines.append('\n')

    fullLines.append(splitted[1])

    completeText = ''

    for line in fullLines:
        completeText += line

    return completeText

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

    funcText += '\n\t\t' + menuItemAttr
    funcText += f'\n\t\tstatic void {funcName}'
    funcText += '\n\t\t{'
    funcText += f'\n\t\t\t{openSceneUnityFuncName}'
    funcText += '\n\t\t}'

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