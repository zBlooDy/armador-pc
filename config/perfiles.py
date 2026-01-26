
PERFILES = {
    "gaming": {
        "description": "PC orientada a juegos",
        "limits": {
            "procesador": 0.22,
            "mother": 0.13,
            "placa de video": 0.35,
            "memoria": 0.10,
            "almacenamiento": 0.10,
            "fuente": 0.06,
            "gabinete": 0.04,
        }
    },

    "oficina": {
        "description": "PC de oficina / estudio",
        "limits": {
            "procesador": 0.30,
            "mother": 0.18,
            "placa de video": 0.00,   # integrada
            "memoria": 0.15,
            "almacenamiento": 0.15,
            "fuente": 0.12,
            "gabinete": 0.10,
        }
    },

    "editor": {
        "description": "Trabajo pesado / render / edición",
        "limits": {
            "procesador": 0.30,
            "mother": 0.15,
            "placa de video": 0.25,
            "memoria": 0.15,
            "almacenamiento": 0.10,
            "fuente": 0.03,
            "gabinete": 0.02,
        }
    }
}
