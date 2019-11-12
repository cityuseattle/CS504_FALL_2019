def function1():
    print('can i skip this task?')
    function2()

def function2():
    raise Exception('it is not a good idea to skip this task.')

function1()