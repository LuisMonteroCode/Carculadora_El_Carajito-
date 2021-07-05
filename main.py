#Universidad Tecnica Antonio Jose de Sucre, Sede: Ciudad Bolivar - Luis Montero - 28.694.084

#-CARCULADORA CHIDA-#
# --VARIABLES--
simbolos = {"sumar": '+', "restar": '-', "multiplicar": '*', "dividir": '/'}
reintertarElPrograma = 1

# --OPERACIONES GENERALES--
# --MENU OPERACIONES--
print("Bienvenido(@) a la super carculadora: \"eL CARAJITO\" \n*Carculamos lo carculabre*\n")
print("Estas son las operaciones disponibles a realizar: \n--------------")

for j in simbolos:
	print(j, " -> " + simbolos[j])

print("--------------")

# --CONDICIONES Y CARCULOS--
# --ESTARA ACTIVA HASTA QUE EL USUARIO DECIDA--

while (reintertarElPrograma == 1):

	# PIDIENDO EL TIPO DE CARCULO A REALIZAR
	simbolo_dato = input("Ingrese el tipo de operacion a realizar: ")

	# --SUMA--
	if simbolo_dato.lower() == "sumar" or simbolo_dato.lower() == '+':
		print ("\n-- Operacion -> 'SUMA' --\n")

		print ("-----------------------------------------")
		
		num1 = int(input("ingrese un numero: "))
		num2 = int(input("ingrese otro numero: "))
		
		resultado = num1 + num2

		# --COMPROVANDO SI EL DATO ES EL SIMBOLO DEL CALCULO--
		if (simbolo_dato.lower() == '+'):
			print (f"\nLa operacion fue: {num1} + {num2}")
		else:
			print (f"\nLa operacion fue: {num1} {simbolos[simbolo_dato.lower()]} {num2}")

		print(f"El resultado es: {resultado}")

		print ("-----------------------------------------")

	# --RESTAR--
	elif simbolo_dato.lower() == "restar" or simbolo_dato.lower() == '-':
		print ("\n-- Operacion -> 'RESTA' --\n")

		print ("-----------------------------------------")
		
		num1 = int(input("ingrese un numero: "))
		num2 = int(input("ingrese otro numero: "))
		
		resultado = num1 - num2

		# --COMPROVANDO SI EL DATO ES EL SIMBOLO DEL CALCULO--
		if (simbolo_dato.lower() == '-'):
			print (f"\nLa operacion fue: {num1} - {num2}")
		else:
			print (f"\nLa operacion fue: {num1} {simbolos[simbolo_dato.lower()]} {num2}")

		print(f"El resultado es: {resultado}")

		print ("-----------------------------------------")

	# --MUTIPLICACION--
	elif simbolo_dato.lower() == "multiplicar" or simbolo_dato.lower() == '*':
		print ("\n-- Operacion -> 'MULTIPLICACION' --\n")

		print ("-----------------------------------------")
		
		num1 = int(input("ingrese un numero: "))
		num2 = int(input("ingrese otro numero: "))
		
		resultado = num1 * num2

		# --COMPROVANDO SI EL DATO ES EL SIMBOLO DEL CALCULO--
		if (simbolo_dato.lower() == '*'):
			print (f"\nLa operacion fue: {num1} * {num2}")
		else:
			print (f"\nLa operacion fue: {num1} {simbolos[simbolo_dato.lower()]} {num2}")

		print(f"El resultado es: {resultado}")

		print ("-----------------------------------------")

	# --DIVISION--
	elif simbolo_dato.lower() == "dividir" or simbolo_dato.lower() == '/':
		print ("\n-- Operacion -> 'DIVICION' --\n")

		print ("-----------------------------------------")
		
		num1 = int(input("ingrese un numero: "))
		num2 = int(input("ingrese otro numero: "))
		
		resultado = num1 / num2

		# --COMPROVANDO SI EL DATO ES EL SIMBOLO DEL CALCULO--
		if (simbolo_dato.lower() == '/'):
			print (f"\nLa operacion fue: {num1} / {num2}")
		else:
			print (f"\nLa operacion fue: {num1} {simbolos[simbolo_dato.lower()]} {num2}")

		print(f"El resultado es: {resultado}")

		print ("-----------------------------------------")

	else: 
		print ("----------------!!ERROR!!----------------")
		print ("ERROR 404 - DATO INGRESADO NO ES UNA OPERACION ARITMETICA O ES ERRONEO :(\n")
		reintertarElPrograma = 0;

	
	reintertarElPrograma = int(input("Desea reintentar?\n(1)Si\n(2)No\n"))

	if (reintertarElPrograma == 1):
		print ("-----------------------------------------")

	elif (reintertarElPrograma == 2):
		break

	else:
		print ("----------------!!ERROR!!----------------")
		print ("ERROR 414 - DATO DE SELECION NO ESTA REGISTRANDO :(")
		reintertarElPrograma = 0;

# --CONCLUYENDO EL PROGRAMA--
print("\n-----Finalizando el programa-----")