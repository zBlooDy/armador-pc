from menu_carga.manual import menu_carga_manual 
from menu_carga.formulario import menu_carga_formulario
from config.colores import Colors
import logging
import os

def mostrar_menu():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
            filename="logs/proceso.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
    )   
    print(f"\n{Colors.MAGENTA}{'='*40}{Colors.RESET}")
    print(f"{Colors.CYAN} >>>> Menú Principal <<<< {Colors.RESET}")
    print(f"{Colors.MAGENTA}{'='*40}{Colors.RESET}\n")
    print(f"{Colors.YELLOW}1. Iniciar armado de computadoras con carga manual de perfiles{Colors.RESET}")
    print(f"{Colors.YELLOW}2. Iniciar armado de computadoras con documento de google{Colors.RESET}")
    print(f"{Colors.YELLOW}3. Salir{Colors.RESET}\n")
    while True:
        eleccion = input(f"{Colors.MAGENTA}Elija una opcion: {Colors.RESET}")
        if eleccion.isdigit():
            match eleccion:
                case "1":
                    menu_carga_manual()
                    break
                case "2":
                    menu_carga_formulario()
                    break
                case "3":
                    print(f"{Colors.GREEN}✅ Gracias por usar el sistema. Vuelva pronto!{Colors.RESET}")
                    exit()
                case _:
                    print(f"{Colors.RED}✗ Opción incorrecta{Colors.RESET}")
        else:
            print(f"{Colors.RED}✗ Ingrese una opcion válida{Colors.RESET}")


mostrar_menu()