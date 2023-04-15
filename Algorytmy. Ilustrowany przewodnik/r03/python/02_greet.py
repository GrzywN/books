def greet2(name):
    print "Jak siê masz, " + name + "?"

def bye():
    print "Ok, czeœæ!"

def greet(name):
    print "Czeœæ, " + name + "!"
    greet2(name)
    print "Przygotowanie do po¿egnania..."
    bye()

greet("adit")
