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
print("Ingresa los siguientes datos de la víctima")
nombre = input("Ingresa su nombre: ")
apellido = input("Ingresa su apellido: ")

# Pregunta si se conoce la fecha completa o solo el año
conoce_fecha_completa = input("¿Conoces la fecha completa de nacimiento (DD/MM/AAAA)? Responde 's' para sí o 'n' para solo el año: ").strip().lower()

if conoce_fecha_completa == 's':
    fecha_nacimiento = input("Ingresa su fecha de nacimiento (DD/MM/AAAA): ")
    dia, mes, anio = fecha_nacimiento.split("/")
else:
    anio = input("Ingresa el año de nacimiento (AAAA): ")
    dia = ""
    mes = ""

mascota = input("Ingresa el nombre de su mascota: ")
ciudad = input("Ingresa su ciudad de nacimiento: ")

# Creamos una lista con los datos proporcionados
datos = [nombre, apellido, dia, mes, anio, mascota, ciudad]

# Filtramos para eliminar elementos vacíos
datos = [dato for dato in datos if dato]

# Generamos combinaciones posibles de tres y cuatro elementos
combinaciones = []
for i in range(3, len(datos) + 1):
    combinaciones.extend([''.join(combo) for combo in permutations(datos, i)])

# Añadimos variantes comunes y patrones típicos
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
    dia + "_" + mes + "_" + anio           # Fecha con separadores
]

# Combinaciones específicas de nombre + mascota + año, mes o día
variantes += [
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

# Espera a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")
