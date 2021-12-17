import random
def generate():
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    print("program  generates number1:",num1," number2 :",num2)
    result =num1+(num2/2)
    print("the result is : ",format(result,".2f"))
generate()
while True:
    choice=input("do you want to generate another number? (y/n) ")
    if choice=='y':
        generate()
    elif choice=='n':
        break
print("The program is terminated.. Thank you")
