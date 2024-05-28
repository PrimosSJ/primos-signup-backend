# Instrucciones de uso

Disclaimer: **Esta herramienta solo funciona en la máquina prime**
Esto debido a configuraciones con el login de Microsoft

### Instalación
Una vez en prime ejecutar:
```
docker compose up --build -d
```
Esto creará dos contenedores, uno para la base de datos y otro para el backend

### Migraciones
El proyecto fue realizado en Django, asi que vuelve su peor enemigo, las migraciones.

- Identificar el contenedor del backend (no la BD, el backend!!)
```
docker ps -a
```
- Copiar el Container ID
- Acceder a la terminal del contenedor
```
docker exec -it <Container_ID> bash
```
- Navegar hasta la carpeta que tenga el manage.py
- Haga las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- Verifique las migraciones en la base de datos, para eso le recomiendo utilizar el gestor de bases de datos DBeaver.
Para esto tendrán que crear una conexión a través de un túnel SSH, pero como hay otra máquina en medio (apu) tienen que saltar por ahí primero, así que tienen que configurar un SSH Tunnel con un SSH Jump en el DBeaver.
- SSH Jump: credenciales de APU
- SSH Tunnel: credenciales de Prime

Solo tiene que verificar que las tablas se hayan creado con sus respectivas columnas

# Información general sobre servicios de primos

Todos los servicios que tiene Primos están o deberían estar alojados en prime.
Prime es una máquina dentro del departamento de infromática.

### Para acceder a prime desde la red de la U:
- Acceder a APU
- Desde APU ejecutar:
```
ssh primo@prime
```

Podrán ver el estado de los servicios (todos en Docker container) ejecutando:
```
docker ps -a
```
