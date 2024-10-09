def main():
    firstNum = input("First number: ")
    if firstNum == "quit":
        return 
    else:
        firstNum = int(firstNum)

    secondNum = int(input("Second number: "))
    operator = input("Operator (+, -, *, /, ^, %): ")

    match operator:
        case "+":
            print(firstNum + secondNum)
        case "-":
            print(firstNum - secondNum)
        case "*":
            print(firstNum * secondNum)
        case "/":
            if firstNum == 0 or secondNum == 0:
                main()
            else:
                print(firstNum / secondNum)

        case "^":
            print(pow(firstNum, secondNum))
        case "%":
            print(firstNum % secondNum)
        case _:
            print("Invalid operation")
    
    main()

main()