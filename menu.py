valido=True
students=[]
while (valido):
  print("\n******Menú********")
  print("1. Crear un alumno")
  print("2. Modificar un alumno")
  print("3. Consultar todos los alumnos")
  print("4. Eliminar alumno")
  print("5. Salir")
  option=int(input("\neliga una opción valida del menú: "))
  if (option>=1 and option <=5):
    if (option==1):
      name=input("Digite un nombre: ")
      age=input("ingrese la edad: ")
      students.append({"nombre": name, "edad": age})
    if (option==3):
      for student in students:
        print(student)
    if (option==5):
      print("\nFue un placer PERRITO, no vemos .l.")
      valido=False
  else:
    print("No sea bruto")