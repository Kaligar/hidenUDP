import socket
import struct

def receive_data_in_chunks(server_socket):
    total_data = b""
    while True:
        data, addr = server_socket.recvfrom(65507)  # Tamaño máximo del paquete UDP sin los encabezados
        total_data += data[8:]  # Ignorar el tamaño total (8 primeros bytes)
        if len(data) < 65507:  # Si los datos recibidos son más pequeños que el tamaño máximo
            break
    return total_data

# Creación del socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12345))

while True:
    data = receive_data_in_chunks(server_socket)
    print(f"Datos recibidos: {data}")

