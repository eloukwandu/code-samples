import random

def fwread(*args):
    name = random.randrange(1, 200)
    full_name = str(name) + ".txt"
    fw = open(full_name, 'w')
    fw.write('Beautiful in all ramifications\n')
    fw.write('I love her earnestly\n')
    fw.close()

    fr = open(full_name, 'r')
    delectable = fr.read()
    print(delectable)
    fr.close()


