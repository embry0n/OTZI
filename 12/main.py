import subprocess


try:
    data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "Все профили пользователей" in i]
    wifi = []
    passwords = []

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')

        for j in results:
            if "Содержимое ключа" in j:
                wifi.append(f"{i}")
                passwords.append(f"{j.split(':')[1][1:-1]}")

    print(wifi)
    for password in range(0, len(passwords)):
        passwords[password] = '*' * len(passwords[password])
    print(passwords)
except Exception as ex:
    print(f'Ошибка: {ex}')
