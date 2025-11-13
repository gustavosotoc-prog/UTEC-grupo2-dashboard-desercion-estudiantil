# UTEC-grupo2-dashboard-desercion-estudiantil
Es un repositorio para el proyecto final del grupo 2 del programa "Programación en Python"
# 📊 UTEC - Grupo 2: Dashboard de Deserción Estudiantil

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/built%20with-streamlit-orange)
![Pandas](https://img.shields.io/badge/data-pandas-green)
![Plotly](https://img.shields.io/badge/charts-plotly-purple)

Este proyecto fue desarrollado por **Grupo 2** de **UTEC** como parte de un curso de Python. Proporciona un dashboard interactivo para analizar la situación académica universitaria y factores relacionados con la deserción estudiantil.

---

## 🚀 Características Principales

- ✅ **5 Secciones de Análisis** con visualizaciones especializadas
- ✅ **Filtros Interactivos** por múltiples variables demográficas y académicas
- ✅ **20+ Visualizaciones** (gráficos de barras, pie, líneas, scatter)
- ✅ **Métricas en Tiempo Real** según filtros aplicados
- ✅ **Diseño Responsivo** con layout de múltiples columnas

---

## 📸 Screenshots

| Dashboard Principal | Análisis Demográfico | Situación Académica |
|----------|----------------|------------------|
| ![UI Screenshot](img/screenshot_ui.png) | ![Demo](img/screenshot_demo.png) | ![Academic](img/screenshot_academic.png) |

---

## 🗂 Estructura del Proyecto

```
├── proyecto_python.py           # Aplicación principal Streamlit
├── nuevadata1.xlsx              # Dataset con datos estudiantiles
├── requirements.txt             # Dependencias Python
├── img/                         # Capturas de pantalla
└── README.md                    # Documentación del proyecto
```

---

## 📊 Secciones del Dashboard

### 1️⃣ **Perfil Sociodemográfico del Estudiante**
Análisis de características demográficas:
- Distribución por **estado civil**
- Análisis por **género** (Masculino/Femenino)
- **Región de nacimiento**
- Estudiantes que **estudian fuera de su residencia**
- **Necesidades educativas especiales**
- Estado de **deuda** financiera
- **Edad al momento de inscripción**

**Filtros disponibles:**
- Estado Civil (multiselect)
- Género (multiselect)
- Estudia fuera de residencia (multiselect)

---

### 2️⃣ **Perfil Académico de Ingreso**
Evaluación de características al ingresar:
- **Distribución por rango de notas** de ingreso (9.5-19)
- **Nivel educativo al ingreso**
- Estudiantes por **facultad** (con código alfabético)
- **Modalidad de postulación**

**Filtros disponibles:**
- Nota de ingreso (slider numérico)
- Facultad (multiselect)

---

### 3️⃣ **Perfil Académico de Estudio**
Análisis del desempeño durante los estudios:
- **Distribución de notas promedio** (1er y 2do año)
- **Número de cursos aprobados** por año
- **Situación académica actual** (Graduado/Desertor/En curso)

**Filtro disponible:**
- Número de cursos aprobados en 1er año (slider)

---

### 4️⃣ **Situación Académica por Variables Demográficas**
Relación entre factores demográficos y resultados académicos:
- Situación académica por **estado civil**
- Situación académica por **género**
- Situación académica por **región**
- Situación académica por **estudia fuera de residencia**
- Situación académica por **rango de edad al inscribirse**

**Métricas calculadas:**
- % de Graduados
- % de Desertores
- % En curso

---

### 5️⃣ **Situación Académica por Variables Académicas**
Relación entre factores académicos y deserción:
- Situación por **facultad**
- Situación por **nivel educativo de ingreso**
- Situación por **cursos aprobados** (1er y 2do año)
- **Edad vs cantidad de desertores** (scatter plot)
- Situación por **rango de nota de ingreso**

**Filtro disponible:**
- Nota de ingreso (slider)

---

## 🧪 Instrucciones de Instalación

### 1. Validar instalación de Python
Asegúrate de tener **Python 3.8+** instalado:

```bash
python --version
```

### 2. Crear entorno virtual
En la raíz del proyecto ejecuta:

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**En Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**En Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**En macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 📦 Dependencias Principales

```txt
streamlit==1.32.0
pandas==2.2.0
matplotlib==3.8.0
numpy==1.26.0
seaborn==0.13.0
plotly==5.18.0
openpyxl==3.1.2
```

---

## ▶️ Cómo Usar el Dashboard

### 1. Preparar los datos

Asegúrate de que el archivo `nuevadata1.xlsx` esté en la ruta correcta. Si necesitas cambiar la ruta, edita la línea 16 del código:

```python
datos = pd.read_excel(r"RUTA_A_TU_ARCHIVO\nuevadata1.xlsx", sheet_name="Sheet1")
```

### 2. Ejecutar la aplicación

```bash
streamlit run proyecto_python.py
```

O con la ruta completa:

```bash
streamlit run "C:\Users\TU_USUARIO\ruta\al\proyecto\proyecto_python.py"
```

### 3. Navegar por el Dashboard

1. 🌐 Se abrirá automáticamente en `http://localhost:8501`
2. 🎯 Usa el **menú lateral izquierdo** para seleccionar la sección
3. 🔧 Aplica **filtros** según tus necesidades
4. 📈 Observa cómo las visualizaciones se actualizan en tiempo real

---

## 🎨 Tipos de Visualizaciones

| Tipo de Gráfico | Librería Usada | Uso Principal |
|-----------------|----------------|---------------|
| **Gráfico de Pie** | Plotly & Matplotlib | Proporciones y porcentajes |
| **Gráfico de Barras** | Seaborn & Matplotlib | Comparaciones categóricas |
| **Gráfico de Barras Apiladas** | Matplotlib & Pandas | Comparación de grupos múltiples |
| **Gráfico de Líneas** | Seaborn | Tendencias a lo largo de rangos |
| **Scatter Plot** | Matplotlib | Relación entre variables numéricas |
| **Barras Horizontales** | Matplotlib | Rankings o listas ordenadas |
| **Countplot** | Seaborn | Frecuencias de categorías |

---

## 🔍 Análisis Técnico del Código

### **Arquitectura del Dashboard**

```
Streamlit UI (proyecto_python.py)
│
├── Configuración Inicial
│   ├── st.set_page_config() → Layout y tema
│   └── Carga de datos (Excel)
│
├── Sidebar Navigation
│   ├── Selector de sección
│   └── Filtros dinámicos por sección
│
└── Secciones (5 pestañas)
    ├── Pestaña 1: Perfil Sociodemográfico
    ├── Pestaña 2: Perfil Académico Ingreso
    ├── Pestaña 3: Perfil Académico Estudio
    ├── Pestaña 4: Situación por Demografía
    └── Pestaña 5: Situación por Academia
```

---

### **Componentes Clave del Código**

#### 1. **Configuración de Página**
```python
st.set_page_config(
    page_title="Dashboard pestañas",
    page_icon="📊",
    layout="wide",  # Usa todo el ancho disponible
    initial_sidebar_state="expanded",  # Sidebar visible por defecto
)
```

#### 2. **Carga de Datos**
```python
datos = pd.read_excel(
    r"C:\Users\MAURICIO\Desktop\...\nuevadata1.xlsx", 
    sheet_name="Sheet1"
)
```

#### 3. **Sistema de Navegación**
```python
char_type = st.sidebar.selectbox(
    "Selecciona el tipo de visualizacion",
    [
        "Perfil sociodemográfico del estudiante",
        "Perfil académico de ingreso",
        # ... más opciones
    ],
)
```

#### 4. **Filtros Interactivos**
```python
# Multiselect para múltiples opciones
seleccion_genero = st.sidebar.multiselect(
    "Genero, 1=Masculino; 0=Femenino",
    options=datos["Genero"].unique(),
    default=datos["Genero"].unique(),
)

# Slider para valores numéricos
nota_ing = st.sidebar.slider(
    "Nota de ingreso",
    min_value=float(datos["Nota de ingreso"].min()),
    max_value=float(datos["Nota de ingreso"].max()),
    step=0.1,
    value=float(datos["Nota de ingreso"].min()),
)
```

#### 5. **Filtrado de DataFrame**
```python
datos_filtrados = datos[
    (datos["Estado Civil"].isin(seleccion_estado_civil)) & 
    (datos["Genero"].isin(seleccion_genero)) &
    (datos["Estudia fuera de su lugar de residencia"].isin(seleccion_fuera_residencia))
]
```

#### 6. **Sistema de Columnas**
```python
# Layout de 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    # Contenido columna 1
    st.markdown("**Título del Gráfico**")
    # Código de visualización

with col2:
    # Contenido columna 2
    
with col3:
    # Contenido columna 3
```

#### 7. **Métricas Dinámicas**
```python
colA, colB, colC, colD = st.columns(4)
total = len(datos_filtrados)
pct_grad = datos_filtrados["Variable_Objetivo"].eq("Graduado").mean() * 100

with colA:
    st.metric("Total estudiantes", f"{total:,}")
with colB:
    st.metric("% Graduados", f"{pct_grad:.1f}%")
```

---

### **Técnicas de Visualización Implementadas**

#### **1. Gráfico Pie con Plotly**
```python
cant = datos_filtrados["Estado Civil"].value_counts()
fig = go.Figure([go.Pie(
    values=cant.values, 
    labels=cant.index, 
    hole=0.3  # Donut chart
)])
fig.update_layout(height=280, margin=dict(t=20, b=20, l=20, r=20))
st.plotly_chart(fig, use_container_width=True)
```

**Ventajas:**
- Interactivo (hover, zoom)
- Responsive automático
- Exportable

#### **2. Gráfico de Barras con Matplotlib**
```python
fig, ax = plt.subplots(figsize=(4, 3.4))
cant.plot(kind="bar", ax=ax, color="skyblue")
ax.set_xlabel("Género", fontsize=8)
ax.set_ylabel("Cantidad", fontsize=8)

# Agregar etiquetas sobre las barras
for bar in ax.containers:
    ax.bar_label(bar, fmt="%.0f", fontsize=8)
    
plt.tight_layout()
st.pyplot(fig)
plt.close()  # Liberar memoria
```

#### **3. Countplot con Seaborn**
```python
fig, ax = plt.subplots(figsize=(4, 3))
sns.countplot(
    data=datos_filtrados, 
    x="Region", 
    color="royalblue", 
    ax=ax
)
for bar in ax.containers:
    ax.bar_label(bar, fmt="%.0f", fontsize=8)
st.pyplot(fig)
```

#### **4. Barras Agrupadas con Plotly**
```python
df_pivot = datos_filtrados.groupby([
    "Variable_Objetivo", 
    "Estado Civil"
]).size().unstack()

df_long = df_pivot.reset_index().melt(
    id_vars="Variable_Objetivo", 
    var_name="Estado Civil", 
    value_name="Cantidad"
)

fig = px.bar(
    df_long,
    x="Estado Civil",
    y="Cantidad",
    color="Variable_Objetivo",
    barmode="group",  # Barras lado a lado
    text="Cantidad",
)
st.plotly_chart(fig, use_container_width=True)
```

#### **5. Categorización de Rangos**
```python
bins = [9.5, 11, 13, 15, 17, 19]
labels = ["9.5-11", "11.1-13", "13.1-15", "15.1-17", "17.1-19"]

rango_notas = pd.cut(
    datos_filtrados["Nota de ingreso"],
    bins=bins,
    labels=labels,
    include_lowest=True,  # Incluye el límite inferior
)
```

#### **6. Gráfico de Líneas con Anotaciones**
```python
fig, ax = plt.subplots(figsize=(6, 4))
sns.lineplot(
    data=df_rangos,
    x="RANGO_EDAD",
    y="CANTIDAD",
    hue="Variable_Objetivo",
    marker="o",
    palette="Set2",
    ax=ax,
)

# Agregar valores sobre los puntos
for variable, datos_var in df_rangos.groupby("Variable_Objetivo"):
    for x, y in zip(datos_var["RANGO_EDAD"], datos_var["CANTIDAD"]):
        ax.text(x, y + 0.8, str(int(y)), 
                ha="center", va="bottom", fontsize=6)
```

---

## 📈 Estructura de Datos Esperada

El archivo `nuevadata1.xlsx` debe contener las siguientes columnas:

### **Variables Demográficas:**
- `Estado Civil`: Categoría (Soltero, Casado, etc.)
- `Genero`: Binario (0 = Femenino, 1 = Masculino)
- `Region`: Categoría (A, B, C, etc.)
- `Estudia fuera de su lugar de residencia`: Binario (0 = No, 1 = Si)
- `Necesidades educativas especiales`: Categoría
- `Deudor`: Binario (0 = Sin deuda, 1 = Con deuda)
- `Edad al momento de la inscripcion.`: Numérico (17-40)

### **Variables Académicas:**
- `Nota de ingreso`: Numérico (9.5-19.0)
- `Facultad`: Categoría
- `Nivel_educativo_ingreso`: Categoría
- `Modalidad de postulación`: Categoría
- `Numero_cursos_aprobados_primer_año`: Entero (0-15)
- `Numero_cursos_aprobados_segundo_año`: Entero (0-15)
- `Nota_promedio_primer_año`: Numérico (0-20)
- `Nota_promedio_segundo_año`: Numérico (0-20)

### **Variable Objetivo:**
- `Variable_Objetivo`: Categoría ("Graduado", "Desertor", "En curso")

---

## 🎓 Conceptos de Python Aplicados

| Concepto | Aplicación en el Proyecto |
|----------|---------------------------|
| **DataFrames (Pandas)** | Manipulación de datos tabulares |
| **Groupby & Aggregation** | Agrupación por categorías |
| **Filtering** | Aplicar múltiples filtros con operadores lógicos |
| **Pivot Tables** | Transformar datos para visualización |
| **Value Counts** | Contar frecuencias de categorías |
| **Categorical Data** | `pd.cut()` para crear rangos |
| **Conditional Logic** | `if-elif-else` para navegación |
| **List Comprehensions** | Generar etiquetas alfabéticas |
| **String Formatting** | F-strings para métricas |
| **Context Managers** | Manejo de recursos de Matplotlib |

---

## 🔧 Funciones Clave de Streamlit

```python
# Layout
st.set_page_config()          # Configuración global
st.columns()                  # Dividir en columnas
st.sidebar                    # Barra lateral

# Widgets de entrada
st.selectbox()                # Selector único
st.multiselect()              # Selector múltiple
st.slider()                   # Deslizador numérico

# Mostrar contenido
st.title()                    # Título principal
st.markdown()                 # Texto con formato
st.metric()                   # Métricas destacadas
st.pyplot()                   # Gráficos Matplotlib
st.plotly_chart()             # Gráficos Plotly

# Manejo de estados
st.info()                     # Mensaje informativo
st.warning()                  # Mensaje de advertencia
st.stop()                     # Detener ejecución
```

---

## 💡 Mejoras Posibles

### **Funcionalidades:**
1. ✨ **Exportar reportes** a PDF/Excel
2. 📊 **Comparador de cohortes** (año de ingreso)
3. 🤖 **Modelo predictivo** de deserción con ML
4. 📧 **Sistema de alertas** para riesgo de deserción
5. 🔄 **Actualización automática** de datos

### **Visualizaciones:**
1. 📍 **Mapa geográfico** de origen de estudiantes
2. 🎯 **Heatmap** de correlaciones
3. 📊 **Dashboard ejecutivo** con KPIs principales
4. 🌊 **Sankey diagram** de flujo estudiantil
5. ⏱️ **Serie temporal** de deserción por semestre

### **Técnicas:**
1. 🗃️ **Base de datos** (PostgreSQL/SQLite)
2. ⚡ **Caché de datos** con `@st.cache_data`
3. 🎨 **Temas personalizados** con CSS
4. 🔐 **Sistema de autenticación**
5. 🌐 **Deploy en la nube** (Streamlit Cloud, Heroku)

---

## 👥 Team Members - Grupo 2

- Mauricio
- Thaty
- [Agregar más integrantes]

---

## 📚 Recursos de Aprendizaje

### **Documentación Oficial:**
- 📖 [Streamlit Docs](https://docs.streamlit.io)
- 🐼 [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- 📊 [Plotly Python](https://plotly.com/python/)
- 🎨 [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- 📉 [Matplotlib Guide](https://matplotlib.org/stable/users/index.html)

### **Tutoriales Recomendados:**
- 🎥 Streamlit: Data Apps in Python
- 📘 Pandas for Data Analysis
- 🎓 Data Visualization with Python

---

## 🐛 Solución de Problemas Comunes

### **Error: "No module named 'openpyxl'"**
```bash
pip install openpyxl
```

### **Error: "File not found"**
Verifica la ruta del archivo Excel:
```python
# Usa ruta absoluta o relativa correcta
datos = pd.read_excel("nuevadata1.xlsx")  # Si está en el mismo directorio
```

### **Gráficos no se muestran**
Asegúrate de cerrar las figuras de Matplotlib:
```python
st.pyplot(fig)
plt.close()  # Importante para liberar memoria
```

### **Dashboard lento**
Implementa caché de datos:
```python
@st.cache_data
def cargar_datos():
    return pd.read_excel("nuevadata1.xlsx")
```

---

## 📄 Licencia

Este proyecto fue desarrollado con fines académicos para UTEC.

---

## 🤝 Contribuciones

Si deseas mejorar este proyecto:
1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit tus cambios: `git commit -m 'Agregar nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

## 📞 Contacto

Para preguntas o sugerencias sobre el proyecto, contacta al **Grupo 2 de UTEC**.

---

**⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub!**
