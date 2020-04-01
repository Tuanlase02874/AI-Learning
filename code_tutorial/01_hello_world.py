
def function1(a, b, c):
    return a + b + c


def function2():
    print("Kim Chi")


def speech_recognition(sound):
    signal = sound
    return signal


if __name__ == '__main__':
    print("Hello worlrd")
    # comment code
    d = function1(a=4, b=5, c=6)
    print("Results d= ", d)
    function2()
    if False:
        print("True 1")
        print("True 2")
        print("True 3")
    else:
        print("False 1")
        print("False 2")

    # Variables
    x = 5
    y = "John"
    print(x)
    print(type(x))
    print(y)
    x = "Sally"
    print(x)
    print(type(x))

    x = 'Sally'
    print(x)
    print(type(x))

    #Legal variable names:
    myvar = "John1"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John2"
    myvar2 = "John"
    print(MYVAR)
    print(myvar)

    #Illegal variable names:
    #2_myvar = "John"
    # my-var = "John"
    # my var = "John"