import cv2
import socket
import struct
import pickle

HOST = '127.0.0.1'  # Localhost
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Esperando conexión...")
conn, addr = server_socket.accept()
print(f"Conectado a: {addr}")

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data)
    cv2.imshow("Video Recibido", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

conn.close()
server_socket.close()
cv2.destroyAllWindows()
