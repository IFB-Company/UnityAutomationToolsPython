import sys
import os
import unittest

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

from ...unityScripts import usefulLinksGenerator
from ...unityScripts import global_info

class UsefulLinksGeneratorTests(unittest.TestCase):
    def test_createHookPrefabInPath(self):
        testUnityFolderPath = '/Users/intfloatbool/Documents/SRC/Python/IFB_UnityAutomationTools/unityScripts/tests/test_data/testUnityProject_0/Assets/Prefabs'
        fileInFolderPath = os.path.join(testUnityFolderPath, global_info.FOLDER_HOOK_FILE_NAME)
        usefulLinksGenerator.createHookPrefabInPath(testUnityFolderPath)

        isFileExist = os.path.exists(fileInFolderPath)
        self.assertTrue(isFileExist)

if __name__ == '__main__':
    unittest.main()