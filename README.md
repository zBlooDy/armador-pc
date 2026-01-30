# 🖥️ Sistema de Armado Automático de PCs

Sistema en Python que arma computadoras automáticamente según perfiles predefinidos
(gaming, oficina, edición), presupuesto disponible y precios reales obtenidos mediante scraping al sitio de CompraGamer - Argentina.

El objetivo del proyecto es simular el proceso de armado de PCs de forma inteligente,
adaptándose a restricciones de presupuesto y disponibilidad de componentes.

---

## 🚀 Características principales

- **Menú interactivo** con dos modalidades de carga de datos
- Armado automático de PCs por perfil
- **Inferencia inteligente de perfiles** usando IA (Gemini API)
- **Carga manual** de perfiles con interfaz de consola
- **Carga automática desde formularios** de Google Forms
- Presupuestos dinámicos por componente (basados en porcentajes)
- Selección inteligente de componentes con fallback
- Scraping de precios reales (CompraGamer)
- Exportación de resultados a Excel (una hoja por perfil)
- Manejo de errores y casos límite
- Logs detallados del proceso

---

## 📝 Modalidades de carga

### 1. Carga Manual
Interfaz interactiva por consola que permite:
- Ingresar múltiples perfiles de forma manual
- Especificar nombre, tipo, presupuesto y cantidad de PCs
- Validación en tiempo real de datos ingresados

### 2. Carga por Formulario
Procesamiento automático de respuestas desde Google Forms:
- **Formulario disponible**: https://forms.gle/RaPFWwGnYQXcWip27
- Análisis automático de respuestas usando IA
- Inferencia inteligente del perfil del usuario
- Procesamiento masivo de múltiples solicitudes

---

## � Inferencia Inteligente de Perfiles

El sistema utiliza **Gemini AI** para analizar automáticamente las respuestas del formulario y determinar el perfil más adecuado:

### Proceso de Inferencia:
1. **Análisis de respuestas**: La IA procesa todas las respuestas del usuario
2. **Clasificación automática**: Determina si el usuario necesita un perfil gaming, oficina o editor
3. **Validación**: Sistema de fallback que asigna perfil por defecto en caso de error
4. **Configuración automática**: Aplica automáticamente la configuración del perfil inferido

### Ventajas:
- **Personalización automática**: No requiere conocimiento técnico del usuario
- **Precisión**: Análisis inteligente basado en patrones de uso
- **Escalabilidad**: Procesa múltiples formularios automáticamente

---

## �🧠 Perfiles soportados

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

- **Python 3**: Lenguaje principal
- **Selenium**: Web scraping de precios
- **openpyxl**: Generación de archivos Excel
- **pandas**: Procesamiento de datos de formularios
- **Gemini AI**: Inferencia inteligente de perfiles
- **python-dotenv**: Manejo de variables de entorno
- **logging**: Sistema de logs detallados
- Programación orientada a objetos

---

## 🚀 Cómo usar el sistema

### Opción 1: Formulario Web (Recomendado)
1. Completa el formulario: https://forms.gle/RaPFWwGnYQXcWip27
2. Ejecuta el programa: `python menu.py`
3. Selecciona la opción "2" (Carga por formulario)
4. El sistema procesará automáticamente todas las respuestas

### Opción 2: Carga Manual
1. Ejecuta el programa: `python menu.py`
2. Selecciona la opción "1" (Carga manual)
3. Ingresa los datos solicitados para cada perfil
4. El sistema armará las PCs según los perfiles especificados

### Resultados
- Los resultados se guardan automáticamente en formato Excel
- Cada perfil se exporta en una hoja separada
- Incluye detalles completos de componentes y precios

---

## 📁 Estructura del proyecto
```
armado-pc/
│
├── menu.py                    # Punto de entrada - Menú principal
├── .env                       # Variables de entorno (API keys)
│
├── armador/
│   ├── armador_pc.py         # Lógica principal de armado
│   └── armador_perfiles.py   # Procesamiento de múltiples perfiles
│
├── config/
│   ├── perfiles.py           # Definición de perfiles y porcentajes
│   └── colores.py            # Configuración de colores para consola
│
├── estado/
│   └── estado_pc.py          # Gestión del estado de la PC
│
├── scraper/
│   └── navigation.py         # Web scraping de precios
│
├── selector/
│   └── selector_componentes.py  # Selección inteligente de componentes
│
├── storage/
│   └── exportar.py           # Exportación a Excel
│
├── menu_carga/
│   ├── manual.py             # Interfaz de carga manual
│   └── formulario.py         # Procesamiento de formularios
│
├── perfil/
│   └── inferencia_perfil.py  # IA para inferencia de perfiles
│
├── formularios/
│   └── resultados.csv        # Datos del formulario de Google
│
├── logs/
│   └── proceso.log           # Logs del sistema
│
└── README.md
```
