menu='\n1.Protta\n2.Biriyani\n3.Mandhi\n4.Beef Roast\n5.Alfam\n'
userInput=input("Pls enter what dish you want"+"\n"+menu)

if "Protta" in userInput:
    print("You selected " +userInput)

elif "Biriyani" in userInput:
    print("You selected "+userInput)
    
elif "Mandhi" in userInput:
    print("You selected "+userInput)
    
elif "Beef Roast" in userInput:
    print("You selected "+userInput)
    
elif "Alfam" in userInput:
    print("You selected "+userInput)

else:
    print("\nSorry this dish is not available on this Aamil 's Hotel")
    input("Any else sir : ")