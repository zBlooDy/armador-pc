import logging
from armador.armador_pc import armar_pc
from config.colores import Colors
from storage.exportar import exportar_resultados

def carga_perfiles(perfiles_entrada):
    
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