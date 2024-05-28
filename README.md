# Instrucciones de uso

Disclaimer: **Esta herramienta solo funciona en la máquina prime**
Esto debido a configuraciones con el login de Microsoft

### Instalación
Una vez en prime ejecutar:
```
docker compose up --build -d
```


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
