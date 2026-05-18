import requests


def validar_texto(nombre):
    """
    Valida que el nombre ingresado sea un texto válido.


    Args:
        nombre (str): nombre ingresado por el usuario.

    Returns:
        str: nombre validado, sin espacios al principio ni al final.

    Raises:
        ValueError: si el nombre está vacío o contiene caracteres inválidos.
        TypeError: si el dato ingresado no es un texto.
    """

    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser un texto.")

    nombre = nombre.strip()

    if nombre == "":
        raise ValueError("El nombre no puede estar vacío.")

    for caracter in nombre:
        if not caracter.isalpha() and caracter != " ":
            raise ValueError("El nombre solo puede contener letras y espacios.")

    return nombre


def consultar_nacionalidad(nombre, api_key):
    """
    Consulta la API Nationalize.io para dar las posibles nacionalidades
    asociadas a un nombre.

    La función valida el nombre, arma los parámetros de la consulta,
    realiza el pedido a la API y convierte la respuesta JSON a un
    diccionario de Python.

    Args:
        nombre (str): nombre que se desea consultar.
        api_key (str): clave personal de acceso a la API.

    Returns:
        dict: diccionario con los datos devueltos por la API.
              

    Raises:
        ValueError: si el nombre es inválido, si falta la API key, si la respuesta
                    no tiene formato JSON válido o si no hay países probables.
        ConnectionError: si no se puede conectar con la API.
        TimeoutError: si la API tarda demasiado en responder.
    """

    nombre = validar_texto(nombre)

    if not isinstance(api_key, str) or api_key.strip() == "":
        raise ValueError("La API key no puede estar vacía.")

    url = "https://api.nationalize.io/"

    parametros = {
        "name": nombre,
        "apikey": api_key
    }

    try:
        respuesta = requests.get(url, params=parametros, timeout=10)

    except requests.exceptions.ConnectionError:
        raise ConnectionError("No se pudo conectar con la API.")

    except requests.exceptions.Timeout:
        raise TimeoutError("La API tardó demasiado en responder.")

    if respuesta.status_code != 200:
        raise ValueError("La API respondió con un error")

    try:
        datos = respuesta.json()

    except ValueError:
        raise ValueError("La respuesta de la API no tiene formato JSON válido.")

    if "country" not in datos:
        raise ValueError("La respuesta de la API no contiene información de países.")

    if len(datos["country"]) == 0:
        raise ValueError("No se encontraron países probables para ese nombre.")

    return datos


def obtener_pais_mas_probable(datos):
    """
    Obtiene el país con mayor probabilidad dentro de los datos devueltos
    por la API.

    Args:
        datos (dict): diccionario devuelto por la API. Debe contener
                      la clave "country", asociada a una lista de países.

    Returns:
        dict: diccionario del país con mayor probabilidad.
              

    Raises:
        TypeError: si los datos no son un diccionario.
        ValueError: si no existe la clave "country" o si la lista está vacía.
    """

    if not isinstance(datos, dict):
        raise TypeError("Los datos deben estar en un diccionario.")

    if "country" not in datos:
        raise ValueError("Los datos no contienen la clave 'country'.")

    paises = datos["country"]

    if len(paises) == 0:
        raise ValueError("No hay países disponibles para analizar.")

    pais_mas_probable = paises[0]

    for pais in paises:
        if pais["probability"] > pais_mas_probable["probability"]:
            pais_mas_probable = pais

    return pais_mas_probable


def formatear_probabilidad(probabilidad):
    """
    Convierte una probabilidad en un porcentaje.


    Args:
        probabilidad (float): probabilidad en formato decimal.

    Returns:
        str: probabilidad expresada como porcentaje.

    Raises:
        TypeError: si la probabilidad no es un número.
        ValueError: si la probabilidad está fuera del rango 0 a 1.
    """

    if not isinstance(probabilidad, int) and not isinstance(probabilidad, float):
        raise TypeError("La probabilidad debe ser un número.")

    if probabilidad < 0 or probabilidad > 1:
        raise ValueError("La probabilidad debe estar entre 0 y 1.")

    porcentaje = probabilidad * 100

    return f"{porcentaje:.1f}%"
