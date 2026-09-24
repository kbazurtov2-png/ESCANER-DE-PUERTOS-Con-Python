#ESCÁNER DE PUERTOS DE RED
#Universidad Estatal de Milagro (UNEMI) Grupo #10

#INTEGRANTES:
#Añasco Espinoza Darío Franco
#Arias Escobar Genaro Israel
#Bazurto Velez Kevin Ariel
#Castro Escobar Milly Crisol
#Cobo Ordoñez José Rodolfo
#Cárdenas Toala Ximena Gabriela
#Guamán Vasconez Rolando Alexander

#Descripción:
#    Programa de consola que verifica qué puertos TCP se
#    encuentran abiertos en un equipo dentro de un rango
#    definido por el usuario.
#---------------------------------------------------------
        
import socket
from datetime import datetime

print("-" * 50)
print("           ESCÁNER DE PUERTOS TCP")
print("-" * 50)

# Entrada de datos
ip_objetivo = input("Ingrese la dirección IP a escanear: ")
puerto_inicial = int(input("Ingrese el puerto inicial: "))
puerto_final = int(input("Ingrese el puerto final: "))

print("-" * 50)
print(f"\n[+] Escaneando IP: {ip_objetivo}")
print(f"[+] Rango de puertos: {puerto_inicial} - {puerto_final}")
print(f"[+] Hora de inicio: {datetime.now().strftime('%H:%M:%S')}")
print("-" * 50)

puertos_abiertos = []

# Escaneo de puertos
for puerto in range(puerto_inicial, puerto_final + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.05)
    resultado = sock.connect_ex((ip_objetivo, puerto))
    if resultado == 0:
        print(f"Puerto {puerto} - ABIERTO")
        puertos_abiertos.append(puerto)
    sock.close()

# Mostrar resumen
print("RESULTADOS OBTENIDOS:")
print(f"[+] Puertos analizados: {puerto_final - puerto_inicial + 1}")
print(f"[+] Puertos abiertos: {len(puertos_abiertos)}")
if puertos_abiertos:
    print(f"[+] Lista de puertos abiertos: {puertos_abiertos}")
else:
    print("[!] No se encontraron puertos abiertos en el rango indicado")
print(f"[+] Hora de finalización: {datetime.now().strftime('%H:%M:%S')}")
print("-" * 100)
