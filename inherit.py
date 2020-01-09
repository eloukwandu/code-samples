class Parents():

    def print_last_name(self):
        print("Ukwandu")

class Child(Parents):

    def print_first_name(self):
        print("Elochukwu")


elo = Child()

#elo.print_last_name()
#elo.print_first_name()
s = (str(str(elo.print_first_name()) + str(elo.print_last_name())))
