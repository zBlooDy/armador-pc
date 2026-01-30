import requests
import logging
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def definir_perfil(texto_respuestas):
    prompt = f"""
    Sos un sistema que clasifica perfiles de uso de computadoras.

    Tu tarea es analizar respuestas de una persona y determinar qué tipo de PC necesita.

    Los únicos perfiles posibles son:
    - gaming → PC orientada principalmente a videojuegos
    - oficina → PC para tareas básicas: estudio, trabajo administrativo, navegación, uso general
    - editor → PC para tareas exigentes como edición de video, render, modelado 3D, diseño profesional o programación pesada

    Reglas estrictas:
    - Respondé únicamente con UNA palabra
    - La respuesta debe ser exactamente una de estas: gaming, oficina o editor
    - No expliques tu respuesta
    - No agregues texto adicional
    - No uses mayúsculas

    Analizá las siguientes preguntas y respuestas del usuario:

    {texto_respuestas}
    """

    respuesta_api = call_gemini_api(prompt)
    perfil_inferido = respuesta_api.strip().lower()
    
    if perfil_inferido in ["gaming", "oficina", "editor"]:
        logging.info(f"Perfil definido correctamente: {perfil_inferido}")
        return perfil_inferido
    else:
        logging.error(f"✗ Respuesta inválida del API de OpenAI: {perfil_inferido}. Se setea 'oficina' por defecto.")
        return "oficina"
    



def call_gemini_api(prompt): 

    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    except Exception as e:
        logging.error(f"✗ Error al inicializar el cliente de Gemini: {e}")
        return "oficina"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text