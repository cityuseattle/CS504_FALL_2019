import docx

def readDoc(filename):
    doc=docx.Document(filename)
    fullText=[]
    #read all paragraphs
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(readDoc('test.docx'))
