import logging


class EstadoPC:
    def __init__(self, perfil, presupuesto):
        self.perfil = perfil
        self.presupuesto = presupuesto
        self.gastado = 0
        self.componentes = {
            "procesador": None,
            "mother": None,
            "placa de video": None,
            "memoria": None,
            "almacenamiento": None,
            "fuente": None,
            "gabinete": None,
        }


    def presupuesto_restante(self):
        return self.presupuesto - self.gastado

    def agregar_componente(self, tipo, componente):
        """
        componente = {
            "nombre": str,
            "precio": int,
        }
        """
        if tipo in self.componentes:
            self.componentes[tipo] = componente
            self.gastado += componente['precio']
        else:
            logging.error(f"Tipo de componente '{tipo}' no reconocido.")    
    

    def presupuesto_por_componente(self, tipo):
        if tipo in self.perfil['limits']:
            faltantes = [c for c in self.componentes if self.componentes[c] is None]

            suma_porcentajes = sum(self.perfil['limits'][comp] for comp in faltantes)
            
            if suma_porcentajes == 0:
                return self.presupuesto_restante() 
            
            peso_tipo = self.perfil['limits'][tipo]

            return min(self.presupuesto_restante() * (peso_tipo / suma_porcentajes), self.presupuesto_restante())

        else:
            logging.error(f"Tipo de componente '{tipo}' no reconocido.")
            return 0