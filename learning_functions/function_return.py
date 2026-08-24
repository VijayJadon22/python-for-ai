

def calculate_sum(a,b):
    return a+b

sum=calculate_sum(a=5,b=4)
print(sum)


def calculate_area(length,width):
    area=length*width
    return area

area=calculate_area(length=10,width=30)
print(area)


def double(num):
    return num*2

total=double(10) + double(3)
print(total)

if double(3)>15:
    print("Yes")
else:
    print("No")


#returning multiple values

def simple_function():
    numbers=[1, 3, 4, 2, 5]
    first_number=numbers[0]
    last_number=numbers[-1]
    return first_number,last_number

num1 , num2 = simple_function()
print(num1,num2)
