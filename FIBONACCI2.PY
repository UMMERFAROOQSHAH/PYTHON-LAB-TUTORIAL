terms =int(input ("How many terms we want to print: "))  
n1 = 0  
n2 = 1  
count = 0 
if terms<= 0:  
    print ("Please enter valid number of terms")  
elif terms==1:  
    print ("The Fibonacci sequence of the numbers up to",terms," :")  
    print(n1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count<terms:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count+=1 