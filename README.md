
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
<img width="1920" height="1080" alt="Captura de pantalla 2026-05-18 213114" src="https://github.com/user-attachments/assets/7a93ebf7-6351-45d6-a6f5-60e92cdd3372" />
<img width="1920" height="1080" alt="Captura de pantalla 2026-05-18 213128" src="https://github.com/user-attachments/assets/785a599e-bef4-481f-b3d9-82bd14b06baa" />
<img width="1920" height="1080" alt="Captura de pantalla 2026-05-18 213139" src="https://github.com/user-attachments/assets/9d4715a9-df84-4872-bd29-eb6ae93c330b" />

---

## 💻 Instrucciones de Ejecución

1.- Entrar al link de streamlink: https://proyectofinal-nxg7tt9xvftdwge2mhendp.streamlit.app/
2.- descargar el DATASET:  BankMarketing.csv que esta en el github
3.- Subir el archivo.csv al proyecto
4.- Evaluar(poner 20)
