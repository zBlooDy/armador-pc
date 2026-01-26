import os
from armador.armador_pc import armar_pc
from config.perfiles import PERFILES
from storage.exportar import exportar_resultados
import logging

# Códigos ANSI para colores
class Colors:
    RESET = '\033[0m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'

def main():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
            filename="logs/proceso.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
    )   
    
    
    perfiles_entrada = menu()
    resultados = []
    
    for perfil in perfiles_entrada: 
        logging.info(f"================ Armando computadoras para el perfil: {perfil['tipo']['description']} con presupuesto {perfil['presupuesto']} =================")
        print(f"\n{Colors.MAGENTA}{'='*65}{Colors.RESET}")
        print(f"{Colors.CYAN}Armando computadoras para: {perfil['nombre']} por favor espere...{Colors.RESET}")
        print(f"{Colors.MAGENTA}{'='*65}{Colors.RESET}\n")
        
        computadoras_armadas = []
        for num_pc in range(perfil['cantidad_pcs']):
            computadora = armar_pc(perfil)
            computadoras_armadas.append(computadora)
            print(f"{Colors.GREEN}✓ PC {num_pc + 1} armada exitosamente{Colors.RESET}")
            logging.info(f"================ Computadora armada para el perfil: {perfil['tipo']['description']} =================")
        
        resultados.append({
            "nombre": perfil["nombre"],
            "tipo": perfil["tipo"]["description"],
            "presupuesto": perfil["presupuesto"],
            "pcs": computadoras_armadas
        })
    
    if resultados:
        print(f"\n{Colors.YELLOW}⌛ Generando archivo de resultados...{Colors.RESET}")
        exportar_resultados(resultados)
        print(f"{Colors.GREEN}✓ Resultados guardados exitosamente{Colors.RESET}\n")


def menu():
    print(f"\n{Colors.CYAN} >>>> Bienvenido al sistema de armado de PCs.{Colors.RESET}")
    print(f"{Colors.CYAN}Se armarán computadoras según perfiles predefinidos y presupuestos asignados.{Colors.RESET}\n")
    print(f"{Colors.CYAN}En caso de no tener suficiente presupuesto para un componente, no se seleccionara el mismo y se avanzara al siguiente.{Colors.RESET}\n")
    
    perfiles = []
    
    while True:
        tipo = input(f"{Colors.YELLOW}Ingrese su tipo de perfil: gaming | oficina | editor (o 'salir' para terminar): {Colors.RESET}").lower()
        if tipo == 'salir':
            print(f"{Colors.GREEN}✅ Gracias por usar el sistema. Vuelva pronto!{Colors.RESET}")
            break

        if tipo not in PERFILES:
            print(f"{Colors.RED}✗ Tipo de perfil no válido. Por favor, intente de nuevo.{Colors.RESET}")
            continue
        
        presupuesto = input(f"{Colors.YELLOW}Ingrese su presupuesto total para la PC: {Colors.RESET}")
        try:
            presupuesto = int(presupuesto)
            if presupuesto <= 0:
                raise ValueError
        except ValueError:
            print(f"{Colors.RED}✗ Por favor, ingrese un número válido para el presupuesto.{Colors.RESET}")
            continue

        cantidad_pcs = input(f"{Colors.YELLOW}Ingrese la cantidad de PCs a armar para este perfil: {Colors.RESET}")
        try:
            cantidad_pcs = int(cantidad_pcs)
            if cantidad_pcs <= 0:
                raise ValueError
        except ValueError:
            print(f"{Colors.RED}✗ Por favor, ingrese un número válido para la cantidad de PCs.{Colors.RESET}")
            continue

        nombre = input(f"{Colors.YELLOW}Ingrese un nombre para este perfil: {Colors.RESET}")

        perfiles.append({
            "nombre": nombre,
            "tipo": PERFILES[tipo],
            "presupuesto": presupuesto,
            "cantidad_pcs": cantidad_pcs
        })
        
        print(f"{Colors.GREEN}✅ Perfil '{nombre}' añadido correctamente{Colors.RESET}\n")

    return perfiles


main()