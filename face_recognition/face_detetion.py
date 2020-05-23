import cv2
import face_recognition


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    # cap.set(3, 640)  # set Width
    # cap.set(4, 480)  # set Height
    while (True):
        ret, frame = cap.read()
        # frame = cv2.flip(frame, -1) #Flip camera vertically
        if ret:
            face_locations = face_recognition.face_locations(frame)
            for face in face_locations:
                print("face: ", face)
                top, right, bottom, left = face
                color = (0, 0, 0)
                # Line thickness of 2 px
                thickness = 5
                cv2.rectangle(frame, (left, top), (right, bottom), color, thickness)

            cv2.imshow('Face Detection', frame)

            k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            print("Call ESC")
            break
    cap.release()
    cv2.destroyAllWindows()