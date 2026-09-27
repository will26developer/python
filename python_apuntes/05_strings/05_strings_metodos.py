#Metodos de cadenas

frase1: str = "Hola mundo desde Python"
print(f"Frase original: {frase1}")

print("===== Transformacion de mayusculas / minusculas")
print(f"lower(): {frase1.lower()}")
print(f"upper(): {frase1.upper()}")
print(f"title(): {frase1.title()}")
print(f"capitalize(): {frase1.capitalize()}")
print(f"swapcase(): {frase1.swapcase()}")

print("===== Busqueda y comprabacion")
print(f"index(): {frase1.index("mundo")}")
print(f"find(): {frase1.find("mundo")}")
print(f"count(): {frase1.count('o')}")
print(f"startswith(): {frase1.startswith('H')}")
print(f"endswith(): {frase1.endswith('on')}")

print("===== Comprobacion de tipo de contenido")
print(f"isalpha(): {frase1.isalpha()}")
print(f"isnumeric(): {frase1.isnumeric()}")
print(f"isdigit(): {frase1.isdigit()}")
print(f"isdecimal(): {frase1.isdecimal()}")
print(f"isalnum(): {frase1.isalnum()}")
print(f"isupper(), islower(): {frase1.isupper()} {frase1.islower()}")
print(f"istitle(): {frase1.istitle()}")

print("==== Limpieza y recorte")
print(f"strip(): {frase1.strip()}")
print(f"rstrip(): {frase1.rstrip()}")
print(f"lstrip(): {frase1.lstrip()}")
print(f"replace(): {frase1.replace('o','a')}")

print("==== Division y union")
frase_lista: list[str] = frase1.split()
print(f"split(): {frase_lista}")
print(f"join(): {' ->> '.join(frase_lista)}")

