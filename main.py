from api_nacionalidad import (
    consultar_nacionalidad,
    obtener_pais_mas_probable,
    formatear_probabilidad
)


API_KEY = input("Ingrese su API key: ")


def mostrar_menu():
    print("Predictor de nacionalidad")
    print("1. Consultar un nombre")
    print("2. Comparar 2 nombres")
    print("3. Salir")


while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese un nombre: ")

        try:
            datos = consultar_nacionalidad(nombre, API_KEY)
            pais_mas_probable = obtener_pais_mas_probable(datos)

            print("\nNombre consultado:", datos["name"])
            print("Cantidad de registros:", datos["count"])

            print("\nPaíses probables:")

            for i, pais in enumerate(datos["country"], start=1):
                codigo_pais = pais["country_id"]
                probabilidad = formatear_probabilidad(pais["probability"])
                print(f"{i}. {codigo_pais} - {probabilidad}")

            print("\nPaís más probable:", pais_mas_probable["country_id"])

        except ValueError as error:
            print("Error:", error)

        except ConnectionError as error:
            print("Error de conexión:", error)

        except TimeoutError as error:
            print("Error de tiempo:", error)

    elif opcion == "2":
        nombre_1 = input("Ingrese el primer nombre: ")
        nombre_2 = input("Ingrese el segundo nombre: ")

        try:
            datos_1 = consultar_nacionalidad(nombre_1, API_KEY)
            datos_2 = consultar_nacionalidad(nombre_2, API_KEY)

            pais_1 = obtener_pais_mas_probable(datos_1)
            pais_2 = obtener_pais_mas_probable(datos_2)

            probabilidad_1 = formatear_probabilidad(pais_1["probability"])
            probabilidad_2 = formatear_probabilidad(pais_2["probability"])

            print("\nResumen de predicciones:")
            print(f"{datos_1['name']} -> {pais_1['country_id']} {probabilidad_1}")
            print(f"{datos_2['name']} -> {pais_2['country_id']} {probabilidad_2}")

        except ValueError as error:
            print("Error:", error)

        except ConnectionError as error:
            print("Error de conexión:", error)

        except TimeoutError as error:
            print("Error de tiempo:", error)

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
