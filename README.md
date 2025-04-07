# Entorno virtual

**Para crear el entorno virtual**:

```
python -m venv .venv
```

**Para activar el entorno virtual**:

```
source .venv/bin/activate
```

**Para instalar las dependencias**:

```
pip install flask
```

## Para correr el programa

**Solo la maquina local**:

```
flask run
```

**Para activar el debugger**:

```
flask run --debug
```

**esde cualquier maquina de la red**:

```
flask run -h 0.0.0.0
```
