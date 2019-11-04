import docx

def readDoc(filename):
    doc = docx.Document(filename)
    fullText = []

    for para in doc.paragraphs:
        # add each paragraph to the list, fullText
        fullText.append(para.text)

    return '\n'.join(fullText)

print(readDoc('test.docx'))        