def calcul(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2 if num2 != 0 else "Division par zéro impossible"
    else:
        result = "Opérateur non valide"
    print(f"{num1} {operator} {num2} = {result}")

calcul(50, '+', 50)
