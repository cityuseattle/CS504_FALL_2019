import docx


def readDoc(filename):
    doc = docx.Document(filename)
    fullText = []
    # read all the paragraphs
    for para in doc.paragraphs:
        #add each para to list
        fullText.append(para.text)
    return '\n'.join(fullText)

print(readDoc('test.docx'))