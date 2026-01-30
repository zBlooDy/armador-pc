import logging
import pandas as pd
from armador.armador_perfiles import carga_perfiles

from config.colores import Colors
from config.perfiles import PERFILES
from perfil.inferencia_perfil import definir_perfil

def carga_formularios():
    ruta = "formularios/resultados.csv"

    # Leer csv que tiene el resultado del google forms
    print(f"{Colors.CYAN}⌛ Cargando respuestas de formulario, por favor espere...{Colors.RESET}\n")
    
    try:
        df = pd.read_csv(ruta)
        logging.info("✅ Formulario cargado correctamente")
    except Exception as e:
        logging.error(f"✗ No se pudo cargar el formulario: {e}")
        return
    
    perfiles = []
    
    # Recorremos el df
    for _, fila in df.iterrows():
        nombre = fila.iloc[1]
        presupuesto = int(fila.iloc[2])
        cantidad = int(fila.iloc[3])

        logging.info(f"Procesando perfil: {nombre}, Presupuesto: {presupuesto}, Cantidad: {cantidad}")

        texto = construir_texto_respuestas(df, fila)

        tipo_perfil = definir_perfil(texto)

        perfiles.append({
            "nombre": nombre,
            "tipo": PERFILES[tipo_perfil],
            "presupuesto": presupuesto,
            "cantidad_pcs": cantidad
        })

        print(f"{Colors.GREEN}✅ Perfil '{nombre}' añadido correctamente{Colors.RESET}\n")

    
    logging.info("✅ Todos los perfiles de formularios fueron procesados correctamente. Iniciando armado de pcs...")
    
    carga_perfiles(perfiles)


def construir_texto_respuestas(df, fila):
    texto = ""


    for col in df.columns[4:]:
        respuesta = fila[col]
        if pd.notna(respuesta):
            texto += f"{col}: {respuesta}\n"
    
    logging.info("Respuestas cargadas correctamente para definir el perfil")

    return texto 


