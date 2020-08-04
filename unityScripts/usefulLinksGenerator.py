import os
import sys
import shutil

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

import global_info

CLASS_NAME_CS = 'UsefulLinks'

def generateUsefulLinksClassBody():
    namespaceName = global_info.DEFAULT_NAMESPACE_CS
    
    return ''

def generateFuncForLink(hookPath):
    dirName = os.path.basename(os.path.dirname(hookPath))
    funcName = 'Open'
    dirName = dirName.replace('-','_')
    dirName = dirName.replace(' ','_')
    funcName += dirName
    funcName += '()'
    lines = [
        f'\n[MenuItem("{CLASS_NAME_CS}/dirName")]',
        f'\nprivate static void {funcName}',
    ]

def createHookPrefabInPath(folderPath):
    dataDirPath = global_info.getDataDirPath()
    hookFileSource = os.path.join(dataDirPath, global_info.FOLDER_HOOK_FILE_NAME)
    destPath = os.path.join(folderPath, global_info.FOLDER_HOOK_FILE_NAME)
    if not os.path.exists(destPath):
        shutil.copyfile(hookFileSource, destPath)
    