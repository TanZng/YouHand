# importing vlc module
import vlc

# importing pafy module
import pafy

# url of the video
url = "https://www.youtube.com/watch?v=acEOASYioGY&ab_channel=BadBunny"

# creating pafy object of the video
video = pafy.new(url)

# getting stream at index 0
best = video.streams[0]

# creating vlc media player object
media = vlc.MediaPlayer(best.url)

# start playing video
while True:
    x = int(input("Elija una opcion:\n1. Play\n2. pause\n3. Stop\n"))
    if x == 1:
        media.play()
    if x == 2:
        media.pause()
    if x == 3:
        media.stop()

