

op = input("escoja un operador: + - / *:  ")

num_1 = (int(input("Ingrese un numero: ")))

num_2 = (int(input("Ingrese un numero: ")))

if op == "+":
    print("Resultado: ", num_1 + num_2)
elif op == "-":
    print("Resultado: ", num_1 - num_2)
elif op == "/":
    print("Resultado: ", num_1 / num_2)
elif op == "*":
    if num_2 !=0:
        print("Resultado: ", num_1 * num_2)
else:
    print("por favor ingrese un operador.")
