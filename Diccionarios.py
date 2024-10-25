from itertools import permutations

print(r"""
             __
           <(o )___
             (  ._> )
              `---'   

       ¡Bienvenido a DiccsUp!
Generador de combinaciones para contraseñas.
""")

# Pedimos los datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ")
mascota = input("Ingresa el nombre de tu mascota: ")
ciudad = input("Ingresa tu ciudad de nacimiento: ")

# Dividimos la fecha de nacimiento en día, mes y año
dia, mes, anio = fecha_nacimiento.split("/")

# Creamos una lista con los datos proporcionados
datos = [nombre, apellido, dia, mes, anio, mascota, ciudad]

# Generamos combinaciones posibles de dos, tres y cuatro elementos
combinaciones = []
for i in range(2, len(datos) + 1):
    combinaciones.extend([''.join(combo) for combo in permutations(datos, i)])

# Añadimos variantes comunes y patrones típicos, incluyendo nombre+mascota+anio
variantes = [
    nombre + anio,
    apellido + anio,
    mascota + anio,
    ciudad + anio,
    nombre + dia + mes,
    nombre + mes + anio,
    nombre + mascota,
    mascota + apellido,
    nombre + ciudad,
    nombre[::-1],           # Nombre al revés
    mascota[::-1],           # Mascota al revés
    anio + nombre,
    dia + apellido + mes,
    nombre.capitalize() + "123",           # Capitalizado + 123
    nombre + apellido + "123",
    mascota.capitalize() + "!",
    nombre.capitalize() + anio,
    apellido.capitalize() + anio,
    nombre.capitalize() + mascota.capitalize() + "!",
    ciudad.capitalize() + "2023",
    nombre + "@" + anio,
    mascota + "@" + apellido,
    nombre.capitalize() + anio[-2:],       # Capitalizado y últimos 2 del año
    mascota.capitalize() + anio[-2:],
    dia + mes + anio,                      # Fecha completa sin separadores
    dia + "_" + mes + "_" + anio,          # Fecha con separadores

    # Combinaciones específicas de nombre + mascota + año, mes o día
    nombre + mascota + anio,
    nombre + mascota + dia,
    nombre + mascota + mes,
    nombre.capitalize() + mascota.capitalize() + anio,
    nombre + mascota + anio[-2:],          # Últimos 2 dígitos del año
    nombre + mascota + "123"
]

# Añadimos combinaciones con caracteres especiales y números comunes al final
especiales = ["!", "?", "#", "$", "@", "123", "321", "2024"]
for dato in datos:
    variantes.extend([dato + especial for especial in especiales])
    variantes.extend([dato.capitalize() + especial for especial in especiales])

# Mezclamos mayúsculas y minúsculas en combinaciones de datos comunes
mayus_variantes = []
for v in variantes:
    mayus_variantes.append(v.upper())
    mayus_variantes.append(v.lower())
    mayus_variantes.append(v.capitalize())

# Unimos todas las posibles combinaciones y variantes
posibles_contrasenas = set(combinaciones + variantes + mayus_variantes)

# Guardamos las contraseñas en un archivo de texto
with open("posibles_contrasenas.txt", "w") as file:
    for pw in posibles_contrasenas:
        file.write(pw + "\n")

print("Las posibles contraseñas se han guardado en 'posibles_contrasenas.txt'")
