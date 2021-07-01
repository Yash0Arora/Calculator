import math
sign = input('What Do You Want Me To Do ? \n"+" for Addition \n"-" for Subtarction\n"*" for Multiplication \n"/" for Division \n"sqrt" to Find Square Root  \n"E" to Evaluate \n\n    "?" for Help and operators to use in EVALUATE\n ')

if (sign == "?") :
    help_file = open("helpText.txt", "r")
    helpContent = help_file.read()
    help_file.close()
    print(helpContent)

# To Add

elif (sign == "+") :

    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    sum = float(first_number) + float(second_number)
    print("Sum = " + str(sum))

# To subtract

elif (sign == "-") : 
    
    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    diffrence = float(first_number) - float(second_number)
    print("Difference = " + str(diffrence))

# To multiply

elif (sign == "*") : 

    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    product = float(first_number) * float(second_number)
    print("Product = " + str(product))

# To Divide

elif (sign == "/") :

    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    quotient = float(first_number) / float(second_number)
    print("Answer = " + str(quotient))

# To evaluate

elif (sign.upper() == "E") :

    print("Give your expression")
    expre = input("")
    print(eval(expre))

#to find square root

elif (sign.upper() == 'SQRT'):
     number = input("Of What Number Should I find Square Root Of? ")
     print(math.sqrt(int(number)))

# if nothing is typed

else:
    print("Sorry, we coud'nt help you")