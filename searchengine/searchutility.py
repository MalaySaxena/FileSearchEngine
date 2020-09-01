import re

def checkAND(Strings, pdf_text):
    flag = True

    for word in Strings:
        if re.search(word, pdf_text) is None:
            flag = False
            break

    return flag

def checkOR(Strings, pdf_text):
    flag = False

    for word in Strings:
        if re.search(word, pdf_text):
            flag = True
            break

    return flag