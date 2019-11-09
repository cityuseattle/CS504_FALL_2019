file = open('hello.txt', 'a')
file.write('\nThis is contract I just appended')
file.close()

new_file = open('world.txt', 'w')
new_file.write('This is new file')
new_file.close()

file = open('hello.txt')
content = file.read()
file.close()
print(content)