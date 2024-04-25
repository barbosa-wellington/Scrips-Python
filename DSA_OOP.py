class Book:

    def __init__(self):

        # Define attributes
        self.title = "Programming in C++"
        self.isbn = 89897565

    def printT(self):
        print("The book %s has been created with the ISBN code %d" %(self.title, self.isbn))

book1 = Book()

# book1.title = "Horrible Science"
# book1.isbn = 76767868723

print(book1.title)
book1.printT()

class Students:

    def __init__(self,name, age, grate):
        self.name = name
        self.age = age
        self.grate = grate


student1 = Students('Wellington', 29, 7.9)

print(student1.name)
print(student1.age)
print(student1.grate)


class Employees():

    def __init__(self, name, salary, title,transid='T0'):
        self.name = name
        self.salary = salary
        self.title = title
        self.transid = transid
    def listFunc(self):
        print("Employee " + self.name + " has a salary of $"+ str(self.salary) + " and oculpation is " + self.title)

    def transaction(self):
        newid=int(self.transid[1:])
        newid = newid + 1
        self.transid = 'T'+str(newid)


employee1 = Employees("Wellington", 56000, "Soul Chef")
employee1.listFunc()
print(employee1.transaction())


employee2 = Employees("Charles", 30000, "Waiter")
employee2.listFunc()
print(employee2.transaction())

employee3 = Employees("William", 70000, "Head Chef")
employee3.listFunc()
print(employee3.transaction())

employee4 = Employees("Leadron", 56000, "Soul Chef")
employee4.listFunc()
print(employee4.transaction())


