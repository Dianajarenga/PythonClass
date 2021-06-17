class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
        
        
    def area(self):  
        A=(self.width*self.length)
        return f"area is {A}"
    def perimeter(self):
        P=(self.length*2+self.width*2) 
        return f"the perimeter is {P}"
rect=Rectangle(width=20,length=40) 
print(rect.area())
print(rect.perimeter())

def smallest():
    s=[3,6,8,2,4,1,5,7]
    print(min(s))
smallest()
x = ['a','b','a','e','d','b','c','e','f','g','h']
y=set(x)
print(y)
print(list(y))
    
def divisible_by_seven():
    c=[]
    for i in range(100,200):
        if i%7==0:
            c.append(i)
            print(c)

divisible_by_seven()
def greet(students):
    student=[]
    for student in students:
                print(f" hello {student['name']} you were born in {2021-student['age'] } ")
greet(students = [{"age": 19, "name": "Eunice"},
                {"age": 21, "name": "Agnes"}, 
                {"age": 18, "name": "Teresa"},
                {"age": 22, "name": "Asha"}]
              )
def divisible_by_three(n):
    n=range(n+1)
    i=1
    for i in n:
       if i%3==0:
           print(i) 
divisible_by_three(30)