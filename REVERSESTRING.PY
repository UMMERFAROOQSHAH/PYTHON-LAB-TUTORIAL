string=str(input("enter string: "))
length=len(string)
print("original string is: ",string)
reverse_string=string[::-1] #start(begning),stop(go all the way),step(-1->backwards)
print("reversed string is:",reverse_string)
# #USING FOR LOOP:
string="UMMER FAROOQ SHAH"
length=len(string)
reverse_string=""
print("original string is: ",string)
for i in range(length-1,-1,-1):#start(index),end,steps
    reverse_string+=string[i]
print("reversed string is:",reverse_string)