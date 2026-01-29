from config.perfiles import PERFILES
from config.colores import Colors
from armador.armador_perfiles import carga_perfiles

def menu_carga_manual():
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

    carga_perfiles(perfiles)