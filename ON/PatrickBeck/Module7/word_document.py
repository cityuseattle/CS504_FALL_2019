import docx


def readDoc(filename):
    doc = docx.Document(filename)
    fullText = []
    # read all paragraphs
    for para in doc.paragraphs:
        # add each paragraph to the list, fullText
        fullText.append(para.text)
    # get text with newline from the list with join()
    return '\n'.join(fullText)


print(readDoc('test.docx'))