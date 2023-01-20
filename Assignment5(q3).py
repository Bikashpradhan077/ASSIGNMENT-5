class Student:
    def __init__(self,name=None,roll_num=None):
        self__Name =name
        self.__Roll_Num = roll_num
        
    def set_name(self,x):
            self.__Name = x
    def get_name(self):
                print("Name : ",self.__Name,end="")
                return ""
    def get_rollno(self):
                    print("Roll Num. : ",self.__Roll_Num)
                    return ""
    def set_rollno(self,x):
                        self.__Roll_Num = x

x = Student()
x.set_name("bikash Pradhan")
x.set_rollno("DS291122A")
print(x.get_name())
print(x.get_rollno())