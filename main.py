import os
import tkinter
import tkinter.messagebox
import sys


# Funciones principales
# Salida
def salir():
    sys.exit()


def ayuda():
    # print("En construccion")
    tkinter.messagebox.showinfo("Ayuda", "Comandos:\nPuño cerrado: Calibrar webcam."
                                         + "\nUn dedo levantado: Retroceder 5s. "
                                         + "\nDos dedos levantados: Pausa / Play. "
                                         + "\nTres dedos levantados: Avanzar 5s. "
                                         + "\nCuatro dedos levantados: Siguiente video."
                                         + "\nCinco dedos levantados: Mute / UnMute. ")


def escuchar():
    global caja_link
    url = caja_link.get()
    if not "https://www.youtube.com/watch" in url:
        # print("Vacio")
        tkinter.messagebox.showinfo("Error", "URL invalida, por favor introduzca una URL valida.")
    else:
        # print("abirendo opencv")
        os.system('python youhand.py ' + url)


# Ventana o panel
window = tkinter.Tk()
window.geometry("380x330")
window.config(bg="white")
window.resizable(0, 0)

# Etiquetas
# Logotipo "YouHand"
label = tkinter.Label(window, text="YouHand")
label.place(x=70, y=70, width=250, height=40)
label.config(fg="midnight blue", font=("Verdana 10 bold", 35), bg="white")

# Señalamiento de link
label_link = tkinter.Label(window, text="Inserte la PlayList:")
label_link.place(x=0, y=120, width=170, height=30)
label_link.config(fg="DodgerBlue4", font=("Verdana 10 bold", 15), bg="white")

# Botones
# Boton de salida
button_exit = tkinter.Button(window, text="Salir", command=salir)
button_exit.place(x=60, y=164, width=90, height=35)
button_exit.config(fg="white", font=("Verdana 10 bold", 14), justify="center", bg="firebrick1")

# Caja de textos
# Caja de link
caja_link = tkinter.Entry(window)
caja_link.place(x=170, y=120, width=170, height=28)
caja_link.config(fg="black", font=("Verdana 10 bold", 14), justify="center", bg="snow2")

# Boton de escuchar
button_escuchar = tkinter.Button(window, text="Escuchar", command=escuchar)
button_escuchar.place(x=240, y=164, width=90, height=35)
button_escuchar.config(fg="white", font=("Verdana 10 bold", 14), justify="center", bg="chartreuse3")

# Boton de ayuda
button_ayuda = tkinter.Button(window, text="Ayuda", command=ayuda)
button_ayuda.place(x=150, y=218, width=90, height=35)
button_ayuda.config(fg="white", font=("Verdana 10 bold", 14), justify="center", bg="turquoise3")


window.mainloop()
