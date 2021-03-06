import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/watch?v=rfFN2xb6CFg&list=RDCLAK5uy_lvjNfBiapOKQwGaT11A5Y3lghUDPmNfpY&start_radio=1")

# video.send_keys(Keys.SPACE) #hits space

videos = browser.find_elements_by_class_name('ytp-play-button')
video = videos[0]

while True:
    try:
        x = int(input("Elija una opcion:"
                      "\n1. Play/Pause"
                      "\n2. Advanza 5 seg"
                      "\n3. Regresa 5 seg"
                      "\n4. Omitir anuncio"
                      "\n5. Subir volumen"
                      "\n6. Bajar volumen"
                      "\n7. Mutear/Desmutear"
                      "\n8. Siguiente Video"
                      "\n9. Poner/Salir fullscreen\n"))
    except ValueError:
        print("Elija un valor valido")

    if x == 1:
        video.click()  # mouse click
    elif x == 2:
        # bars = browser.find_elements_by_class_name('ytp-timed-markers-container')
        video.send_keys(Keys.ARROW_RIGHT)
    elif x == 3:
        video.send_keys(Keys.ARROW_LEFT)
    elif x == 4:
        try:
            boton_saltar_anuncio = browser.find_elements_by_class_name('ytp-ad-skip-button')
            boton_saltar_anuncio[0].click()
        except IndexError:
            print("\nNo hay anuncios que saltar!\n")
    elif x == 5:
        video.send_keys(Keys.ARROW_UP)
    elif x == 6:
        video.send_keys(Keys.ARROW_DOWN)
    elif x == 7:
        boton_mute = browser.find_elements_by_class_name('ytp-mute-button')
        boton_mute[0].click()
    elif x == 8:
        boton_next = browser.find_elements_by_class_name('ytp-next-button')
        boton_next[0].click()
    else:
        boton_fullscreen = browser.find_elements_by_class_name('ytp-fullscreen-button')
        boton_fullscreen[0].click()