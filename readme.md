# Levantar proyecto

#### Clonar repositorio
  ```sh
  $ git clone https://github.com/joalrope/blocks-py.git
```
  
#### Instalar virtualvenv
```sh
  $ pip install virtualenv
```
#### Ir a carpeta del repositorio clonado para activar entorno virtual e instalar dependencias
```sh
  $ virtualenv venv
  $ source venv/bin/activate #linux, mac
  $ venv/Scripts/activate # windows
  $ pip install -r requirements.txt
```

#### Ejecutar proyecto
```sh
  $ "carpeta/repositorio/clonado/venv/Scripts/python.exe" "carpeta/repositorio/clonado/main.py"
``` 

#### Ejecutar pruebas automaticas
```sh
  $ pytest
``` 
