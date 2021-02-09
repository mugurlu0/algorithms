# Write a function which returns an array of n random numbers, n being the only received parameter.
def randArray():
    from random import randint

    x = []
    y = randint(1, 10)
    print(y)
    while len(x) != y:
        x.append(randint(1, 10))
    print(x)


randArray()


# II - translate
# The main goal of pseudo code is to write down the logic behind an algorithm, so that you can easily translate it into human speech or code.

# Given the algorithm below
# with your word explain its purpose

# translate it into Python and Javascript

# function in_array(element, list_elements) {
#     boolean exist = false
#     for (I=0
#          until length($list_elements)) do {
#         if ($element == $list_elements[I]){$exist = true
#                                            }
#     }
#     return $exist
# }

# Python
def in_array(x, y):
    exist = False
    for i in (y):
        if x in y[0:]:
            exist = True
    return exist


# example
in_array(5, [1, 2, 3])

# javascript
function in_array(element, list_elements) {
    var exist = false
    for (var i=0
         i < list_elements.length
         i++) {
        if (element == list_elements[i]) {
            exist = true
        }
    }
    return exist
}
# example
in_array(5, [1, 2, 3])


# This function attempts to check whether a given number exists inside an array.
# It takes two arguments: the element to be checked and the list in which to check.
# It starts checking at index(0) until the last element of the list.
# If there is a correspondence between the first argument and an element inside the list at some index,
# the boolean false value becomes true for the exist variable. Exist is then returned.

# III - sort an array
# Write a function which receives an array of ten random integers as parameter and returns an ascendantly ordered array of integers.


def SortedrandArray():
    from random import randint
    x = []
    while len(x) != 10:
        x.append(randint(1, 10))
    print(sorted(x, reverse=False))


SortedrandArray()
