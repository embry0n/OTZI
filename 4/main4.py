import cv2

image = cv2.imread('lp.jpg')

image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(image_grey, scaleFactor=1.3, minNeighbors=5)
faces2 = face_cascade.detectMultiScale(image_grey, scaleFactor=1.3, minNeighbors=5)

print(f"{len(faces)} лица обнаружено на изображении.")
print(faces)
print(f"{len(faces2)} лица обнаружено на изображении.")
print(faces2)

for x, y, width, height in faces:
    cv2.rectangle(image, (x,y), (x+width, y+height), color=(0, 0, 255), thickness=15)

for x, y, width, height in faces2:
    cv2.rectangle(image, (x,y), (x+width, y+height), color=(0, 0, 255), thickness=15)

cv2.imwrite('image_2.jpg', image)