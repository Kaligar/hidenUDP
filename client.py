import socket
import struct

def send_data_in_chunks(client_socket, data, server_ip, port, max_packet_size=65507):
    # El tamaño máximo del paquete UDP es 65535, y tenemos que restar el tamaño de la cabecera UDP (28 bytes)
    chunk_size = max_packet_size - 28  # 65507 bytes disponibles para los datos

    # Fragmentar los datos en trozos más pequeños
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        packet = struct.pack("Q", len(data)) + chunk  # Prepend the total length of the data
        client_socket.sendto(packet, (server_ip, port))

# Creación del socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_IP = '127.0.0.1'
PORT = 12345
data = b'... tu dato muy largo ...'

send_data_in_chunks(client_socket, data, SERVER_IP, PORT)
