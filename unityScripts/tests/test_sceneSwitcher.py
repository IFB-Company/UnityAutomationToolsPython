import os
import sys
import unittest

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

from ...unityScripts import sceneSwitcherGenerator 

from ..commonScripts import filesSearcher



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
        line_0 = f'\n\t\t[MenuItem("UAT_Scenes/Level_1")]'
        line_1 = '\n\t\tstatic void Load_Level_1()'
        line_2 = '\n\t\t{'
        line_3 = '\n\t\t\tEditorSceneManager.OpenScene("Assets/Scenes/Levels/Level_1.unity");'
        line_4 = '\n\t\t}'

        fullText = line_0 + line_1 + line_2 + line_3 + line_4
        
        generatedFuncText = sceneSwitcherGenerator.generateEditorFunctionForScene_CS(windowName, sceneFullPath)

        self.assertEqual(fullText, generatedFuncText)

    def test_generateSceneSwitcherClassBody(self):
        className = 'SceneSwitcher'
        defaultNameSpace = 'UAT_Generated'
        lines = [
            'using UnityEditor;',
            '\nusing UnityEditor.SceneManagement;',
            '\nusing UnityEngine;',
            '\n',
            f'\nnamespace {defaultNameSpace}',
            '\n{',
            f'\n\tpublic class {className} : MonoBehaviour',
            '\n\t{',
            '\n\t\t[FUNC]',
            '\n\t}',
            '\n}'
        ]

        fullText = ''
        for line in lines:
            fullText += line

        generatedText = sceneSwitcherGenerator.generateSceneSwitcherClassBody(className)

        self.assertEqual(generatedText, fullText)

    def test_generateFullSceneSwitcherClassByScenesList_CS(self):
        className = sceneSwitcherGenerator.CLASS_NAME_CS
        defaultNameSpace = sceneSwitcherGenerator.DEFAULT_NAMESPACE_CS
        
        scenesPath = '/Users/intfloatbool/Documents/SRC/Python/IFB_UnityAutomationTools/unityScripts/tests/test_data/testUnityProject_0/Assets'
        scenesAbsPathList = filesSearcher.findFilesByType(scenesPath, '.unity')

        toolPath = 'UAT_SceneSwitcher'

        scene1AbsPath = scenesAbsPathList[0]
        scene1PureName = sceneSwitcherGenerator.getSceneNameByCroppedPath(scene1AbsPath)
        scene1RelativePath = sceneSwitcherGenerator.cropFullScenePathForRelativeInUnity(scene1AbsPath)
        scene1Attr = sceneSwitcherGenerator.generateAttributeForSceneSwitchFunc_CS(toolPath, scene1PureName)
        scene1FuncName = sceneSwitcherGenerator.generateLoadFunctionName_CS(scene1PureName)

        scene2AbsPath = scenesAbsPathList[1]
        scene2PureName = sceneSwitcherGenerator.getSceneNameByCroppedPath(scene2AbsPath)
        scene2RelativePath = sceneSwitcherGenerator.cropFullScenePathForRelativeInUnity(scene2AbsPath)
        scene2Attr = sceneSwitcherGenerator.generateAttributeForSceneSwitchFunc_CS(toolPath, scene2PureName)
        scene2FuncName = sceneSwitcherGenerator.generateLoadFunctionName_CS(scene2PureName)

        scene3AbsPath = scenesAbsPathList[2]
        scene3PureName = sceneSwitcherGenerator.getSceneNameByCroppedPath(scene3AbsPath)
        scene3RelativePath = sceneSwitcherGenerator.cropFullScenePathForRelativeInUnity(scene3AbsPath)
        scene3Attr = sceneSwitcherGenerator.generateAttributeForSceneSwitchFunc_CS(toolPath, scene3PureName)
        scene3FuncName = sceneSwitcherGenerator.generateLoadFunctionName_CS(scene3PureName)

        lines = [
            'using UnityEditor;',
            '\nusing UnityEditor.SceneManagement;',
            '\nusing UnityEngine;',
            '\n',
            f'\nnamespace {defaultNameSpace}',
            '\n{',
            f'\n\tpublic class {className} : MonoBehaviour',
            '\n\t{',
            '\n\t\t',
            f'\n\t\t{scene1Attr}',
            f'\n\t\tstatic void {scene1FuncName}',
            '\n\t\t{',
            f'\n\t\t\tEditorSceneManager.OpenScene("{scene1RelativePath}");',
            '\n\t\t}\n',
            f'\n\t\t{scene2Attr}',
            f'\n\t\tstatic void {scene2FuncName}',
            '\n\t\t{',
            f'\n\t\t\tEditorSceneManager.OpenScene("{scene2RelativePath}");',
            '\n\t\t}\n',
            f'\n\t\t{scene3Attr}',
            f'\n\t\tstatic void {scene3FuncName}',
            '\n\t\t{',
            f'\n\t\t\tEditorSceneManager.OpenScene("{scene3RelativePath}");',
            '\n\t\t}\n',
            '\n\t}',
            '\n}'
        ]

        expectedText = ''
        for line in lines:
            expectedText += line 
            
        generatedText = sceneSwitcherGenerator.generateFullSceneSwitcherClassByScenesList_CS(scenesPath)
        self.maxDiff = 5959
        self.assertEqual(expectedText, generatedText)

if __name__ == "__main__":
    unittest.main()
