import json

language = input("Enter language name Do you want to update: ")
errorName = input("Which error you want to update: ")
key = input("Which key you want to upadte: ")
update = input("Enter upadtes: ")

with open("data/errorCache.json") as file:
    readData = file.read()
    errorsDict = json.loads(readData)
    for error in errorsDict[language]:
        if error['errorName'] == errorName:
            error[key] = update
    with open("data/errorCache.json", 'w') as updateFile:
        rawText = json.dumps(errorsDict,indent=4, sort_keys=True)
        updateFile.write(rawText)
        updateFile.close()
