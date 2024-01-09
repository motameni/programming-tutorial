class NumberHolder:

    def __init__(self, number):
        self.number = number

    def return_number(self):
        return self.number


var = NumberHolder(7)
print(var.return_number())  # Prints '7'
