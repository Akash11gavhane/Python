
# python Object - Oriented programming

# why classes are used ?

# code reusabality        
# code maintanibility
# modular programming

# class - Real world Entity or Object

# that object contains diffrent diffrent attributes and methods

# for defining any of the class you have need to use class keyword

class Car :


# here class is keyword name for defining a class and car is a name of class without name your class is not defined

    pass

    # class is blueprint and using that we can make instances or objects

    # car is blueprint we can make multiple copies of it and for making these copies we use instance or objects

car1 = Car()  # thats how we initialise the instance or object

car2 = Car() 

# thats how we make two copies of our class

print(car1)




# class - Real world Entity or Object
# attributes -- properties of the class
# methods -- actions of the class

car1.window=4 # type: ignore
car1.tyres=4 # type: ignore
car1.engine="Diesel"# type: ignore

car2.windows=5 # type: ignore
car2.tyres=6 # type: ignore
car2.engine="petrol" # type: ignore

#print(car1.engine)  # type: ignore
#print(car2.engine)  # type: ignore


## this is the worst way of deiining


## lets define the object in effiecient manner



# print(dir(car1)) # this method is useful for see the directory or how many methods are there in the given object or instance


class Car1 :

    # constructor 
    # 

    def __init__(self , windows , tyres , engine):

        self.windows = windows
        self.tyres = tyres
        self.engine = engine

        # we assign three parameters to self. attributes

        # self is use for any of the attribute present in the class we can directly call it 

    def self_driving(self):
        print("The car type is {}".format(self.engine))

        # like that we can make multiple methods using self and we can pass multiple attributes with self object 
        # self is just naming convention you can give any name at the self

    def self_driving1(self , engine):
        print("The car type is {}".format(engine))

        
car1 = Car1(4 , 4 , "Petrol")
print("the number of tyres is object car1 is :" , car1.tyres)
print("the number of windows is object car1 is :" , car1.windows)
print("the engine of object car1 is :" , car1.engine)



print(car1.self_driving())

print(car1.self_driving1("Electric"))

