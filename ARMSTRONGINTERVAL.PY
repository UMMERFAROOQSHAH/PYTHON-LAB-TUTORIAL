start=int(input("Enter start range: "))    
end=int(input("Enter end range: "))    
for num in range(start,end+ 1):    
   sum = 0    
   temp = num    
   while temp > 0:    
       digit = temp % 10    
       sum += digit ** 3    
       temp //= 10    
       if num == sum:    
            print(num)    