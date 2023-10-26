import cv2


def face_capture():
    cascade_path = 'haarcascade_frontalface_default.xml'

    clf = cv2.CascadeClassifier(cascade_path)
    camera = cv2.VideoCapture('video_2023-10-12_17-57-40.mp4') #video
    #camera = cv2.VideoCapture(0) #webcamera

    while True:
        meow, frame = camera.read
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1, # на сколько уменьшается изображение при каждом масштабе
            minNeighbors=5, #чем больше число, тем строже критерий отбора
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)

        cv2.imshow('Faces', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    # cv2.destroyAllWindows()


face_capture()
# def main():
#     face_capture()
#
#
# if __name__ == '__main__':
#     main()
