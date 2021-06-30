import math
sign = input('What Do You Want Me To Do ? \n"+" for Addition \n"-" for Subtarction\n"*" for Multiplication \n"/" for Division \n"E" to Evaluate \n"sqrt" to Find Square Root \n\n    "?" for Help and operators to use in EVALUATE\n ')

if (sign == "?") :
    help_file = open("helpText.txt", "r")
    helpContent = help_file.read()
    help_file.close()
    print(helpContent)

# To Add

if sign == "+" :

    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    sum = float(first_number) + float(second_number)
    print("Sum = " + str(sum))

# To subtract

if sign == "-" : 
    
    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    sum = float(first_number) - float(second_number)
    print("Sum = " + str(sum))

# To multiply

if sign == "*" : 

    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    sum = float(first_number) * float(second_number)
    print("Sum = " + str(sum))

# To Divide

if sign == "/" :

    first_number = input("First Number =  " )
    second_number = input("Second Number =  ")
    sum = float(first_number) / float(second_number)
    print("Sum = " + str(sum))

# To evaluate

if (sign == "E") :

    print("Give your expression")
    expre = input("")
    print(eval(expre))

#to find square root

if sign == 'Sqrt':
     number = input("Of What Number Should I find Square Root Of? ")
     print(math.sqrt(int(number)))
