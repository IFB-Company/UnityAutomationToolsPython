EDITOR_FOLDER_NAME = "Editor"
SCRIPTS_DIR_NAME = "UAT_Scripts"
UNITY_SCENES_EXTENSION = '.unity'
FOLDER_HOOK_FILE_NAME = '[HOOK_FOLDER].prefab'

import os

def getDataDirPath():
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    dataFolderName = 'data'
    return os.path.join(scriptDir, dataFolderName)