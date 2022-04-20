class ClassA():

    def __init__(self):
        self.var1 = 1
        self.var2 = 2
    
    def test(self):
        print(self.var1+10)
    
    





class ClassB(ClassA):
    def __init__(self, classA):
        print (classA.var1)
        print (classA.var2)

object1 = ClassA()
object2 = ClassB(object1)

object1.test()