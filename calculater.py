num1:int = int(input("Enter the first number:"))
num2:int = int(input("Enter the second number:"))
print("press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division")
choice: int = int(input('Enter the number between 1 To 4:')) 
if choice == 1:
   print("The addition of given to num is :",num1+num2)
elif choice == 2:
   print("The subtraction of given to num is :",num1-num2) 
elif choice == 3:
    print("The multiplication of given to num is :",num1*num2)
elif choice == 4:
   print("The division of given to num is :",num1/num2) 
else:
    print('invalid number')  