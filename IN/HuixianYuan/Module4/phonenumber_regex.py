import re

def findnumber(text):
    regEx=re.compile(r'([0-9]{3})(\s|-|\.)([0-9]{3})(\s|-|\.)([0-9]{4})')
    for match in re.finditer(regEx, text):
        print(match.group())

def find_Urls(text1):
    pattern=re.finditer(r'http[s]?://[a-zA-Z]+\.[a-z]+', text1)
    for i in pattern:
        print('Urls: ', i)

if __name__ =="__main__":
    message='call me at 206 555 5555 or 206.123.4567 tomorrow. 206-999-6789 is my office.'
    print('phone number found: ')
    findnumber(message)

    text='''<p>Contents :</p><a href='https://google.com'>Python Examples</a>
    <a href='http://github.com'>Even More Examples</a> '''
    print('\nUrls found: ')
    find_Urls(text)
