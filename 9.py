# Функция для составления плейлиста для мамы
def reverse_playlist(playlist):
    reversed_playlist = playlist[::-1]  #для обратного порядка
    return reversed_playlist


# Ввод плейлиста от папы
papas_playlist = []
print("Введите плейлист папы (по одной песне в строке):")
while len(papas_playlist) < 5:
    song = input()
    papas_playlist.append(song)

# Составление плейлиста для мамы
mamas_playlist = reverse_playlist(papas_playlist)
print("Плейлист мамы:")
for song in mamas_playlist:
    print(song)
