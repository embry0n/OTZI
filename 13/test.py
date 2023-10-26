import cv2


# def face_capture():
#     cascade_path = 'path_to_haarcascade_frontalface_default.xml'
#
#     clf = cv2.CascadeClassifier(cascade_path)
#     camera = cv2.VideoCapture('video_2023-10-12_17-57-40.mp4')
#
#     while True:
#         _, frame = camera.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         faces = clf.detectMultiScale(
#             gray,
#             scaleFactor=1.1,
#             minNeighbors=5,
#             minSize=(30, 30),
#             # flags=cv2.CASCADE_SCALE_IMAGE
#         )
#
#         for (x, y, width, height) in faces:
#             cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
#
#         cv2.imshow('Faces', frame)
#
#         if cv2.waitKey(1) == ord('q'):
#             break
#
#     camera.release()
#     cv2.destroyAllWindows()
#
#
# face_capture()


def face_capture():
    cascade_path = 'haarcascade_frontalface_default.xml'

    clf = cv2.CascadeClassifier(cascade_path)
    web_camera = cv2.VideoCapture(0) # получаем видео с камеры
    #camera = cv2.VideoCapture('video_2023-10-12_17-57-40.mp4')
    camera = cv2.VideoCapture('meow.mov')

    # пока не нажата любая клавиша — выполняем цикл
    while cv2.waitKey(1)<0:
        # получаем очередной кадр с камеры

        _, frame=camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(gray)
        # если кадра нет
        # if not hasFrame:
        #     # останавливаемся и выходим из цикла
        #     break
        if cv2.waitKey(1) == ord('q'):
            break
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
        # выводим картинку с камеры
        cv2.imshow('Faces', frame)

        # пока не нажата любая клавиша — выполняем цикл
    while cv2.waitKey(1) < 0:
        # получаем очередной кадр с камеры

        _, frame_2 = web_camera.read()
        gray = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
        faces_2 = clf.detectMultiScale(gray)
        # если кадра нет
        # if not hasFrame:
        #     # останавливаемся и выходим из цикла
        #     break
        if cv2.waitKey(1) == ord('q'):
            break
        for (x, y, width, height) in faces_2:
            cv2.rectangle(frame_2, (x, y), (x + width, y + height), (0, 0, 255), 2)
        # выводим картинку с камеры
        cv2.imshow('Faces', frame_2)

    cv2.destroyAllWindows()


face_capture()
