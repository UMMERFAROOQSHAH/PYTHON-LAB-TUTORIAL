#A number that is equal to the sum of its own digits multiplied by the number of digits it contains  (153=1*1*1+5*5*5+3*3*3=153)is known as an Armstrong number:-
num=int(input("enter number: "))
sum = 0    
temp = num      
while temp>0:
  digit = temp % 10    
  sum += digit ** 3    
  temp //= 10    
if num == sum:    
    print(num,"is armstrong")    
else:
    print(num,"is  not armstrong")   