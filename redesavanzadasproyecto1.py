import requests
import dns.resolver

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
ip_ingresada = input("Ingresa la dirección IP que deseas geolocalizar y ver si esta en una lista negra: ")
token = "f523b9e976cf29"  # Si tienes un token de ipinfo.io, escríbelo aquí entre comillas

# Llamada a la función
info = geolocalizar_ip(ip_ingresada.strip(), token)

# Mostrar resultados
if info:
    print("\n📍 Información de geolocalización:")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")


#---------------------------------------------------------Fernando Amaro H---------------------------------------------------


# Listas negras DNS comunes
dnsbls = [
    "zen.spamhaus.org",
    "bl.spamcop.net",
    "dnsbl.sorbs.net",
    "b.barracudacentral.org"
]

def check_blacklist(ip):
    # Reversa la IP para la consulta DNSBL (formato requerido)
    reversed_ip = ip_ingresada

    print(f"\nVerificando IP: {ip} en listas negras...\n")

    for dnsbl in dnsbls:
        query = f"{reversed_ip}.{dnsbl}"
        try:
            # Si tiene respuesta, está en la lista negra
            dns.resolver.resolve(query, "A")
            print(f"⚠️  La IP está en la lista negra: {dnsbl}")
        except dns.resolver.NXDOMAIN:
            print(f"✅ No está en la lista negra: {dnsbl}")
        except Exception as e:
            print(f"❓ Error consultando {dnsbl}: {e}")

# Solicita al usuario una IP
ip_input = input("Ingresa la dirección IP a verificar: ").strip()

# Validación básica de IP
import ipaddress
try:
    ipaddress.ip_address(ip_input)
    check_blacklist(ip_input)
except ValueError:
    print("❌ Dirección IP no válida.")