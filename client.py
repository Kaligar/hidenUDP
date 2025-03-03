import cv2
import socket
import struct
import pickle

SERVER_IP = "127.0.0.1"  # Cambia por la IP del servidor
PORT = 9999

# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Configura el socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Serializa el fotograma
        data = pickle.dumps(frame)
        message_size = struct.pack("Q", len(data))

        # Envía el tamaño y el fotograma serializado
        client_socket.sendall(message_size + data)

except KeyboardInterrupt:
    print("\nCerrando conexión...")
finally:
    cap.release()
    client_socket.close()
