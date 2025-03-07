import cv2

cap = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)  # Usa tu pipeline si es necesario

if not cap.isOpened():
    print("❌ Error: No se pudo abrir la cámara o el archivo de video.")
else:
    print("✅ Cámara o video abierto correctamente.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ No se pudo leer el cuadro.")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
