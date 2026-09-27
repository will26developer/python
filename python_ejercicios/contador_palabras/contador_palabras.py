from re import sub

def contador_palabras(text: str) -> dict[str, int]:
    clean_text: list[str] = sub(r'\W+', ' ', text.lower()).split()
    word_map: dict[str, int] = dict.fromkeys(clean_text, 0)
    for word in clean_text:
        word_map[word] += 1
    return word_map


texto: str = """
Python es un lenguaje de programacion muy popular. Python se usa en ciencia de datos,
en inteligencia artificial y en desarrollo web. Muchos programadores eligen Python
porque Python es facil de leer y facil de aprender. La comunidad de Python es enorme
y ofrece muchas librerias utiles. Si quieres aprender programacion, Python es una
muy buena opcion para empezar. Python tambien se usa mucho en automatizacion de tareas.
"""

print(contador_palabras(texto))