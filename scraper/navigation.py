import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException

def crear_driver():
    driver = get_driver()

    try:
        driver.get("https://compragamer.com/armatupc")

        logging.info("✅ CompraGamer cargó correctamente")
    
        return driver
    except Exception as e:
        driver.quit()
        raise e


def obtener_componentes(driver, tipo):
    """
    Se scrapean los elementos de la pagina actual y se formatean en una lista de diccionarios con nombre y precio.
    
    :param driver: Instancia del driver de Selenium.
    """
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'cgw-product-card'))
    )

    cards = driver.find_elements(By.CSS_SELECTOR, 'cgw-product-card')

    componentes = []
    for card in cards:
        
        try:
            card.find_element(
                By.XPATH,
                ".//span[contains(text(), 'Compatible')]"
            )
            es_compatible = True
        except:
            es_compatible = False

        if not es_compatible:
            continue

        
        nombre = card.find_element(By.CSS_SELECTOR, 'h3.product-card__title').text

        precio_container = card.find_element(
            By.CSS_SELECTOR,
            'span.product-card__cart__price--current'
        )

        precio_texto = precio_container.find_elements(By.TAG_NAME, 'span')[1].text
        precio = int(precio_texto.replace('.', ''))

        componentes.append({
            "nombre": nombre,
            "precio": precio,
        })
    
    logging.info(f"Se encontraron {len(componentes)} componentes compatibles para la categoria {tipo}.")
    return componentes


def clickear_componente(driver, nombre_componente):
    """
    Se busca el componente segun el nombre (el cual fue preseleccionado anteriormente) y se hace click en el elemento para seguir con el armado de la PC.
    
    :param driver: Instancia del driver de Selenium.
    :param nombre_componente: Nombre del componente a buscar y clickear.
    """
    wait = WebDriverWait(driver, 10)

    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'cgw-product-card'))
    )

    # Busco el producto que coincida con el nombre
    for card in cards:
        try:
            nombre = card.find_element(By.CSS_SELECTOR, 'h3.product-card__title').text

            if nombre_componente.lower() in nombre.lower():
                # Busco el elemento scroleando
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    card
                )

                wait.until(EC.element_to_be_clickable(card))

                card.click()

                chequeo_ventana(driver)

                return
        except:
            continue


def chequeo_ventana(driver, timeout=2):
    """
    Esta funcion chequea si aparecio alguna alerta/modal en la pagina y la cierra si es asi, caso contrario no hace nada.
    """
    wait = WebDriverWait(driver, timeout)

    try:
        modal = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "mat-dialog-container")
            )
        )

        boton_aceptar = modal.find_element(
            By.XPATH,
            ".//button//span[contains(text(), 'aceptar')]/ancestor::button"
        )

        boton_aceptar.click()
        logging.info("Apareció un modal y fue cerrado.")
        return True

    except TimeoutException:
        # No apareció ningún modal → flujo normal
        return False



def clickear_boton(driver, texto):
    """
    Esta funcion simula el click en el boton "Saltar paso"
    """

    wait = WebDriverWait(driver, 10)

    boton = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{texto}')]/ancestor::button"))
    )

    boton.click()

def esperar_categoria(driver, tipo):
    """
    Espera que la categoria aparezca, simbolo de que la pagina cargo correctamente y las cards pertenecen a la categoria deseada.
    """
    wait = WebDriverWait(driver, 10)

    def h1_contiene_tipo(driver):
        h1 = driver.find_element(
            By.CSS_SELECTOR,
            "h1.txt_section-name"
        )
        return tipo.lower() in h1.text.lower()

    wait.until(h1_contiene_tipo)
    
def get_driver(headless=False):
    """
    Esta funcion inicializa y devuelve un driver de Chrome para abstraernos de la logica en el main.py
    
    :param headless: Booleano que indica si el navegador debe abrirse en modo headless (sin interfaz grafica). Por defecto es False.
    :return: Instancia del driver de Chrome.
    """

    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

