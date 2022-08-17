def a_bisiesto(Bisiesto):
    if Bisiesto % 4 != 0:
      print("No es un año bisiesto")
    elif Bisiesto % 4 == 0 and Bisiesto % 100 != 0 or Bisiesto % 400 != 0: 
        print("Es un año bisiesto")
    elif Bisiesto % 4 == 0 and Bisiesto % 100 == 0 and Bisiesto % 400 != 0: 
        print("No es un año bisiesto")
    elif Bisiesto % 4 == 0 and Bisiesto % 100 == 0 and Bisiesto % 400 == 0: 
        print("Es un año bisiesto")
Bisiesto = int(input("Ingrese el año: "))  
a_bisiesto(Bisiesto) 