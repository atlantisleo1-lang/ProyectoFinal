import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import io

st.set_page_config(page_title="Proyecto Final")
class DataAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe
        
    def clasificar_variables(self):
        x = []
        y = []
        for a in list(self.df.columns):
            if self.df[a].dtype in ['int64', 'float64']:
                x.append(a)
            else:
                y.append(a)
        return x, y

    def obtener_estadisticas(self):
        return self.df.describe()

    def plot_histograma(self, columna, bins=30):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=self.df, x=columna, bins=bins, kde=True, color="#4CB391", ax=ax)
        ax.set_title(f"Distribución de {columna}", fontsize=14)
        ax.set_xlabel(columna, fontsize=12)
        ax.set_ylabel("Frecuencia (Cantidad de clientes)", fontsize=12)
        return fig

secciones = st.sidebar.selectbox("Secciones", ["Home", "Carga del dataset", "Conclusiones Finales"])
if secciones == "Home":
    st.title("Análisis Exploratorio de Datos: Campaña de Telemarketing Bancario")
    st.subheader("Primer proyecto de portafolio profesional")
    
    col_texto, col_foto = st.columns([2, 1])
    with col_texto:
        st.write("**Nombre Completo:** Leonel Eberth Escalante Izquierdo")
        st.write("**Curso / Especialización:** Especialización en Python for Analytics")
        st.write("**Año:** 2026")
        st.write("**Edad:** 26 años")
        
    with col_foto:
        st.image("logo.png", width=150) 
        
    col_izq, col_dmc, col_medio, col_py, col_der = st.columns([1.5, 1.2, 0.5, 1, 1.5])
    
    with col_dmc:
        st.image("logodmc.png", width=160)
    with col_py:
        st.image("python.png", width=90) 
        
    st.divider() 

    # Breve descripción del objetivo del análisis (SIMPLIFICADA)
    st.markdown("### Objetivo del Análisis")
    st.write("""
    El objetivo de este proyecto es entender por qué algunos clientes aceptan un producto financiero (como un depósito a plazo fijo) y otros lo rechazan cuando el banco los llama por teléfono. 
    Al explorar los datos de forma interactiva, buscaremos patrones clave, como la edad, el tipo de trabajo o la situación económica del país,para ayudar al banco a tomar mejores decisiones comerciales, dejar de perder tiempo en llamadas innecesarias y hacer que sus futuras campañas sean mucho más exitosas.
    """)
    
    # Breve explicación del dataset (SIMPLIFICADA)
    st.markdown("### Explicación del Dataset")
    st.write("""
    Este conjunto de datos es, en esencia, un registro histórico de miles de llamadas telefónicas que hizo un banco a distintas personas. 
    El archivo contiene tres tipos principales de información: el perfil del cliente (su edad, profesión, nivel de estudios), detalles de la llamada (cuánto duró, si fue a celular o fijo) y el contexto de la economía en ese momento. 
    La columna más importante de todas es la variable final (llamada 'y'), que es la meta de nuestro estudio, ya que nos indica simplemente si el cliente dijo "sí" o "no" a la oferta del banco.
    """)
    
    # Tecnologías utilizadas (Mantenemos la parte técnica aquí para el profesor)
    st.markdown("### Tecnologías y Herramientas Usadas:")

    st.markdown("""
    * **Streamlit:** Construcción de la interfaz gráfica interactiva, implementación de widgets dinámicos (filtros, selectores, botones de carga) y gestión de memoria global con session_state para preservar los datos analizados entre secciones.
    * **Pandas:** Carga de archivos planos, manipulación y limpieza de datos, indexación y generación de tablas para resumir la información de los clientes.
    * **NumPy:** Soporte en el procesamiento de datos numéricos y operaciones lógicas, facilitando la detección de valores faltantes y códigos ocultos.
    * **Matplotlib y Seaborn:** Diseño de las visualizaciones gráficas, incluyendo diagramas de caja (boxplots), gráficos de barras, histogramas y mapas de calor para ver la relación entre variables.
    * **Programación Orientada a Objetos (POO):** Implementación de la clase `DataAnalyzer` para mantener el código ordenado, agrupando los cálculos matemáticos y la creación de gráficos en un solo lugar.
    * **Lógica de Control:** Uso de condicionales (if/else) y bucles para garantizar que la aplicación web funcione de manera fluida y sin errores.
    """)

