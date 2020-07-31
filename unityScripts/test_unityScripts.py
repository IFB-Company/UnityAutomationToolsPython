import sys
import unittest
import os

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

from commonScripts import fileReader
from commonScripts import filesSearcher

testDataRelativePath = "test_data"
testDataPath = os.path.join(scriptDir, testDataRelativePath)
class UnityScriptsTests(unittest.TestCase):

    def test_fileReader(self):
        dataDirName = "readerData"
        dataFileName = "testDataFile.txt"
        filePath = os.path.join(testDataPath, dataDirName, dataFileName)
        fileReadedData = fileReader.readFile(filePath)
        self.assertNotEqual(fileReadedData, '')
        self.assertTrue('here' in fileReadedData)
        self.assertTrue('is' in fileReadedData)
        self.assertTrue('text' in fileReadedData)
        self.assertTrue('data' in fileReadedData)
        self.assertTrue('file' in fileReadedData)
        self.assertTrue('for' in fileReadedData)
        self.assertTrue('tests' in fileReadedData)
        return 0
    
    def test_filesSearcher(self):
        testDirName = 'testUnityProject_0'
        dirPath = os.path.join(testDataPath, testDirName)
        filesData = filesSearcher.findFilesByType(dirPath, ".unity")

        filePath_0 = '/Users/intfloatbool/Documents/SRC/Python/IFB_UnityAutomationTools/unityScripts/test_data/testUnityProject_0/Assets/Scenes/Main.unity'
        filePath_1 = '/Users/intfloatbool/Documents/SRC/Python/IFB_UnityAutomationTools/unityScripts/test_data/testUnityProject_0/Assets/Scenes/Levels/Level_0.unity'
        filePath_2 = '/Users/intfloatbool/Documents/SRC/Python/IFB_UnityAutomationTools/unityScripts/test_data/testUnityProject_0/Assets/Scenes/Levels/Level_1.unity'
        self.assertTrue(len(filesData) > 0)
        self.assertTrue(filePath_0 in filesData)
        self.assertTrue(filePath_1 in filesData)
        self.assertTrue(filePath_2 in filesData)
        self.assertTrue(len(filesData) == 3)


def runTest():
    unittest.main()

if __name__ == '__main__':
    unittest.main()