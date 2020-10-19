## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		slef.name = name

## ??
class Cat(Animal):
	
	def __init__(slef, name):
		## Cat has-a name
		self.name = name

## ??
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		'''
		super() 函数是用于调用父类(超类)的某个方法。
		
		此处调用了父类Person的__init__方法
		传入name作为参数，完成self.name 和 self.pet的初始化
		从而将父类的属性赋予Employee
		'''
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## slamon is-a Fish
class salmon(Fish):
	pass

## halibut is-a Fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet of Cat
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet of Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## course is-a Salmon
course = Salmon()

## harry is-a Halibut
harry = Halibut()