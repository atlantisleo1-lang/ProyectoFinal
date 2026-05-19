
# ProyectoFinal - Análisis Exploratorio de Datos (EDA): Campaña de Telemarketing Bancario

¡Bienvenido a este proyecto de portafolio profesional! Esta es una aplicación web interactiva construida con **Streamlit** diseñada para analizar y procesar el comportamiento de miles de clientes frente a las campañas de captación de depósitos a plazo fijo de una institución financiera.

El objetivo del tablero es traducir grandes volúmenes de datos crudos en directrices estratégicas comerciales y de negocio, optimizando la toma de decisiones sin necesidad de recurrir a modelos predictivos complejos.

---

## 🚀 Características Principales

El dashboard está estructurado en tres módulos principales de navegación mediante la barra lateral (`st.sidebar`):

1. **Home:** Presentación institucional del proyecto, objetivos del negocio, descripción del dataset y herramientas tecnológicas utilizadas.
2. **Carga del Dataset:** Interfaz dinámica protegida con memoria global (`st.session_state`) que permite procesar archivos planos (`.csv` con separación por punto y coma). Desbloquea un análisis profundo de 10 pestañas (`st.tabs`):
   * Estadísticas descriptivas y clasificación de variables automática (numéricas vs. categóricas).
   * Detección avanzada de datos faltantes y valores atípicos (códigos centinela como el valor 999).
   * Visualizaciones optimizadas con **Matplotlib** y **Seaborn** (histogramas interactivos con ajuste de barras mediante `st.slider`, diagramas de caja y mapas de calor de correlación).
   * Filtros analíticos dinámicos basados en parámetros seleccionados por el usuario (`st.selectbox` y `st.multiselect`).
3. **Conclusiones Finales:** Un panel ejecutivo cerrado que resume los 5 hallazgos operativos más críticos del análisis exploratorio, orientados 100% a la rentabilidad y optimización del call center.

---

## 🛠️ Arquitectura de Código (POO)

El proyecto implementa principios de **Programación Orientada a Objetos (POO)** mediante la clase modular `DataAnalyzer`, encargada de encapsular de forma limpia y eficiente:
* La lógica de separación de tipos de datos.
* El procesamiento de medidas de tendencia central y dispersión.
* El renderizado automatizado de gráficos complejos reduciendo la redundancia en el script principal de la interfaz.

---

## 📸 Capturas de la Aplicación

A continuación se muestran algunas secciones del dashboard interactivo en funcionamiento:

| Módulo de Presentación (Home) | Análisis de Distribuciones Interactivas |
|---|---|
| ![Home Screen](https://via.placeholder.com/400x250?text=Captura+Home+Streamlit) | ![Histograma Dinámico](https://via.placeholder.com/400x250?text=Captura+Histograma+Slider) |

| Matriz de Correlación (Heatmap) | Conclusiones y Toma de Decisiones |
|---|---|
| ![Mapa de Calor](https://via.placeholder.com/400x250?text=Captura+Heatmap+Seaborn) | ![Conclusiones](https://via.placeholder.com/400x250?text=Captura+Sección+Conclusiones) |

> *Nota: Reemplaza los enlaces de marcador de posición de arriba con las URLs de tus capturas reales una vez alojadas en GitHub.*

---

## 💻 Instrucciones de Ejecución

Sigue estos pasos para clonar el repositorio y ejecutar la aplicación de forma local en tu computadora:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/ProyectoFinal.git](https://github.com/tu-usuario/ProyectoFinal.git)
cd ProyectoFinal
