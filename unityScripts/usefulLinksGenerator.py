import os
import sys
import shutil

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

import global_info


def createHookPrefabInPath(folderPath):
    dataDirPath = global_info.getDataDirPath()
    hookFileSource = os.path.join(dataDirPath, global_info.FOLDER_HOOK_FILE_NAME)
    destPath = os.path.join(folderPath, global_info.FOLDER_HOOK_FILE_NAME)
    shutil.copyfile(hookFileSource, destPath)
    print(f'Hook created in path: {destPath}')

