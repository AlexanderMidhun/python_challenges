# Create a new list from existing list (Use String Format)
def new_list():
    my_list = [10, 20, 30, 40, 50]
    new_list = ["Number: {}".format(item) for item in my_list]
    print(new_list)

# Create a List with 8 elements and Print second index to sixth index
def another_list():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80]
    print(my_list[2:7])

# Create a tuple with 7 elements
#   1. Use Insert, Append.
#   2. Print the last second element.
def tuples():
    my_tuple = (10, 20, 30, 40, 50, 60, 70)
    my_list = list(my_tuple)
    my_list.insert(2, 25)
    print(my_list)
    my_list.append(80)
    print(my_list)
    my_tuple = tuple(my_list)
    print(my_tuple)
    print("The last second element :", my_tuple[-2])

def result():
    print('__________________________________________________')
    new_list()
    print('__________________________________________________')
    another_list()
    print('__________________________________________________')
    tuples()

result()