import os
import datetime
import sys

testLabel = 'test_'
pyExtensionLabel = '.py'
runnerPath = scriptDir = os.path.dirname(os.path.abspath(__file__))
scriptsPath = os.path.join(runnerPath, "unityScripts")

testScriptsPath = []

for root, dirs, files in os.walk(scriptsPath):
    for file in files:
        if file.startswith(testLabel) and file.endswith(pyExtensionLabel):
            filePath = os.path.join(root, file)
            testScriptsPath.append(filePath)


def runAllTests():
    command = "python3 -m unittest "
    separatorStr = '\n*** *** *** *** *** *** ***\n'
    separatorStr_second = '\n||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| \n'
    print(separatorStr)
    print(separatorStr_second)
    print('Run tests at: ', datetime.datetime.now())
    print(separatorStr_second)
    for file in testScriptsPath:
        print(separatorStr)
        fileName = os.path.basename(file)
        print('Run test file: ', fileName, '...')
        runCommand = command + file
        os.system(runCommand)

runAllTests()

