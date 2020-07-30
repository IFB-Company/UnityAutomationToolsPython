import unittest
import os
import commonScripts.fileReader

testDataRelativePath = "test_data"
scriptDir = os.path.dirname(os.path.abspath(__file__))
print("Absoule path: " + scriptDir)
class SceneSwitcherTests(unittest.TestCase):

    def test_IsOpenSourceFile(self):
        dataFileName = "testDataFile.txt"
        filePath = os.path.join(scriptDir, testDataRelativePath, dataFileName)
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

if __name__ == '__main__':
    unittest.main()