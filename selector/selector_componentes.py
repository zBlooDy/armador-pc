import logging
import random

def selector_componente(componentes, tipo, estado_pc):
    techo_precio = estado_pc.presupuesto_por_componente(tipo)
    restante = estado_pc.presupuesto_restante()

    logging.info(f"Seleccionando {tipo} | Techo={techo_precio} | Restante={restante}")

    # 1. Caso ideal
    componentes_validos = [
        c for c in componentes
        if c['precio'] <= techo_precio and c['precio'] <= restante
    ]

    if componentes_validos:
        top_3 = sorted(componentes_validos, key=lambda x: x['precio'], reverse=True)[:3]
        return random.choice(top_3)

    # 2. Buscamos el mas barato dentro del presupuesto restante
    logging.warning(
        f"No hay {tipo} dentro del techo. Buscando el mas barato posible."
    )

    posibles = [c for c in componentes if c['precio'] <= restante]

    if posibles:
        return min(posibles, key=lambda x: x['precio'])

    # 3. Peor caso, no tenemos presupuesto
    logging.error(f"No se pudo seleccionar {tipo}. Presupuesto insuficiente.")
    return None
