# Object Oriented Programming
# Class and Object
#Create class and object
class emptyclass: #Example 1
    &quot;&quot;&quot;This is an empty class&quot;&quot;&quot;
    pass

class numberclass:#Example 2
    num=5  
n1=numberclass()
print(&quot;The number in the class is &quot;,n1.num)
class withfunction:# Example 3 uses constructor
    num=200
    def lab(self):
        print(&quot;This is lab session&quot;)
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
withobject=withfunction(500,1000)
print(withobject.num)
withobject.num=2000 #modify the object property
print(withobject.num)
del withobject.num
print(withobject.num)
withobject.lab()
print(withobject.num1)

print(withobject.num2)
#Inheritance
#Single inheritance
class Parent:
     def parentfunc(self):
          print(&quot;This is parent function&quot;)
class Child(Parent):
     def childfunc(self):
          print(&quot; This is child function &quot;)
ch = Child()
ch.parentfunc()
ch.childfunc()
#Multiple Inheritance
class Parent1:
   def parentfunc1(self):
        print(&quot;This function belongs to parent1&quot;)
class Parent2:
   def parentfunct2(self):
        print(&quot;This function belongs to parent 2&quot;)
class Child1(Parent1,Parent2):
    def childfunc(self):
        print(&quot;This function belongs to child&quot;)
 
ch1=Child1()
ch1.parentfunc1()
ch1.parentfunct2()
ch1.childfunc()
class Parent: # Example of Multilevel Inheritance
      def parentfunct(self):
        print(&quot;This function belongs to parent &quot;)
class Child1(Parent):
      def childfunc1(self):
          print(&quot;This function belongs to child 1&quot;)
class Child2(Child1):
      def childfunc2(self):
        print(&quot;This function belongs to child 2&quot;)
child2ob = Child2()
child2ob.parentfunct()
child2ob.childfunc1()
child2ob.childfunc2()
class Parent: # Example of Hierarchical
      def parentfunc(self):

          print(&quot;This function belongs to parent&quot;)
class Child1(Parent):
      def childfunc1(self):
          print(&quot;This function belongs to child 1&quot;)
class Child2(Parent):
      def childfunc2(self):
          print(&quot;This function belongs to child 2&quot;)
 
child1ob = Child1()
child1ob.parentfunc()
child1ob.childfunc1()
child2ob=Child2()
child2ob.parentfunc()
child2ob.childfunc2()
class Parent: #Example of super function
    def __init__(self,text):
        print(text,&quot;Parent class constructor&quot;)
class Child(Parent):
    def __init__(self):
        print(&quot;This is child class constructor&quot;)
        super().__init__(&quot;Good Evening!!!&quot;)
 
childob = Child()