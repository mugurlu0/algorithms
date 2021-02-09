
def in_array(x, y):
    exist = False
    for i in (y):
        if x in y[0:]:
            exist = True
    print(exist)


in_array(5, [1, 2, 3])
