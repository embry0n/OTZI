import cv2


def face_capture():
    cascade_path = 'haarcascade_frontalface_default.xml'

    clf = cv2.CascadeClassifier(cascade_path) 
    web_camera = cv2.VideoCapture(0) # получаем видео с камеры
    camera = cv2.VideoCapture('meow.mov')

    # пока не нажата любая клавиша — выполняем цикл. определяем лицо на видео
    while cv2.waitKey(1)<0:
        # получаем очередной кадр с камеры

        _, frame=camera.read() # получаем кадр
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # серим кадр
        faces = clf.detectMultiScale(gray) # детектим

        # для остановки программы нажмем q
        if cv2.waitKey(1) == ord('q'):
            break
        # рисуем квадраты
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
        # выводим картинку с камеры
        cv2.imshow('Faces', frame)

    # все тоже самое только уже для обработки вебкамеры
    while cv2.waitKey(1) < 0:
        # получаем очередной кадр с камеры

        _, frame_2 = web_camera.read()
        gray = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
        faces_2 = clf.detectMultiScale(gray)

        if cv2.waitKey(1) == ord('q'):
            break
        for (x, y, width, height) in faces_2:
            cv2.rectangle(frame_2, (x, y), (x + width, y + height), (0, 0, 255), 2)
        # выводим картинку с камеры
        cv2.imshow('Faces', frame_2)

    cv2.destroyAllWindows()


face_capture()
