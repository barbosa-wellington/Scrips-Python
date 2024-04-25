
# Trying to implmenting a python algorithm
# Bubble sort

# list1 = [6, 3, 12, 7,4,8,9,10,12,16,56,39,43,29,82]
#
#
# def bubble_sort(arr):
#
#     n = len(arr)
#
#     for i in range(n):
#         print("I: ", i)
#
#         for j in range(0, n-i-1):
#             print("J: ", j)
#
#             if arr[j] > arr[j+1]:
#
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# print(bubble_sort(list1))



list_music = []

print(type(list_music))

print(type("I love Jj"))


print(round(3.14151922,5))



sentence = "I want to achieve the highest degree."

print(sentence[::-1])


letter = 'w'

print(letter * 3)
print(sentence.split('a'))

print("\n")

print("--------Dictionary----------\n")

python_student = {"Wellington":75 ,"William":70,"Charles": 75}

print(python_student)


print(python_student['Wellington'])
print(python_student.values())
print(python_student.items())
print(python_student.keys())

python_student["Washington"] = 79

python_student["Names"] = ["Picanha","Feijoada", "Fraudinha"]

#Insert, update data on a dictionary
print(python_student["Names"][0].upper())

# Diong math operation
var1 = python_student["Wellington"] - 2



lista1 = [10, 16, 24, 39, 47]
lista2 = [32, 89, 47, 76, 12]

print(47 in lista1)
#
# for i in [lista1, lista2]:
#     print(i)
#     if i == 47:
#         print(i)



def firstFunc():
    #name = 'Wellington'
    print("Hello Mr.")

def secondFunc(name):
    print("Hello Mr. %s" %(name))

secondFunc('Wellington')

def printNumber():

    for i in range(0, 10):
        print("Number : " + str(i))


printNumber()

#Function to print calculate two numbers
def OperactionFunc(num1, num2):
    print("The first number is :" +str(num1))
    print("The second number is :" + str(num2))
    print("The sum of num1 to num2 is: ", num1 + num2)
#Calling the function
OperactionFunc(10,27)
# by adding * you can define any number of arguments
def printVar(arg1, *vartuple):

    #Print the first value
    print(arg1)

    for i in vartuple:
        print(i)
    return;

printVar('wellington','Kamochanok','Kassandra')


powerN =  lambda num: num ** 2

print(powerN(5))

# List comprehension
#[expression for item in iterable if condition == True]

print([x for x in range(10) if x < 5])

fruit_list = ['banana','abacate','melancia','cereja','manga']
print(fruit_list)
new_list = [x for x in fruit_list if 'm' in x]
print(new_list)

# dict comprehension
# {expression for item in iterable if condition == True}

dict_student ={"Wellington":75 ,"William":70,"Charles": 75}

dict_student_status = {k:v for (k, v) in dict_student.items()}
print(dict_student_status)

# code to present if the student pass or fail
dict_student_status = {k: ('Aproval' if v > 70 else 'Fail') for (k, v) in dict_student.items()}
print(dict_student_status)