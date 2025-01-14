list=['ummer','farooq','shah']
size=len(list)
string= ""
for i in range(size):
    string+= str(list[i])  #Convert each item->string and add to result.
    if i < len(list) - 1:  # Adds a space b/w elements,but not at the end.
        string+= " "
print(string)
#USING MAP(ADVANCED FUNCTION):
list = ['ummer','farooq','shah']
string= ' '.join(map(str,list))
print(string)