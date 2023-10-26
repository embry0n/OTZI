import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=ex9tML6udCU')

print(yt.streams.filter(file_extension='mp4'))
stream = yt.streams.get_by_itag(22) #выбираем по тегу, в каком формате будем скачивать.
stream.download() #загружаем видео.
