while True:
    try:
        input_ = (input("Enter:\t"))
        #or
        _input = (input("Enter:\t"))
    except EOFError:
        break
    print (type(input_))
    print (type(_input))
    print (input_)
    print (_input)