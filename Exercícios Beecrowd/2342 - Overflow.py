limite = int(input().strip())
num1, operador, num2 = input().split()

resultado = 0

if operador == "+":
    resultado = int(num1) + int(num2)
elif operador == "*":
    resultado = int(num1) * int(num2)

if resultado <= limite:
    print("OK")
else:
    print("OVERFLOW")
