import cv2

# Загрузка изображения
image = cv2.imread("help.jpg")
# преобразуем изображение к оттенкам серого
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# инициализировать распознаватель лиц (каскад Хаара по умолчанию)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# обнаружение всех лиц на изображении
faces = face_cascade.detectMultiScale(image_grey)
# количество найденных лиц
print(f"{len(faces)} лиц обнаружено на изображении.")
# для всех обнаруженных лиц рисуем синий квадрат
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    # сохраним изображение с обнаруженными лицами
    cv2.imwrite("detected.jpg", image)