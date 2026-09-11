class Employee: #defines the class you want
    def __init__(self, firstName, lastName): #passes class to initialize state
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"{self.firstName} {self.lastName}" #returns a readable string of the defined class
