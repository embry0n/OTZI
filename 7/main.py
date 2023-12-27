from PIL import Image


def encode(message, file_name, encoded):
    image = Image.open(file_name)
    if image.mode != "RGB":
        print("Error: only 24-bit BMP files are supported.")
        return
    width, height = image.size
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    binary_message += "00000000"
    if len(binary_message) > (width * height * 3):
        print("Error: message is too long to encode in the image.")
        return

    index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                if index < len(binary_message):
                    pixel[i] = (pixel[i] & 0xFE) | int(binary_message[index])
                    index += 1
            image.putpixel((x, y), tuple(pixel))
    image.save(encoded, "BMP")


def decode(bmp_file_name):
    image = Image.open(bmp_file_name)
    if image.mode != "RGB":
        print("Error: only 24-bit BMP files are supported.")
        return

    width, height = image.size
    binary_message = ""
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                binary_message += str(pixel[i] & 0x01)

    message = ""
    for i in range(0, len(binary_message), 8):
        if int(binary_message[i:i+8], 2) == 0:
            break
        message += chr(int(binary_message[i:i+8], 2))
        #print(message)
        #print(int(binary_message[i:i+8], 2))

    print("Decoded message:", message)


message = "Sorry for my bad england. I from Somalia!"
file_name = "arr.png"
encoded = "arr1.png"

encode(message, file_name, encoded)

decode(encoded)
