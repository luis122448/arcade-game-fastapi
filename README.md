# Arcade Game ( Backend )

Proyecto Backend con FastAPI (Python) y PostgreSQL para el registro de puntuciones de un juego de arcade.

## Requisitos

- Python 3.8
- PostgreSQL 15.1

## Configuración de la Base de Datos

En la carpeta raíz del proyecto, crea un archivo llamado .env y define las siguientes variables de entorno:

```dotenv
DB_USERNAME=usuario
DB_PASSWORD=password
DB_HOSTNAME=database_host
DB_PORT=puerto
DB_NAME=nombre_db
```

Asegúrate de reemplazar los valores usuario, password, database_host, puerto y nombre_db con los datos de acceso correspondientes a tu base de datos. Si estás utilizando un servicio de bases de datos en la nube, asegúrate de proporcionar los detalles de conexión correctos.

## Instalación

Clonar el repositorio

```bash
git clone https://github.com/danmondra/pruebas-tecnicas.git
```
En la carpeta raíz del proyecto :

Ejecutar el siguiente comando para instalar las dependencias

```bash
pip install -r requirements.txt
```

finalmente ejecutar el siguiente comando para iniciar el servidor
```bash
python main.py
```

## Uso

En la ruta raíz del proyecto se encuentra el archivo main.py que es el archivo principal del proyecto.

```bash
python main.py
```

Puedes configurar el Host y el Puerto en el metodo main del archivo main.py

```python

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)),
                reload=True,
                )

```

Documentacion de las APIREST ( Local ) la encontraras en la siguiente ruta

```bash
http://localhost:8000/docs

```


## Contribución

Las solicitudes de extracción son bienvenidas. Para cambios importantes, abra un problema primero para discutir qué le gustaría cambiar.

## Autores

[Luis Antonio Calvo Quispe](https://www.linkedin.com/in/luis-antonio-calvo-quispe-7b0b0a1b0/)

## Licencia

MIT License

## Agradecimientos

Agradece a las personas o proyectos que hayan sido una fuente de inspiración o que hayan proporcionado asistencia para el desarrollo de tu proyecto.

## Estado del Proyecto

Puedes agregar información sobre el estado actual del proyecto, si está en desarrollo, en producción o archivado. También puedes agregar un enlace al proyecto en línea o a la documentación.

## Contacto

luis122448@gmail.com
