# I - concatenation
# Write a function which receives two strings and returns them as one string.

def concat(a,b):
    print(str(a)+" "+str(b))

concat("Hi, my", "name is Mehmet")


# II - lowercase
# Write a function which receives a character in uppercase and prints it in lowercase.
def uptolow(x):

    print(x.lower())
uptolow("BECODE ROCKS")

# III - uppercase
# Write a function which receives a string in lowercase and returns an uppercase sentence.
def uptolow(x):

    print(x.upper())
uptolow("becode rocks")
# IV - convert name
# Write a function which receives a name in this format "Doe, John" an returns it in this format "John Doe"
name="Doe, John"
print(name[5:]+" "+name[0:3])

# V - whitespace
# Write a function which receives a sentence full of whitespace and returns it without them.
def spaceRem(sentence):
    print(sentence.replace(" ",""))
spaceRem("This      is        a         sentence      with       plenty          of        whitespaces")


