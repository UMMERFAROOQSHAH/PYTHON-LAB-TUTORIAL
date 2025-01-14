#ELEMENTS FROM USER:
array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)
print("The elements of the array are:", array)
#ELEMENTS GIVEN:-
size = int(input("Enter the size of the array: "))
array=[1,2,3,4,5]
for i in range(size):
    print(array[i])