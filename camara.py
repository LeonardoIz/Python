import cv2


def main():
    camera_index = 0
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("No se puede abrir la camara.")
        return

    print("Presiona 'C' para cambiar de cámara, 'Q' para salir.")

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.release()
            camera_index = (camera_index + 1) % 10
            cap = cv2.VideoCapture(camera_index)
            continue

        cv2.imshow("Camara", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('c'):
            cap.release()
            camera_index = (camera_index + 1) % 10
            cap = cv2.VideoCapture(camera_index)
            if not cap.isOpened():
                camera_index = 0
                cap = cv2.VideoCapture(camera_index)

    cap.release()
    cv2.destroyAllWindows()


main()
