a=int(input("Enter number for multiplication table : "))
b=int(input("\nWhich number does the multiplication table ends : "))

print("\n The multiplication table of ",str(a),"\n")

for i in range(1,b):
    print(a,'x',i,'=',a*i)
else:
    print("sorry this is not working")