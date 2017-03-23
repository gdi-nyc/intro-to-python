def typeIdentifier(a_list):
    for element in a_list:
        # remember we must convert element and type(element) to strings so we can add them
        # together.
        print str(element) + " is a " + str(type(element))

my_list = [1, 'hello', 12.33, 'data', [1,2]]
typeIdentifier(my_list)
