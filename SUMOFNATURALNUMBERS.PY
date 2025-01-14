limit=int(input("enter limit upto which you want to add: "))
count=0
#USING FOR LOOP:
for i in range(0,limit+1):
    count+=i
print("sum of first",limit,"natural numbers is:",count)
#USING WHILE LOOP:
i=1
while i<=limit:
    count+=i
    i+=1
print("sum of first",limit,"natural numbers is:",count)