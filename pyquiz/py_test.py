def listcomp():
    x = [100,110,120,130,140,150]
    for i in x :
        i*=5
        return i
listcomp()   


#def divisible_by_three(n):
  #  for a in n:
    #    if a%3==0:
          #  print(a)
#print(divisible_by_three(33))


def nested_list():
    x = [[1,2],[3,4],[5,6]]
    flat=[]  
    for list in x:
        for i in list:
            flat.append(i)
print(nested_list())



def smallest():
    s=[3,6,8,2,4,1,5,7]
    print(min(s))
smallest()


x = ['a','b','a','e','d','b','c','e','f','g','h']
y=set(x)
print(y)
print(list(y))
    


def divisible_by_seven():
    for i in range(100,200):
        if i%7==0:
            return list(i)

print(divisible_by_seven())

def greet():
    students = [{"age": 19, "name": "Eunice"},
                {"age": 21, "name": "Agnes"}, 
                {"age": 18, "name": "Teresa"},
                {"age": 22, "name": "Asha"}]
              
    for student in students:
        for i in student:
            if i==student[0] & i==student[1]:
                return f" hello {student[1]} you are {2021-student[0] } years old"
greet()
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

