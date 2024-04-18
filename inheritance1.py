class box:
    def __init__(self,names):
        self.names=names
class objectt(box):
    def __init__(self,rollno,names):
        self.rollno=rollno
        box. __init__(self,names)
obj1=objectt(18,"xyz")
print("name=",obj1.names)
print("Rollno=",obj1.rollno)
