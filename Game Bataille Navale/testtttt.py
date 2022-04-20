class ClassA(object):
    # var1 = 0
    # var2 = 0
    def __init__(self):
        ClassA.var1 = 1
        ClassA.var2 = 2
    
    def test(self):
        print(ClassA.var1+10)





class ClassB(ClassA):
    def __init__(self):
        print (ClassA.var1)
        print (ClassA.var2)

object1 = ClassA()
object2 = ClassB()

object1.test()