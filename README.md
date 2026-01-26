# 🖥️ Sistema de Armado Automático de PCs

Sistema en Python que arma computadoras automáticamente según perfiles predefinidos
(gaming, oficina, edición), presupuesto disponible y precios reales obtenidos mediante scraping al sitio de CompraGamer - Argentina.

El objetivo del proyecto es simular el proceso de armado de PCs de forma inteligente,
adaptándose a restricciones de presupuesto y disponibilidad de componentes.

---

## 🚀 Características principales

- Armado automático de PCs por perfil
- Presupuestos dinámicos por componente (basados en porcentajes)
- Selección inteligente de componentes con fallback
- Scraping de precios reales (CompraGamer)
- Exportación de resultados a Excel (una hoja por perfil)
- Manejo de errores y casos límite
- Logs detallados del proceso

---

## 🧠 Perfiles soportados

Cada perfil define qué porcentaje del presupuesto total se destina a cada componente:

- **Gaming**: Prioriza GPU y CPU
- **Oficina**: Prioriza estabilidad y bajo costo
- **Editor**: Prioriza CPU y memoria

Los porcentajes son dinámicos:  
Si un componente ya fue seleccionado, su presupuesto se redistribuye entre los restantes.

---

## 💡 Lógica de selección de componentes

Para cada componente:

1. Se calcula un **techo de precio dinámico** según el presupuesto restante
2. Se buscan componentes dentro de ese techo
3. Si no existen:
   - Se selecciona el componente más barato dentro del presupuesto restante
4. Si no hay presupuesto suficiente:
   - Se marca el componente como **"No seleccionado"**

Esto evita que el sistema se rompa por precios variables o inflación.

---

## 📊 Exportación de resultados

Los resultados se exportan a un archivo Excel:

- Una hoja por perfil
- Detalle de cada PC armada
- Componentes, precios, total gastado y presupuesto restante
- Formato legible y listo para presentar al usuario

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Selenium (scraping)
- openpyxl (Excel)
- logging
- Programación orientada a objetos

---

## 📁 Estructura del proyecto
```
armado-pc/
│
├── main.py
│
├── config/
│ ├── perfiles.py
│
├── armador/
│ ├── armador_pc.py
│
├── estado/
│ ├── estado_pc.py
│
├── scraper/
│ ├── navigation.py
│
├── selector/
│ ├── selector_componentes.py
│
├── storage/
│ └── exportar.py
│
├── logs/
│ └── proceso.log
│
└── README.md
```
