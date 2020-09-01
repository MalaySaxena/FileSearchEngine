from searchengine import pdfutility, searchutility

def getBestFiles(keys):
    files = []

    for file in pdfutility.filesText:
        if searchutility.checkAND(keys, pdfutility.filesText[file]) is True:
            files.append(file)

    return files

def getAnyFiles(keys):
    files = []

    for file in pdfutility.filesText:
        if searchutility.checkOR(keys, pdfutility.filesText[file]) is True:
            files.append(file)

    return files