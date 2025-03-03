import cv2
import socket
import struct
import pickle

HOST = "0.0.0.0"  # Escucha en todas las interfaces
PORT = 9999

# Configura el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"[*] Esperando conexiones en {HOST}:{PORT}...")
client_socket, addr = server_socket.accept()
print(f"[+] Conexión establecida con {addr}")

data = b""

try:
    while True:
        # Recibe el tamaño del mensaje
        while len(data) < struct.calcsize("Q"):
            packet = client_socket.recv(4096)
            if not packet:
                break
            data += packet

        if not data:
            break

        # Extrae el tamaño del mensaje
        packed_msg_size = data[:struct.calcsize("Q")]
        data = data[struct.calcsize("Q"):]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        # Recibe el fotograma
        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Deserializa y muestra el fotograma
        frame = pickle.loads(frame_data)
        cv2.imshow("Cámara Remota", frame)

        if cv2.waitKey(1) == ord("q"):
            break

except KeyboardInterrupt:
    print("\nCerrando servidor...")
finally:
    client_socket.close()
    server_socket.close()
    cv2.destroyAllWindows()
