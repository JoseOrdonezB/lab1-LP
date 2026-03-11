def imprimir_tabla_transiciones(afd, alfabeto):

    estados = afd["estados"]
    transiciones = afd["transiciones"]
    nombres = afd["nombres"]

    print("\n=== Tabla de transición ===\n")

    encabezado = "Estado\t" + "\t".join(alfabeto)
    print(encabezado)

    for estado in estados:

        fila = nombres[estado]

        for simbolo in alfabeto:

            if simbolo in transiciones[estado]:
                destino = transiciones[estado][simbolo]
                fila += "\t" + nombres[destino]
            else:
                fila += "\t-"

        print(fila)