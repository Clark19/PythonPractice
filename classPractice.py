class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "Person(name={},age={})".format(self.name, self.age)


class Student(Person):
  def __init__(self, name, age, school, st_id, major):
    Person.__init__(self, name, age)
    self.school = school
    self.st_id = st_id
    self.major = major

  def __str__(self):
    return f'Student({self.name},{self.age},{self.school},{self.st_id},{self.major})'


s = Student('a',11, 'scf1', 'st-12356777777',   'CS')
print(s)
