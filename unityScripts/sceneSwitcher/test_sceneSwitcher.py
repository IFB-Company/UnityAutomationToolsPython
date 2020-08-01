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

    def test_generateLoadFunctionName_CS(self):
        sceneName = 'Level_1'
        neededName = 'Load_Level_1()'

        generatedName = sceneSwitcherGenerator.generateLoadFunctionName_CS(sceneName)

        self.assertEqual(generatedName, neededName)

    def test_generateEditorFunctionForScene_CS(self):
        #[MenuItem("UAT_Scenes/Level_1")]
        #static void Load_Level_1()
        #{
            #EditorSceneManager.OpenScene("Assets/Scenes/Levels/Level_1.unity");
        #}
        windowName = 'UAT_Scenes'
        sceneName = 'Level_1'
        line_0 = f'\n\t[MenuItem("UAT_Scenes/Level_1")]'
        line_1 = '\n\tstatic void Load_Level_1()'
        line_2 = '\n\t{'
        line_3 = '\n\t\tEditorSceneManager.OpenScene("Assets/Scenes/Levels/Level_1.unity");'
        line_4 = '\n\t}'

        fullText = line_0 + line_1 + line_2 + line_3 + line_4
        
        generatedFuncText = sceneSwitcherGenerator.generateEditorFunctionForScene_CS(windowName, sceneFullPath)

        self.assertEqual(fullText, generatedFuncText)


if __name__ == "__main__":
    unittest.main()
