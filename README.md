# Arcade Game ( Backend )

Proyecto Backend con FastAPI (Python) y PostgreSQL para el registro de puntuciones de un juego de arcade.

## Requisitos

- Python 3.8
- PostgreSQL 13.2

## Instalación

Clonar el repositorio

```bash
pip install -r requirements.txt
```
En la carpeta raíz del proyecto :

Crear un archivo .env con las siguientes variables de entorno :
( Recuerda ajustalo a tu base de datos Local o en Nube )

DB_USERNAME=usuario
DB_PASSWORD=password
DB_HOSTNAME=database_host
DB_PORT=puerto
DB_NAME=nombre_db

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
