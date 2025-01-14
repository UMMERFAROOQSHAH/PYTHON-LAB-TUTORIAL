array = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input("Enter element"))
    array.append(element)
smallest =array[0]         #assuming 1st element is smallest
for num in array:
    if num < smallest:   #num represents the current element in each iteration(18,11,2) and compares this num with smallest
        smallest = num
print("The smallest element in the array is:",smallest)
#USING MIN FUNCTION:
arr = [18,11,2,3,6,9,10]
print("The smallest element in the array is:",min(arr))