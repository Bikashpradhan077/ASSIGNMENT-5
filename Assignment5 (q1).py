class point:

    def __init__(self,x=1,y=3,z=5):
        self.x = x
        self.y = y
        self.z = z

    def sqsum(self):
        return self.x**2+self.y**2+self.z**2

q=point()   
print(q.sqsum())