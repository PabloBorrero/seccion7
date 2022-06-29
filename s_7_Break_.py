"""
Ilustrar el uso del break:: (instrucción que forza la salida de un ciclo repetitivo)

Suponga que se crea un meno de opciones con 5 opciones, un de ellas permite salir del ciclo



    MENU DE OPCIONES
    A. Opcion 1
    B. Opcion 2
    C. Opcion 3
    D. Opcion 4
    X. Opcion 5

"""

# OPCIÓN BREAK

try:
    while True:             #Crea un cilco infinito [Nunca termina por si mismo]
    # Mostrar las opciones 
        print("MENU DE OPCIONES")
        print("\tA. opción 1")
        print("\tB. opción 2")
        print("\tC. opción 3")
        print("\tD. opción 4")
        print("\tX. opción 5")
        # Ler la opción
    
        opc = input(" Su ocpion por favor : "). upper ()
        # Ejecutar las acciones
        if opc == 'X':
            break
    # La acción a realizar será despleagr un mensaje con la opción seleccionada
        print(f'Usted ha seleccionad la opción {opc}')
except Exception:
    print ('Error en los datos')
    
    