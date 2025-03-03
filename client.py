import cv2
import socket
import struct
import pickle

# Dirección IP y puerto del servidor
SERVER_IP = "127.0.0.1"  # Cambia a la IP del servidor si está en otra máquina
PORT = 5000

# Crear socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir la imagen a bytes
    data = pickle.dumps(frame)
    
    # Enviar el tamaño del paquete seguido de los datos
    client_socket.sendto(struct.pack("Q", len(data)) + data, (SERVER_IP, PORT))

    # Mostrar lo que se está enviando
    cv2.imshow("Cliente - Enviando", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
client_socket.close()
cv2.destroyAllWindows()
