class box:
    def __init__(self,names):
        self.names=names
class box1:
    def __init__(self,sem):
        self.sem=sem
class objectt(box):
    def __init__(self,rollno,names,sem):
        self.rollno=rollno
        box. __init__(self,names)
        box1. __init__(self,sem)
obj1=objectt(18,"xyz",3)
print("name=",obj1.names)
print("Rollno=",obj1.rollno)
print("sem=",obj1.sem)
