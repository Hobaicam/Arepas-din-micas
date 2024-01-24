print("¡Vamos a hacer una deliciosa arepa!")

print("Primero, elige el tipo de harina")

print("1. Harina de maíz precocida")

print("2. Harina de trigo")

opcion_harina = input("Elige la opción 1 o 2")



if opcion_harina == "1":

    print("¡Excelente elección! Ahora, prepararemos la masa.")

    

    # Preparacion de la masa con harina de maíz precocida

    print("Para preparar la masa con harina de maíz precocida necesitarás mezclar la harina con agua y sal.")

    print("Luego, forma pequeñas bolas con la masa y aplánalas para darles forma de arepa.")

    print("Finalmente, cocínalas en un sartén caliente hasta que estén doradas por ambos lados.")

    # Solicitar ingredientes al usuario
    harina_input = input("Ingresa la cantidad de harina en gramos: ")
    agua_input = input("Ingresa la cantidad de agua en mililitros: ")

    # Convertir strings a números
    harina = int(harina_input)
    agua = float(agua_input)

    # Calcular masa total
    masa_total = harina + agua

    # Resultado final de la masa
    print(f"La masa total de las arepas es: {masa_total} gramos")

    print("Ahora, elige el relleno")

    print("1. Queso")

    print("2. Carne mechada")

    opcion_relleno = input("Elige la opción 1 o 2")



    if opcion_relleno == "1":

        print("Perfecto, has elegido una deliciosa arepa de queso. Recuerda que debes abrirla¡A disfrutar!")

    elif opcion_relleno == "2":

        print("Estupendo, tendrás una sabrosa arepa de carne mechada. ¡Buen provecho!")

    else:

        print("Opción inválida, intenta nuevamente.")

elif opcion_harina == "2":

    print("Hmm, esa no es una opción muy común para hacer arepas. Intenta con harina de maíz precocida.")

else:

    print("Opción inválida, intenta nuevamente.")




