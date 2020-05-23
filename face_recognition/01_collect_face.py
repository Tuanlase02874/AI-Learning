# Input Name
# save image face in class image

import cv2
import face_recognition

if __name__ == '__main__':
    print('Enter your name:')
    inputname = input()
    inputname_image = inputname.replace(" ","_")
    print('Take picture: ' + inputname)
    print('Take picture save image: ' + inputname_image)
    cap = cv2.VideoCapture(0)
    while (True):
        ret, frame = cap.read()
        if ret:
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(image_rgb)
            if len(face_locations) == 1:
                top, right, bottom, left = face_locations[0]
                face_img = image_rgb[top:bottom, left:right, :]
                face_img = cv2.cvtColor(face_img, cv2.COLOR_RGB2BGR)
                save_image_path = "class_image\%s.jpg"%inputname_image
                cv2.imwrite(save_image_path, face_img)
                print("Save face image in %s"% save_image_path)

                color = (0, 0, 0)
                # Line thickness of 2 px
                thickness = 5
                cv2.rectangle(frame, (left, top), (right, bottom), color, thickness)
            cv2.imshow('Camera', frame)
            k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            print("Call ESC")
            break
    cap.release()
    cv2.destroyAllWindows()