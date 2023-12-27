def hide(html_file, message):
    with open(html_file, 'r') as file:
        html_code = file.read()

    encoded_message = message.encode('utf-8').hex()
    modified_html = html_code.replace('<head>', f'<head><meta content="{encoded_message}" name="hidden-message">')

    with open(html_file, 'w') as file:
        file.write(modified_html)

    print('Секретное сообщение успешно спрятано в HTML файле.')


def seek(html_file):
    with open(html_file, 'r') as file:
        html_code = file.read()

    encoded_message = html_code.split('name="hidden-message"')[1].split('content="')[-1].split('"')[0]
    secret_message = bytes.fromhex(encoded_message).decode('utf-8')

    print(f'Извлеченное секретное сообщение: {secret_message}')


html_file_path = 'example.html'
message_to_hide = 'MEOW'

hide(html_file_path, message_to_hide)
seek(html_file_path)