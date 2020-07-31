import os
import sys
import unittest

scriptDir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] != scriptDir:
    sys.path[0] = scriptDir

import sceneSwitcherGenerator


class SceneSwitcherTests(unittest.TestCase):
    def test_generateSceneSwitcherScript(self):
        testDir = 'testFolder'
        testFile = "testSceneSwitcher.cs"
        fullPath = os.path.join(testDir, testFile)
        generatedPath = sceneSwitcherGenerator.generateFile(testDir, testFile)

        self.assertTrue(fullPath in generatedPath)

if __name__ == "__main__":
    unittest.main()
