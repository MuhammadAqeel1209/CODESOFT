def AddElementInList():
    my_list = []
    size = int(input(f"\nHome many Digit you want to {operators}\t"))
    for i in range(size):
        i = int(input(f"\nEnter the number for operations\t"))
        my_list.append(i)
    return my_list

while True:
    operators = input("\n\nEnter the operators\nFor Mutiply *\nFor Divide /\nFor Addition +\nFor Subtraction -\nFor Modulus %\nFor exit !\t")
    if(operators == '*'):
        save = []
        result = 1
        my_data = AddElementInList()
        for i in my_data:
            result  *= i
        print(f"Multiplication is\t{result}")    

    elif(operators == '-'):
        save = []
        my_data = AddElementInList()
        result = 0
        for i in my_data:
            result  = my_data[0] - sum(my_data[1:])
        print(f"Subtration is\t{result}") 

    elif(operators == '+'):
        save = []
        result = 0
        my_data = AddElementInList()
        for i in my_data:
            result  = sum(my_data)
        print(f"Addition is\t{result}") 

    elif(operators == '/'):
        save = []
        my_data = AddElementInList()
        result = my_data[0]
        for i in my_data[1:]:
            result  /= i
        print(f"Division is\t{result}") 

    elif(operators == '%'):
        save = []
        my_data = AddElementInList()
        result = my_data[0]
        for i in my_data[1:]:
            result  %= i
        print(f"Modulus is\t{result}") 

    elif(operators == "!"):
        print("Thanks For using My Calculators")
        break           

    else:
        print("Wrong Inputs!!\nPlz Select Correct option from memu!!\n")