elif secciones == "Carga del dataset":
    archivo = st.file_uploader("Sube un archivo.csv")  
    if archivo is not None:
        df_temp = pd.read_csv(archivo, sep=';')
        st.session_state['datos_cargados'] = True
        st.session_state['mi_clase_guardada'] = DataAnalyzer(df_temp)

    if 'mi_clase_guardada' in st.session_state:
        analizador = st.session_state['mi_clase_guardada']
        df = analizador.df 
        st.write("✅ Archivo cargado correctamente")
        
        if st.checkbox("Mostrar todas las filas del dataset original"):
            st.dataframe(df)
        else:
            st.write(df.head())
            st.write(df.shape)

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, = st.tabs(["Información general del dataset", "Clasificación de variables", "Estadísticas descriptivas", "Análisis de valores faltantes","Distribución de variables numéricas", "Análisis de variables categóricas", "Análisis bivariado (numérico vs categórico)", "Análisis bivariado (categórico vs categórico)", "Análisis basado en parámetros seleccionados", "Hallazgos clave"])
        with tab1:
            st.markdown("### Información general del dataset")
            st.markdown("**1. Resumen .info():**")
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_str = buffer.getvalue()
            st.text(info_str) 
            
            st.markdown("**2. Tipos de datos por variable:**")
            st.dataframe(df.dtypes) 
            
            st.markdown("**3. Conteo de valores nulos:**")
            conteo_nulos = df.isin(['unknown', 999 , np.nan, None, '']).sum()
            st.dataframe(conteo_nulos)
            total_nulos = df.isin(['unknown', 999, np.nan, None, '']).sum().sum()
            st.metric(label="Total de valores nulos en el dataset", value=total_nulos)
            st.markdown("**Nota:**")
            st.write("En la columna de pdays(Días desde la última gestión), el valor 999 no representa un conteo real de días, sino que es un código de sistema (valor centinela) programado en la base de datos para indicar: *Que este cliente NUNCA ha sido contactado en campañas anteriores.*")

        with tab2:
            
            cols_num, cols_cat = analizador.clasificar_variables()
            
            df_num = pd.DataFrame(cols_num, columns=["Variables Numéricas"])
            df_cat = pd.DataFrame(cols_cat, columns=["Variables Categóricas"])
            
            df_num.index = df_num.index + 1
            df_cat.index = df_cat.index + 1
            
            st.success(f"Se encontraron {len(cols_num)} variables numéricas:")
            st.dataframe(df_num)
            
            st.info(f"Se encontraron {len(cols_cat)} variables categóricas:")
            st.dataframe(df_cat)

        with tab3:
            st.markdown("### Estadísticas descriptivas")
            st.markdown("**1. Resumen estadístico (.describe):**")
            st.dataframe(df.describe())
            st.dataframe(analizador.obtener_estadisticas())
            st.markdown("**2. Interpretación de los datos:**")
        
            st.markdown("""
            * **Análisis de la Tasa de Variación del Empleo (emp.var.rate):**
                
                Se seleccionó esta columna porque es el indicador macroeconómico más relevante para entender el contexto de la campaña. La disposición de un cliente a adquirir productos financieros (como préstamos o depósitos) está directamente condicionada por la estabilidad laboral del país en ese momento.
                * **Media vs. Mediana:**La mediana(valor central al ordenar los datos) se sitúa en 1.1, lo que indica que al menos el 50% de las llamadas se realizaron en periodos de estabilidad o crecimiento del empleo. Sin embargo, la media(promedio) cae drásticamente a 0.081. Esto ocurre porque los periodos de recesión arrastran el promedio matemático hacia abajo.
                * **Dispersión(variación):** La variable presenta un rango muy amplio, con un máximo de 1.4 pero un mínimo crítico de -3.4 (indicando una fuerte crisis económica en ciertos meses de la campaña). Su desviación estándar de 1.57 confirma una alta volatilidad en el entorno económico durante el periodo en que el banco intentaba vender sus productos.
                """)
            
        with tab4:
            st.markdown("### Análisis de Valores Faltantes")
            
            conteo_nulos = df.isin(['unknown', 999, np.nan, None, '']).sum()
            conteo_filtrado = conteo_nulos[conteo_nulos > 0].sort_values(ascending=False)
            
            st.dataframe(conteo_filtrado)

            st.markdown("**2. Visualización gráfica:**")
            if not conteo_filtrado.empty:
                fig, ax = plt.subplots(figsize=(10, 6))

                sns.barplot(x=conteo_filtrado.values, y=conteo_filtrado.index, ax=ax, palette="viridis")
                ax.set_title("Cantidad de Valores Faltantes por Variable", fontsize=14)
                ax.set_xlabel("Número de registros faltantes", fontsize=12)
                ax.set_ylabel("Variables", fontsize=12)
                st.pyplot(fig)

                st.markdown("**3. Conclusión del análisis:**")
                st.markdown("""              
                * **Credito en Mora (default):** El historial de mora crediticia es la variable con mayor cantidad de datos faltantes ('unknown'). Los encuestados suelen negarse a revelar si tienen deudas sin pagar durante una llamada en frío, o bien, el banco no tiene acceso a ese historial si la persona no es un cliente previo. En ciencia de datos, este 'unknown' no debe borrarse, ya que la negativa a responder suele ser un fuerte indicador predictivo de riesgo.
                * **Nivel educativo (education):** El nivel educativo también presenta un alto volumen de omisiones. Durante las campañas de telemarketing, los operadores tienen un tiempo limitado y priorizan las preguntas directas sobre la venta del producto. Al no ser un dato legalmente obligatorio para ofrecer un depósito a plazo, los operadores (o los mismos clientes) tienden a omitirlo para acelerar la gestión.
                * **Días desde la última gestión (pdays):** La gran concentración del valor atípico 999 nos revela que la campaña se enfocó casi en su totalidad en clientes que no habían sido contactados en campañas anteriores. Para futuros análisis de Machine Learning, esta columna no podrá usarse como una variable numérica continua, sino que deberá transformarse en una categoría (ej. "Contactado previamente" vs "No contactado").
                """)
        
        with tab5:
            st.markdown("### Distribución de variables numéricas")
            st.markdown("Análisis de la frecuencia y concentración de los datos mediante histogramas.")
            
            cols_num = df.select_dtypes(include=['number']).columns.tolist()
        
            var_seleccionada = st.selectbox("Selecciona una variable para ver su distribución:", cols_num)
            
            st.markdown("**Ajuste visual:**")
            bins_seleccionados = st.slider("Selecciona el número de barras (bins) del histograma:", min_value=10, max_value=100, value=30, step=5)
            
            st.markdown(f"**Histograma de la variable: {var_seleccionada}**")
            
            fig_hist = analizador.plot_histograma(columna=var_seleccionada, bins=bins_seleccionados)
            st.pyplot(fig_hist)
            
            st.markdown("**Interpretación visual de las variables principales:**")
            st.markdown("""
            Al explorar las distintas variables con el histograma, se observan los siguientes patrones de distribución:
            
            * **Edad (age):** Presenta una distribución que se asemeja a una campana normal, pero con un ligero sesgo hacia la derecha (asimetría positiva). La gran mayoría de los clientes se concentran en el bloque de los 30 a 40 años.
            * **Duración de la llamada (duration):** Tiene un sesgo positivo extremo (cola muy larga hacia la derecha). El histograma muestra que casi todas las llamadas se agrupan en el lado izquierdo (entre 0 y 300 segundos). Los valores que superan los 1000 segundos son visualmente imperceptibles en frecuencia, confirmando que son casos atípicos.
            * **Contactos en campaña (campaign):** Al igual que la duración, el histograma se concentra casi totalmente en los números 1, 2 y 3. La curva cae en picada inmediatamente, demostrando visualmente que la política general es no insistir demasiadas veces con el mismo cliente.
            """)
        with tab6:
            st.markdown("### Análisis de variables categóricas")
            
            cols_cat = df.select_dtypes(exclude=['number']).columns.tolist()
            
            var_cat = st.selectbox("Selecciona una variable categórica para analizar:", cols_cat)
            
            st.markdown(f"**1. Tabla de frecuencias y proporciones de: {var_cat}**")
            
            conteos = df[var_cat].value_counts()
            proporciones = df[var_cat].value_counts(normalize=True) * 100
            
            df_cat_stats = pd.DataFrame({
                'Conteo (Clientes)': conteos,
                'Proporción (%)': proporciones.round(2) # Redondeamos a 2 decimales
            })
            
            st.dataframe(df_cat_stats)
            st.markdown("**2. Gráfico de barras:**")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            sns.countplot(data=df, y=var_cat, order=conteos.index, palette="Set3", ax=ax)

            ax.set_title(f"Distribución de la variable {var_cat}", fontsize=14)
            ax.set_xlabel("Cantidad de clientes", fontsize=12)
            ax.set_ylabel(var_cat, fontsize=12)
            
            st.pyplot(fig)
            
        with tab7:
            st.markdown("### Análisis Bivariado (Numérico vs Categórico)")
            st.markdown("**1. Edad del cliente vs. Aceptación (`age` vs `y`)**")
            
            fig1, ax1 = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df, x='y', y='age', palette="Set1", ax=ax1)
            
            ax1.set_title("Distribución de Edad según el Resultado de la Campaña", fontsize=14)
            ax1.set_xlabel("¿Aceptó el depósito? (y)", fontsize=12)
            ax1.set_ylabel("Edad (age)", fontsize=12)
            
            st.pyplot(fig1)

            st.markdown("**2. Duración de la llamada vs. Aceptación (`duration` vs `y`)**")
            
            fig2, ax2 = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df, x='y', y='duration', palette="Set2", ax=ax2)
            
            ax2.set_title("Duración de la Llamada según el Resultado", fontsize=14)
            ax2.set_xlabel("¿Aceptó el depósito? (y)", fontsize=12)
            ax2.set_ylabel("Duración en segundos (duration)", fontsize=12)
            
            st.pyplot(fig2)

            st.markdown("**3. Conclusiones y hallazgos operativos:**")
            st.markdown("""
            * **El factor Edad (`age` vs `y`):** Al observar las cajas, vemos que la mediana de edad es prácticamente idéntica para quienes aceptan y quienes rechazan (alrededor de los 38-40 años). Sin embargo, la caja de los 'yes' presenta valores atípicos (puntos por encima del bigote superior) mucho más marcados en edades avanzadas (mayores de 60 años). Esto sugiere que, aunque el cliente promedio tiene 40 años, la tercera edad es un nicho altamente receptivo para los depósitos a plazo fijo.
            
            * **La advertencia de la Duración (`duration` vs `y`):** Este gráfico es sumamente revelador. La caja de los 'yes' está significativamente más arriba que la de los 'no'. Es lógico: si un cliente está interesado, hará más preguntas y la llamada durará más. 
            
            """)   
        
        
        with tab8:
            st.markdown("### Análisis Bivariado (Categórico vs Categórico)")

            st.markdown("**1. Nivel Educativo vs. Aceptación (education vs y)**")
            
            st.write("Tabla de contingencia:")
            crosstab_edu = pd.crosstab(df['education'], df['y'])
            st.dataframe(crosstab_edu)
            
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            sns.countplot(data=df, x='education', hue='y', ax=ax1, palette="Set1")
            
            ax1.set_title("Resultados de la Campaña según Nivel Educativo", fontsize=14)
            ax1.set_xlabel("Nivel Educativo (education)", fontsize=12)
            ax1.set_ylabel("Cantidad de clientes", fontsize=12)
            plt.xticks(rotation=45) 
            
            st.pyplot(fig1)

            st.markdown("**2. Medio de Contacto vs. Aceptación (contact vs y)**")
            
            st.write("Tabla de contingencia:")
            crosstab_contact = pd.crosstab(df['contact'], df['y'])
            st.dataframe(crosstab_contact)
            
            fig2, ax2 = plt.subplots(figsize=(8, 5))
            sns.countplot(data=df, x='contact', hue='y', ax=ax2, palette="Set2")
            
            ax2.set_title("Resultados de la Campaña según Medio de Contacto", fontsize=14)
            ax2.set_xlabel("Medio de contacto (contact)", fontsize=12)
            ax2.set_ylabel("Cantidad de clientes", fontsize=12)
            
            st.pyplot(fig2)

            st.markdown("**3. Conclusiones y hallazgos operativos:**")
            st.markdown("""
            * **education vs y:** Visualmente destaca que el grupo con título universitario (university.degree) genera el mayor volumen absoluto de aceptaciones (yes). Sin embargo, también generan una cantidad masiva de rechazos. Esto indica que es un segmento con alto poder adquisitivo y capacidad de ahorro, pero que requiere un argumento de venta mucho más sólido o personalizado por parte del asesor financiero.
            
            * **contact vs y:** El gráfico de medio de contacto revela una ventaja operativa aplastante. Los contactos realizados a teléfonos celulares (cellular) no solo duplican en volumen a los teléfonos fijos (telephone), sino que la proporción de aceptaciones es visiblemente superior. Esto es un reflejo del comportamiento moderno: contactar a un teléfono fijo (generalmente en horario laboral) genera más fricción y rechazo rápido, mientras que el celular permite una comunicación más personal y directa.
            """)

        with tab9:
            st.markdown("### Análisis Dinámico basado en Parámetros")
           
            st.markdown("**1. Visor de datos a la carta (Uso de Multiselect):**")
            
            todas_las_columnas = df.columns.tolist()
            
            columnas_elegidas = st.multiselect(
                "Selecciona las columnas que deseas visualizar en la tabla:",
                options=todas_las_columnas,
                default=["age", "job", "y"] )
            

            if columnas_elegidas:
                # Mostramos los primeros 1000 registros para que la app cargue rápido
                st.dataframe(df[columnas_elegidas].head(1000)) 
            else:
                st.warning("Por favor, selecciona al menos una columna para visualizar los datos.")

            st.markdown("---")

            st.markdown("**2. Motor de promedios dinámico (Uso de Selectbox):**")
            st.markdown("Selecciona una variable de texto para agrupar a los clientes y descubrir el promedio de sus datos numéricos.")

            cols_cat = df.select_dtypes(exclude=['number']).columns.tolist()
            cols_num = df.select_dtypes(include=['number']).columns.tolist()

            var_agrupacion = st.selectbox("Agrupar clientes por:", cols_cat)

            if var_agrupacion:
                df_agrupado = df.groupby(var_agrupacion)[cols_num].mean()
                
                st.write(f"Promedios calculados para cada categoría de {var_agrupacion}:")
                st.dataframe(df_agrupado)
                
            st.markdown("**3. ¿Qué logramos con este análisis?**")
            st.markdown("""
            * **Autonomía del usuario:** Mediante el componente multiselect, evitamos saturar la pantalla con decenas de columnas, permitiendo al analista enfocarse únicamente en las variables relevantes para su hipótesis.
            * **Descubrimiento ágil de patrones:** El agrupador dinámico con selectbox funciona como una tabla dinámica de Excel automatizada. Por ejemplo, al agrupar por estado civil (marital), podemos descubrir en un solo clic si los clientes casados tienen un promedio de edad mayor o si son contactados con mayor frecuencia que los solteros.
            """)

        with tab10:
            st.markdown("### Hallazgos Clave y Resumen del EDA")
            st.markdown("Esta sección consolida los descubrimientos de negocio más importantes obtenidos tras el análisis exploratorio de la base de datos.")

            st.markdown("**1. Visualización Resumen (Mapa de Calor de Correlaciones):**")
            st.markdown("El siguiente mapa muestra cómo se relacionan linealmente las variables numéricas entre sí. Los colores cálidos (rojos) indican correlación positiva fuerte, y los fríos (azules), correlación negativa.")
            
            cols_num = df.select_dtypes(include=['number'])
            
            fig, ax = plt.subplots(figsize=(12, 8))
            
            correlacion = cols_num.corr()
            
            sns.heatmap(correlacion, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
            
            st.pyplot(fig)

            st.markdown("**2. Insights Principales derivados del EDA:**")
            
            st.markdown("""
            Tras cruzar y analizar las variables demográficas, operativas y macroeconómicas, se destacan los siguientes 4 hallazgos críticos para el negocio:

            * **Estrategia enfocada en "Mercado Frío":** El análisis de la variable pdays reveló una saturación del valor artificial 999. Esto demuestra que la campaña actual se diseñó para captar clientes completamente nuevos o no contactados históricamente, ignorando la base de clientes previamente gestionados.
            * **El peso del contexto macroeconómico (emp.var.rate):** Se comprobó visual y estadísticamente que la tasa de variación de empleo afecta la decisión del cliente. Quienes aceptaron la campaña tienden a concentrarse en periodos de tasas más bajas o negativas, sugiriendo que el producto (depósito a plazo) funciona como un "refugio seguro" en tiempos de incertidumbre económica.
            * **Supremacía del canal móvil (contact):** El análisis bivariado categórico demostró que contactar a los prospectos mediante teléfono celular (cellular) no solo duplica el volumen de alcance frente al teléfono fijo, sino que genera una proporción de conversión (aceptación) significativamente mayor, marcando una clara directriz para futuras campañas.
           """)
    else:
        st.info("Sube un archivo.csv") 

elif secciones == "Conclusiones Finales":
    if 'datos_cargados' not in st.session_state or not st.session_state['datos_cargados']:
        st.warning("Debes subir el archivo CSV en la sección 'Carga del dataset' para desbloquear los hallazgos y decisiones.")
    else:
        st.title("Conclusiones y Toma de Decisiones")
        st.write("Con base en los análisis exploratorios realizados en las distintas fases del proyecto, se establecen las siguientes 5 directrices operativas:")

        st.markdown("""
        ### 1. Basado en el Análisis de Valores Faltantes (Ítem 4)
        * **Hallazgo Operativo:** La revisión de nulos y atípicos demostró una concentración absoluta del valor 999 en la variable pdays, confirmando que casi toda la base corresponde a clientes sin contacto previo ("mercado frío"). Además, datos como default (mora) tienen alta tasa de omisión.
        * **Toma de Decisión:** Se debe reestructurar la adquisición de bases de datos. Es financieramente ineficiente dedicar todo el call center a prospectos fríos. Marketing debe adquirir listas pre-calificadas o destinar al menos un 30% del esfuerzo operativo a campañas de retención o "retargeting" con clientes que ya tengan historial en el banco.

        ### 2. Basado en el Análisis de Variables Categóricas (Ítem 6)
        * **Hallazgo Operativo:** Al analizar las proporciones de la variable objetivo (y), se descubrió un desbalance de clases masivo (la inmensa mayoría rechaza la campaña).
        * **Toma de Decisión:** Para reducir los costos hundidos del call center por llamadas fallidas, se debe implementar un filtro de prospectos más estricto antes de iniciar el marcado. No se debe llamar a todos por igual; se priorizarán los segmentos con mayor proporción de respuestas positivas detectados en la tabla de frecuencias.

        ### 3. Basado en el Análisis Bivariado Numérico vs Categórico (Ítem 7)
        * **Hallazgo Operativo:** El cruce de age vs y mediante diagramas de caja demostró que, aunque la mediana de edad es de casi 40 años para ambos grupos, las aceptaciones (yes) tienen una fuerte presencia (valores atípicos) en rangos de edad avanzada (tercera edad).
        * **Toma de Decisión:** Lanzar una sub-campaña focalizada exclusivamente en clientes mayores de 60 años. Para este segmento, se asignarán los asesores mejor calificados y se utilizará un guion centrado en la "seguridad y respaldo" de los ahorros, simplificando los trámites para evitar barreras tecnológicas.

        ### 4. Basado en el Análisis Bivariado Categórico vs Categórico (Ítem 8)
        * **Hallazgo Operativo:** Al comparar el medio de contacto (contact) contra el resultado (y), se evidenció que los teléfonos celulares (cellular) no solo dominan en volumen, sino que su proporción de éxito frente al teléfono fijo (telephone) es operativamente superior.
        * **Toma de Decisión:** Migrar inmediatamente los recursos de comunicación al canal móvil. Cualquier nueva lista de leads comprada por el banco debe tener como requisito obligatorio un número celular válido, permitiendo además incorporar estrategias previas por SMS para "calentar" al prospecto antes de la llamada.

        ### 5. Basado en el Análisis Dinámico por Parámetros (Ítem 9)
        * **Hallazgo Operativo:** La herramienta de agrupación dinámica permitió descubrir que las medias financieras y sociodemográficas cambian drásticamente al agrupar a los clientes por diferentes variables categóricas (ej. estado civil o trabajo), revelando "micro-nichos" que pasan desapercibidos en análisis estáticos.
        * **Toma de Decisión:** Abandonar el modelo de campañas masivas de "talla única". Al dotar a los supervisores de ventas con este dashboard interactivo, pueden detectar nichos hiper-específicos en tiempo real y adaptar la oferta de tasas de interés del depósito a plazo según el perfil agrupado, maximizando la agilidad comercial.
        """)