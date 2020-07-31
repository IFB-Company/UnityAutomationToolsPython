import os
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
    for file in testScriptsPath:
        runCommand = command + file
        os.system(runCommand)

runAllTests()

