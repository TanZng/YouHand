# **YouHand** <img src="https://raw.githubusercontent.com/TanZng/YouHand/master/src/youhand.gif" width="100" align="left" />
<br/>
<br/>

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
WIP

### LICENSE

