
#Diccionarios

persona: dict[str, str | int] = {
    "nombre": "William",
    "edad": 30,
    "ciudad": "España"
}
print(persona)

#Acceso
print(persona["nombre"])
print(persona.get("profesion"))          # None, sin error
print(persona.get("profesion", "N/A"))   # con default

#Modificacion
persona["edad"] = 31
persona["profesion"] = "Almacen"
print(persona)

persona.setdefault("pais", "España")
print(persona)

#Actualizar con otro dict
persona.update({"edad": 32, "hobby": "Python"})
print(persona)

#Eliminar
hobby = persona.pop("hobby")
print(hobby, persona)

#Iterar - lo mas comun
for clave, valor in persona.items():
    print(clave, "->", valor)

print(list(persona.keys()))
print(list(persona.values()))