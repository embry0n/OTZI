import speedtest

test = speedtest.Speedtest()
# скорость скачивания, скорость загрузки
print(test.download()/2**20,'\n',test.upload()/2**20)

