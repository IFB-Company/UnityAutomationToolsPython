import os
import sys

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

import global_info

from commonScripts import filesSearcher

TOOL_PATH = 'UAT_SceneSwitcher'
CLASS_NAME_CS = 'SceneSwitcher'
DEFAULT_NAMESPACE_CS = 'UAT_Generated'
SCENE_SWITCHER_FILE_NAME = "SceneSwitcher.cs"

FUNCS_BODY_KEY = '[FUNC]'


def createSceneSwitcherScriptForUnityProject(projectAssetsPath):
    pathToScript = os.path.join(projectAssetsPath, global_info.SCRIPTS_DIR_NAME, global_info.EDITOR_FOLDER_NAME, SCENE_SWITCHER_FILE_NAME)

    scriptContent = generateFullSceneSwitcherClassByScenesList_CS(projectAssetsPath)

    pathWithoutFile = os.path.dirname(pathToScript)
    if not os.path.exists(pathWithoutFile):
        os.makedirs(pathWithoutFile)

    file = open(pathToScript, 'w')
    file.write(scriptContent)
    file.close()
    print("File generated?")

def generateFullSceneSwitcherClassByScenesList_CS(scenesAbsPathCollection):
    classBody = generateSceneSwitcherClassBody(CLASS_NAME_CS)
    splitted = classBody.split(FUNCS_BODY_KEY)
    
    fullLines = []
    fullLines.append(splitted[0])
    
    scenesAbsPaths = filesSearcher.findFilesByType(scenesAbsPathCollection, '.unity')
    if len(scenesAbsPathCollection) <= 0:
        raise Exception("No scenes found!")
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
    replaced1 = pureSceneName.replace(' ', '_')
    replaced2 = replaced1.replace('-','_')
    replaced2 = replaced2.replace('(','_')
    replaced2 = replaced2.replace(')','_')
    replaced2 = replaced2.replace('&','_')
    replaced2 = replaced2.replace('&&','_')
    return 'Load_' + replaced2 + '()'

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

if len(sys.argv) > 2:
    print("Some args here!")
    print(sys.argv)
    if sys.argv[1] == 'run': 
        unityAssetsPath = sys.argv[2]
        if os.path.exists(unityAssetsPath):
            createSceneSwitcherScriptForUnityProject(unityAssetsPath)
            print("Create data in: " + unityAssetsPath)