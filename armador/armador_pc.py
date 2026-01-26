from estado.estado_pc import EstadoPC
from selenium.webdriver.common.by import By 
from scraper.navigation import clickear_boton, crear_driver, esperar_categoria, obtener_componentes, clickear_componente
from selector.selector_componentes import selector_componente
import logging

def armar_pc(perfil):
    orden_componentes = ["procesador", "mother", "cooler", "memoria", "placa de video", "almacenamiento", "fuente", "gabinete"]

    estado_pc = EstadoPC(perfil['tipo'], perfil['presupuesto'])
    

    driver = crear_driver()

    for tipo in orden_componentes:
        
        esperar_categoria(driver, tipo)
        
        if tipo == "cooler":
            clickear_boton(driver, "Saltear paso") 
            continue 

        componentes = obtener_componentes(driver, tipo)

        componente_seleccionado = selector_componente(componentes, tipo, estado_pc)

        
        if componente_seleccionado is None:
            clickear_boton(driver, "Saltear paso")
            falta_componente = {
                "nombre": "No seleccionado",
                "precio": 0
            }
            estado_pc.agregar_componente(tipo, falta_componente)
            continue 
        
        estado_pc.agregar_componente(tipo, componente_seleccionado)
        
        clickear_componente(driver, componente_seleccionado['nombre'])

        # Chequeamos si el titulo es el mismo, en ese caso clickeamos en Siguiente ya que no queremos agregar mas del mismo producto

        h1 = driver.find_element(
                    By.CSS_SELECTOR,
                    "h1.txt_section-name"
                )
        
        if tipo.lower() in h1.text.lower():
            clickear_boton(driver, "Siguiente")


        logging.info(f"Componente seleccionado para {tipo}: {componente_seleccionado['nombre']} - ${componente_seleccionado['precio']}")
    
    driver.quit()

    return estado_pc

