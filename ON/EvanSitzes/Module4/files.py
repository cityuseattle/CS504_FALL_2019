file = open('hello.txt', 'a')
file.write('\nThis is the new content for the file')
file.close()

new_file = open('world.txt', 'w')
new_file.write('This is a new file')
new_file.close()


file = open('hello.txt')
content = file.read()
file.close()
print(content)