# **YouHand** <img src="https://raw.githubusercontent.com/TanZng/YouHand/master/src/youhand.gif" width="100" align="left" />
<br/>
<img src="https://github.com/TanZng/YouHand/blob/master/src/gifDemo.gif?raw=true" width="400" align="center" />
<br/>

Video Demo: WIP

### Instalacion

Se recomienda Python 3.8.x

Instalar chromedriver

https://sites.google.com/a/chromium.org/chromedriver/

Para instalar opencv
```bash
pip install --upgrade pip
pip install opencv-python==4.2.0.32
```

Para instalar los requerimientos
###Oli, de nuevo
```bash
pip3 install -r requirements.txt
```

### Ejecutar

Usar el comando

```bash
python3 main.py
```


### Comandos utiles

Obtener requeriminetos
```bash
pip3 freeze > requirements.txt
```

Puede agregar en el script youhand.py lo siguiente si su controlador no es detectado.

```python
browser = webdriver.Chrome(executable_path='/ruta/chromedriver')
```

### Creditos
- [Gabriela Solano](https://github.com/GabySol): Ingeniera y creadora de contenido sobre visión por computador, nos apoyamos en sus tutoriales para contar los dedos levantados a través de la webcam.
- [Andrea Aranda](https://github.com/Andy-Aranda): Desarrolladora de la UI y UX.
- [Tania Zuñiga](https://github.com/Delttoria): Product Manager.
- [Gregorio César Cuevas Herrera](https://github.com/Delttoria): Tech Lead.
- [Emiliano Montoya](https://github.com/Emi-bit): Desarrollador.
- [Daniel Nieto](https://github.com/danielnietod): Desarrollador.

### LICENSE
[MIT License](https://github.com/TanZng/YouHand/blob/master/LICENSE)

