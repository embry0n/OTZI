import zipfile
from tqdm import tqdm

worldlist = 'passwords.txt'
zip_file = 'meow.zip'
zip_file = zipfile.ZipFile(zip_file)

n_words = len(list(open(worldlist, 'rb')))

with open(worldlist, "rb") as worldlist:
    for word in tqdm(worldlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("Пароль найден", word.decode().strip())
            exit(0)
print("Паполь не найден")