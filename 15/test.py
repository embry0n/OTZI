import ipinfo
import sys


# Получаем IP-адрес из командной строки
def probiv_ip_gps():
    try:
        ip_address = sys.argv[1]
    except IndexError:
        ip_address = None

    # Вставьте свой токен доступа сюда
    access_token = ''

    # Создаем объект для работы с сервисом IPinfo
    handler = ipinfo.getHandler(access_token)

    # Получаем информацию об IP-адресе
    details = handler.getDetails(ip_address)


    meow = []
    # Выводим полученные данные
    for key, value in details.all.items():
        #print(f"{key}: {value}")
        meow.append(f"{key}: {value}")
    print(meow[0], meow[1], meow[2])

    return meow