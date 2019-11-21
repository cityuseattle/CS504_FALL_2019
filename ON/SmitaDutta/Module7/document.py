import docx

def readDoc(fileName):
    doc= docx.Document(fileName)
    fullText= []

    # read all paragraphs
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(readDoc('test.docx'))    


