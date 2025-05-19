import requests


#--------------------------------------------------------Bastian Onate R----------------------------------------------------



def geolocalizar_ip(ip, token=None):
    url = f"https://ipinfo.io/{ip}/json"
    if token:
        url += f"?token={token}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error al consultar la IP: {e}")
        return None

# Solicita la IP al usuario
ip_ingresada = input("Ingresa la dirección IP que deseas geolocalizar: ")
token = "f523b9e976cf29"  # Si tienes un token de ipinfo.io, escríbelo aquí entre comillas

# Llamada a la función
info = geolocalizar_ip(ip_ingresada.strip(), token)

# Mostrar resultados
if info:
    print("\n📍 Información de geolocalización:")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
