# Esto solo es para probar que si funcione el regex

from src.regex import preparar_regex

regex = input("Ingrese la expresión regular: ")

regex_preparada, alfabeto = preparar_regex(regex)

print("\nRegex preparada:", regex_preparada)
print("Alfabeto:", alfabeto)
