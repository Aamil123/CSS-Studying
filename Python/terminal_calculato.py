number1=int(input("Enter 2 numbers : "))
number2=int(input())
a= input("\n+,\n-,\n*,\n/,\n select from these operations you want : ")

if '+' in a:
    sum=number1+number2
    print("The sum = "+str(sum))
    
elif '-' in a:
    diffrence=number1-number2
    print("The Diffrence = "+str(diffrence))

elif '*' in a:
    multiplication=number1*number2
    print("The Multiplication = "+str(multiplication))
    
elif '/' in a:
    division=number1/number2
    print("The Division = "+str(division))
    
else:
    input("\nSorry this operation cannot be use in my terminal calculator \nAny other help you want sir :   ")
print("\nTankyou for using my terminal calculator (-_-)\n")


