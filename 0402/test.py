def msg():
    print("hello world")
    print("welcome to python world")
    print("THis is a test message")


def emp():
    pass
def msg2(rep):
    for i in range(rep):
        print("this is a repeated message")

def getArea(radius):
    area = 3.14 * radius * radius
    return area
        
emp()
msg()
msg2(3)
area = getArea(5)
print("this of the circle with radius 5 is", area)