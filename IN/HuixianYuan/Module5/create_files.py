for i in range(5):
    f=open('text{}.txt'.format(i), 'w')
    f.write('testtesttest')
    f.close()

for i in range(5):
    f=open('text{}.py'.format(i), 'w')
    f.write('testtesttest')
    f.close()