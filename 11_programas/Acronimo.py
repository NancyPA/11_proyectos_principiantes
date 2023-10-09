print("---¿Cual es mi acrónimo?---")
frase = input("Ingresa el significado completo de una organización o concepto: ")

palabras = frase.split()
nueva_cadena = ""
for p in palabras:
    nueva_cadena = nueva_cadena + p[0]

print("Tu acrónimo es: "+ nueva_cadena)
