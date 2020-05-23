import cv2
import face_recognition


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height
    while (True):
        ret, frame = cap.read()
        # frame = cv2.flip(frame, -1) #Flip camera vertically
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_locations = face_recognition.face_locations(frame)
            cv2.imshow('Class1', frame)
            cv2.imshow('Class1 gray', gray)

            k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            print("Call ESC")
            break
    cap.release()
    cv2.destroyAllWindows()


