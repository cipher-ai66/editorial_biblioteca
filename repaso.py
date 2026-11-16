libros = [
    ("El Quijote", "Miguel de Cervantes", 1605, True),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, True),
    ("La casa de los espíritus", "Isabel Allende", 1982, False),
    ("1984", "George Orwell", 1949, True),
]

print(libros)
print(len(libros))
print(libros[0])
print(libros[0][0])
print("---------------------------")
for libro in libros:
    print(libro[0], "escrito por", libro[1], "en el año", libro[2])
print("---------------------------")
for titulo, autor, año, disponible in libros:
    print(f"{titulo} fue escrito por {autor} en el año {año}. Disponible: {'Sí' if disponible else 'No'}")
print("---------------------------")
for titulo, autor, año, disponible in libros:
    if disponible:
        print(titulo)

print(len([libro[0] for libro in libros if libro[3]]))
