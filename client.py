import cv2
import socket
import struct
import pickle

HOST = '127.0.0.1'  # Localhost
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    data = pickle.dumps(frame)
    message_size = struct.pack("Q", len(data))
    client_socket.sendall(message_size + data)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
client_socket.close()
cv2.destroyAllWindows()
