#Question_1
def isScalene(x, y, z):
    if x == y == z:
        print("False")
    elif ((x != y) and (x != z) and (y != z)):
        print("True")
    else:
        print("False")
isScalene(12, 19, 15)

#Question_2
list=[]
user_variable=input("Type in a number ranging from 1 to 100.")

def generateNumbers(start, end):
    for i in (range(1, end)):
        list.append(i)
generateNumbers(1, (int(user_variable)))
print(list)

#Question_3_A
def getBiggerNumber(x, y):
    if x > y:
        return x
    else:
        return y
print("Enter the first number.")
a = input()
print("Enter the second number.")
b = input()
print(str(max(a, b)) + "is larger.")

#Question_3_B
n=int(input("Enter size of list"))
my_list=[]

for i in range(0, n):
    num=input("Enter elements")
    my_list.append(num)
lgt=max(my_list)
print("largest number is",lgt)
