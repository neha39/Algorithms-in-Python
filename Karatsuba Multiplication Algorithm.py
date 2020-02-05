def karatsuba_multiplication(num1,num2):
    """
    1. num1 and num2 are two numbers to be multiplied
    2. the function returns the result after multiplication
    """
    if num1<10 or num2<10: #for only single digit multiplication change the 'or' condition to an 'and' condition. 
        return num1*num2
    else:
        n=max(len(str(num1)),len(str(num2)))
        nby2=n//2
        
        a=num1//(10**(nby2))
        b=num1%(10**(nby2))
        c=num2//(10**(nby2))
        d=num2%(10**(nby2))
        
        ac=karatsuba_multiplication(a,c)
        bd=karatsuba_multiplication(b,d)
        ad_bc=karatsuba_multiplication(a+b,c+d)-ac-bd
        
        return ((10**(2*nby2))*ac)+((10**nby2)*ad_bc)+bd
    
""" 
EXAMPLE TO TRY:

num1=3141592653589793238462643383279502884197169399375105820974944592
num2=2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba_multiplication(num1,num2))
"""


