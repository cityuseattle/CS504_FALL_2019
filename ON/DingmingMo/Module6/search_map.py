import webbrowser
import sys

place = ''
if len(sys.argv) > 1:
    place =' '.join(sys.argv[1:])
webbrowser.open('http://google.com/maps/search/'+ place)