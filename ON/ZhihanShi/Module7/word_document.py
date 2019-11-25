import docx

def readDoc(filename):
    doc = docx.Document(filename)
    fullTest =[]
    for para in doc.paragraphs:
        fullTest.append(para.text)
    return '\n'.join(fullTest)
print(readDoc('test.docx'))
