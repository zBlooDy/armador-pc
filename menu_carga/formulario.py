import logging
import pandas as pd
import gspread

from armador.armador_perfiles import carga_perfiles
from google.oauth2.service_account import Credentials
from config.colores import Colors
from config.perfiles import PERFILES
from perfil.inferencia_perfil import definir_perfil

def carga_formularios():

    # Leer google sheet 
    print(f"{Colors.CYAN}⌛ Cargando respuestas de formulario, por favor espere...{Colors.RESET}\n")
    
    df = leer_google_sheet()
    
    perfiles = []
    
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



def leer_google_sheet():
    
    sheet_id = "18RfGSNjimd84MT_FjP6HdgU5OOCukC-2LsiWLGLtiMw"
    
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credenciales/google_sheets.json",
        scopes=scopes
    )

    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id).sheet1

    data = sheet.get_all_records()

    df = pd.DataFrame(data)

    logging.info("✅ Google Sheet leída correctamente")

    return df
