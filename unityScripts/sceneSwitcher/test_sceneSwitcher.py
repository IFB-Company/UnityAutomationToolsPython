import os
import sys
import unittest

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

import sceneSwitcherGenerator

sceneFullPath = '/Users/intfloatbool/Documents/SRC/Python/IFB_UnityAutomationTools/unityScripts/test_data/testUnityProject_0/Assets/Scenes/Levels/Level_1.unity'

class SceneSwitcherTests(unittest.TestCase):
    def test_generateFile(self):
        testDirName = 'testFolder'
        testFile = "testSceneSwitcher.cs"
        testDirPath = os.path.join(scriptDir, testDirName)
        fullPath = os.path.join(testDirPath, testFile)
        fileText = 'hey bro from tests!'
        generatedPath = sceneSwitcherGenerator.generateFile(testDirPath, testFile, fileText)

        isFileExists = os.path.exists(generatedPath)
        readedContent = ''
        if isFileExists:
            file = open(generatedPath, 'r')
            readedContent = file.read()
            file.close()

        self.assertEqual(fullPath,generatedPath)
        self.assertTrue(isFileExists)
        self.assertEqual(fileText, readedContent)
    
    def test_cropScenePathForUnity(self):
        unityCorrectPath = 'Assets/Scenes/Levels/Level_1.unity'

        croppedPath = sceneSwitcherGenerator.cropFullScenePathForRelativeInUnity(sceneFullPath)

        self.assertEqual(croppedPath, unityCorrectPath)

    def test_getSceneNameByCroppedPath(self):
        croppedPath = sceneSwitcherGenerator.cropFullScenePathForRelativeInUnity(sceneFullPath)
        sceneName = 'Level_1'

        generatedName = sceneSwitcherGenerator.getSceneNameByCroppedPath(croppedPath)

        self.assertEqual(generatedName, sceneName)

    def test_generateAttributeForSceneSwitchFunc_CS(self):
        sceneName = 'Level_1'
        windowName = 'UAT_Scenes'
        contextPath = windowName + '/' + sceneName
        completeAttrCS = f'[MenuItem("{contextPath}")]'

        generatedAttr = sceneSwitcherGenerator.generateAttributeForSceneSwitchFunc_CS(windowName, sceneName)

        self.assertEqual(generatedAttr,completeAttrCS)

if __name__ == "__main__":
    unittest.main()
