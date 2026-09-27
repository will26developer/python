#Strings en python

cadena: str = "Hola Mundo desde Python"
print(cadena)


#Textos multilinea
frase: str = """
La vida es bella, pero no lo suficiente,
como para no vivirla.
"""
print(frase)

#Concatenando strings
frase3: str = "Can you"
frase4: str = " borrow me this pencil?"
print(frase3 + frase4)

#Concantenando con f strings
nombre: str = "William"
edad: int = 30
altura: float = 1.80

print(f"Mi nombre es: {nombre} y tengo {edad} anos y mido {altura}")