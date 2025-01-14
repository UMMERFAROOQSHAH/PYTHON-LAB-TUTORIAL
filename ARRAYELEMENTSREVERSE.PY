array= [10, 20, 30, 40, 50]
reversed_array= []
for i in range(len(array) - 1, -1, -1):
    reversed_array.append(array[i])
print("Reversed array:", reversed_array)
