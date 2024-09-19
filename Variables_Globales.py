e = "Fantasitic"

def myfunc():
    print("He is " + e)

myfunc()

x = "Increible"

def mensaje():
    print("Eres " + x)

mensaje()

print("Eres " + x)

#The global Keyword
def local():
    global f
    f = "Mejor"

local()

print("Eres el " + f)

i = "Lucas"

def nombre():
    global i
    i = "Alejo"

nombre()

print(i)