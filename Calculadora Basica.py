x = input("introduce el primer numero: ")
operacion = input("Introduce la operacion +,  -, * o /: ")
y = input("Introduce el segundo numero: ")

x_int = int(x)
y_int = int(y)

if operacion == "+":
   resultado = x_int + y_int
elif operacion == "-":
    resultado = x_int - y_int
elif operacion == "/":
    resultado = x_int / y_int
else: 
    resultado = x_int * y_int
   
print(f"El resultado de {x_int} {operacion} {y_int} es {resultado}")

# PRUEBA