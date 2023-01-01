class Parent:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def shit(self):
        print("Ey there, ma name is", self.name, "and I am", self.age, "yrs old\nI'm in the", self.grade, "grade\n")


p = Parent("Patrick", 13, "12th")
p.shit()


class Child(Parent):
    def __init__(self, name, age, grade, year):
        self.name = name
        self.age = age
        self.grade = grade
        Parent.__init__(self, name, age, grade)
        self.graduation_year = year

    def shitty(self):
        print("Hello there, ma name is", self.name, "I am", self.age, "years old")
        print("I joined Shalom Science and Technology Academy in the year", self.graduation_year)
        print("I'm in the", self.grade, "grade")


q = Child("Henry", 11, "8th", 2019)
q.shitty()

class Iterate:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 1000:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


whoa = Iterate()
iter = iter(whoa)

for x in iter:
    print(x)