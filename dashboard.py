import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
st.set_page_config(
    page_title="Dashboard pestañas",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Dashboard Situación académica universitaria")
#st.markdown("Explora la data de situación académica")

datos = pd.read_excel(r"nuevadata1.xlsx", sheet_name="Sheet1")

# PESTAÑAS
st.sidebar.header("Navegación")
char_type = st.sidebar.selectbox(
    "Selecciona el tipo de visualizacion",
    [
        "Perfil sociodemográfico del estudiante",
        "Perfil académico de ingreso",
        "Perfil académico de estudio",
        "Situación académica por variables demográficas",
        "Situación académica por variables académicas"
    ],
)
st.sidebar.markdown("---")

# ====== PESTAÑA 1: PERFIL SOCIODEMOGRÁFICO ======

if char_type=="Perfil sociodemográfico del estudiante":
    st.sidebar.markdown("### Filtros")
           
    seleccion_estado_civil = st.sidebar.multiselect(
    "Estado Civil",
    options=datos["Estado Civil"].unique(),
    default=datos["Estado Civil"].unique(),
    )

    seleccion_genero= st.sidebar.multiselect(
    "Genero, , 1=Masculino; 0= Femenino",
    options=datos["Genero"].unique(),
    default=datos["Genero"].unique(),
    )

    seleccion_fuera_residencia= st.sidebar.multiselect(
    "Estudian fuera de su residencia, , 1=SI; 0= NO",
    options=datos["Genero"].unique(),
    default=datos["Genero"].unique(),
    )
       
    datos_filtrados = datos[
     (datos["Estado Civil"].isin(seleccion_estado_civil)) & (datos["Genero"].isin(seleccion_genero))&(datos["Estudia fuera de su lugar de residencia"].isin(seleccion_fuera_residencia))
    ]
    #st.write(datos_filtrados)
    st.metric("Estudiantes filtrados", len(datos_filtrados))
 
    #Fila 1: 3 gráficos
    col1, col2, col3 = st.columns(3)
#GRAFICANDO GRAFICO PIE  ESTUDIANTES POR ESTADO CIVIL
    with col1:
        st.markdown("**Estudiantes por estado civil**")
        cant = datos_filtrados["Estado Civil"].value_counts()
        fig = go.Figure([go.Pie(values=cant.values, labels=cant.index, hole=0.3)])
        fig.update_layout(
            height=280, margin=dict(t=20, b=20, l=20, r=20), showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

#GRAFICANDO GRAFICO BARRAS  ESTUDIANTES POR GENERO
    #2. cantidad de estudiantes por genero

    with col2:
        st.markdown("**Estudiantes por género**")
        cant = (
            datos_filtrados["Genero"]
            .value_counts()
            .rename({0: "Femenino", 1: "Masculino"})
        )
        fig, ax = plt.subplots(figsize=(4, 3.4))
        cant.plot(kind="bar", ax=ax, color="skyblue")
        ax.set_xlabel("Género", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=8)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()  

#GRAFICANDO GRAFICO BARRAS  ESTUDIANTES POR REGION
    with col3: 
        st.markdown("**Estudiantes por región(nacimiento)**")
        fig, ax = plt.subplots(figsize=(4, 3))
        sns.countplot(data=datos_filtrados, x="Region", color="royalblue", ax=ax)
        ax.set_xlabel("Región", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=8)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()    

    # Fila 2: 4 gráficos
    col4, col5, col6, col7 = st.columns(4)
#GRAFICANDO GRAFICO PIE  ESTUDIANTES POR ESTUDIAN FUERA DE SU RESIDENCIA
    with col4: 
        st.markdown("**Estudian fuera de residencia**")
        cant = (
            datos_filtrados["Estudia fuera de su lugar de residencia"]
            .value_counts()
            .rename({0: "No", 1: "Si"})
        )
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.pie(
            cant.values,
            labels=cant.index,
            autopct="%1.1f%%",
            startangle=45,
            colors=["gold", "royalblue"],
            textprops={"fontsize": 7},
        )
        st.pyplot(fig)
        plt.close() 

 #GRAFICANDO GRAFICO PIE  ESTUDIANTES POR ESTUDIAN FUERA DE SU RESIDENCIA       
    with col5: 
        st.markdown("**Necesidades especiales**")
        cant = datos_filtrados["Necesidades educativas especiales"].value_counts()
        fig, ax = plt.subplots(figsize=(3, 2.5))
        cant.plot(kind="barh", ax=ax, color="lightgreen")
        ax.set_xlabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=6)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
#GRAFICANDO CANTIDAD DE ESTUDIANTES CON Y SIN DEUDA  
    with col6: 
        st.markdown("**Estudiantes con deuda**")
        etiquetas = datos_filtrados["Deudor"].map({0: "Sin deuda", 1: "Con deuda"})
        conteo = etiquetas.value_counts()
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.pie(
            conteo,
            labels=conteo.index,
            autopct="%1.1f%%",
            colors=["gold", "red"],
            textprops={"fontsize": 7},
        )
        st.pyplot(fig)
        plt.close()

#GRAFICANDO CANTIDAD DE ESTUDIANTES POR EDAD DE INGRESO A LA UNIVERIDAD  
    with col7: 
        st.markdown("**Edad al ingreso**")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(
            data=datos_filtrados,
            x="Edad al momento de la inscripcion.",
            color="green",
            ax=ax,
        )
        ax.set_xlabel("Edad", fontsize=3)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=8)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()  


# ====== PESTAÑA 2: PERFIL ACADÉMICO DE INGRESO ======
elif char_type == "Perfil académico de ingreso":
    
    st.sidebar.markdown("###  Filtros")

    nota_ing = st.sidebar.slider(
        "Nota de ingreso",
        min_value=float(datos["Nota de ingreso"].min()),
        max_value=float(datos["Nota de ingreso"].max()),
        step=0.1,
        value=float(datos["Nota de ingreso"].min()),
    )

    seleccion_facultad= st.sidebar.multiselect(
    "Facultad",
    options=datos["Facultad"].unique(),
    default=datos["Facultad"].unique(),
    )

    
    datos_filtrados = datos[datos["Nota de ingreso"] == nota_ing]

    datos_filtrados = datos_filtrados[
    datos_filtrados["Facultad"].isin(seleccion_facultad)
    ]

    if datos_filtrados.empty:
       st.info(f"No hay registros para la nota {nota_ing:.1f}. "
                "Prueba otro valor.")
       st.stop()

    st.metric("Estudiantes según nota filtrada", len(datos_filtrados))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Distribución por rango de notas de ingreso**")
        bins = [9.5, 11, 13, 15, 17, 19]
        labels = ["9.5-11", "11.1-13", "13.1-15", "15.1-17", "17.1-19"]
        rango_notas = pd.cut(
            datos_filtrados["Nota de ingreso"],
            bins=bins,
            labels=labels,
            include_lowest=True,
        )
        df_rangos = (
            pd.DataFrame({"RANGO_NOTA": rango_notas})
            .groupby("RANGO_NOTA", observed=False)
            .size()
            .reset_index(name="CANTIDAD")
        )

        fig, ax = plt.subplots(figsize=(6, 3.3))
        sns.barplot(
            data=df_rangos, x="RANGO_NOTA", y="CANTIDAD", color="skyblue", ax=ax
        )
        ax.set_xlabel("Rango de notas", fontsize=9)
        ax.set_ylabel("Cantidad de Estudiantes", fontsize=9)
        ax.tick_params(labelsize=8)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=8)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
              



    with col2:
        st.markdown("**Nivel educativo al ingreso**")
        cant = datos_filtrados["Nivel_educativo_ingreso"].value_counts()
        fig, ax = plt.subplots(figsize=(8, 4.3))
        colores = plt.cm.Accent(range(len(cant)))
        ax.barh(cant.index, cant.values, color=colores)
        ax.set_xlabel("Cantidad de Estudiantes", fontsize=9)
        ax.set_ylabel("Nivel educativo", fontsize=9)
        ax.tick_params(labelsize=9)
        for i, valor in enumerate(cant.values):
            ax.text(valor + 0.5, i, str(int(valor)), va="center", ha="left", fontsize=10, fontweight="bold")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()



    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Estudiantes por facultad**")

        cant = datos_filtrados["Facultad"].value_counts()

        labels = [chr(65 + i) for i in range(len(cant))] 

        fig, ax = plt.subplots(figsize=(6, 3.4))
        ax.bar(labels, cant.values, edgecolor="black")
        ax.set_xlabel("Facultades", fontsize=9)
        ax.set_ylabel("Cantidad de Estudiantes", fontsize=9)
        ax.tick_params(labelsize=8)

        for p in ax.patches:
            ax.annotate(
                f"{int(p.get_height())}",
                (p.get_x() + p.get_width() / 2, p.get_height()),
                ha="center",
                va="bottom",
                fontsize=7,
            )

        handles = [plt.Line2D([0], [0], lw=0, marker='s', markersize=6) for _ in labels]
        ax.legend(handles, [f"{lbl} = {fac}" for lbl, fac in zip(labels, cant.index)],
                title="Facultades", loc='upper right', fontsize=7, title_fontsize=8)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col4:
        st.markdown("**Modalidad de postulación**")
        cant = datos_filtrados["Modalidad  de postulación"].value_counts()
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.pie(
            cant,
            labels=cant.index,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 8}
        )
        ax.legend(loc="upper left", fontsize=7)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ====== PESTAÑA 3: PERFIL ACADÉMICO DE ESTUDIO======
elif char_type == "Perfil académico de estudio": 
    st.sidebar.markdown("## Filtros")
    
    year_choice = st.sidebar.slider(
        "NUMERO DE CURSOS",
        min_value=int(datos["Numero_cursos_aprobados_primer_año"].min()),
        max_value=int(datos["Numero_cursos_aprobados_primer_año"].max()),
        step=1,
        value=int(datos["Numero_cursos_aprobados_primer_año"].mean())
    )
   
    df_filtered = datos[datos["Numero_cursos_aprobados_primer_año"] == year_choice]

    col1, col2, col3 = st.columns(3)

    if df_filtered.empty:
        st.warning(f"No hay datos para el número de cursos aprobado seleccionado: {year_choice}")
    else:

        with col1:
            st.markdown("##### Distribución de Notas Promedio (1er Año)")

            import plotly.graph_objects as go
            import plotly.express as px

            bins = [0, 5, 10, 15, 20]
            labels = ['0-5', '5-10', '10-15', '15-20']

            cantidad_por_rango_nota_primer_año = pd.cut(
                df_filtered['Nota_promedio_primer_año'], 
                bins=bins, 
                labels=labels, 
                right=False
            ).value_counts(sort=False)

            fig1 = go.Figure(
                [go.Pie(
                    values=cantidad_por_rango_nota_primer_año.values,
                    labels=cantidad_por_rango_nota_primer_año.index,
                    textinfo='label+percent',
                    marker=dict(colors=px.colors.qualitative.Plotly),
                    insidetextorientation='radial'
                )]
            )

            fig1.update_layout(
                #title="Distribución de estudiantes por rango de Nota promedio del primer año",
                autosize=False,
                width=400,
                height=400,
                legend_title="Rango de Notas",
                legend=dict(orientation="v", x=1.05, y=0.5, font=dict(size=10))
            )

            st.plotly_chart(fig1, use_container_width=True)
            st.markdown("---")

            # =================== SEGUNDO GRÁFICO (2do año) ===================

            st.markdown("##### Distribución de Notas Promedio (2do Año)")

            cantidad_por_rango_nota_segundo_año = pd.cut(
                df_filtered['Nota_promedio_segundo_año'], 
                bins=bins, 
                labels=labels, 
                right=False
            ).value_counts(sort=False)

            fig2 = go.Figure(
                [go.Pie(
                    values=cantidad_por_rango_nota_segundo_año.values,
                    labels=cantidad_por_rango_nota_segundo_año.index,
                    textinfo='label+percent',
                    marker=dict(colors=px.colors.qualitative.Vivid),
                    insidetextorientation='radial'
                )]
            )

            fig2.update_layout(
                #title="Distribución de estudiantes por rango de Nota promedio del segundo año",
                autosize=False,
                width=400,
                height=400,
                legend_title="Rango de Notas",
                legend=dict(orientation="v", x=1.05, y=0.5, font=dict(size=10))
            )

            st.plotly_chart(fig2, use_container_width=True)
            st.markdown("---")
       
        with col2:
            st.markdown("##### Número de Cursos Aprobados (1er Año)")
            
            
            fig3, ax3 = plt.subplots(figsize=(5, 4))
            sns.countplot(data=df_filtered, x='Numero_cursos_aprobados_primer_año', ax=ax3, palette='Reds_d')
            #ax3.set_title("Cursos Aprobados (1er Año)", fontsize=10)
            ax3.set_xlabel("N° Cursos Aprobados", fontsize=9)
            ax3.set_ylabel("Cantidad de Estudiantes", fontsize=9)

            for container in ax3.containers:
                ax3.bar_label(container, fmt="%.0f", fontsize=10)

            plt.tight_layout()
            st.pyplot(fig3)
            plt.close(fig3) 
            
            st.markdown("---") 

#Gráfico 2 de la columna 2
            st.markdown("##### Número de Cursos Aprobados (2do Año)")
            
            
            fig4, ax4 = plt.subplots(figsize=(5, 4))
            sns.countplot(data=df_filtered, x='Numero_cursos_aprobados_segundo_año', ax=ax4, palette='Blues_d')
           # ax4.set_title("Cursos Aprobados (2do Año)", fontsize=10)
            ax4.set_xlabel("N° Cursos Aprobados", fontsize=9)
            ax4.set_ylabel("Cantidad de Estudiantes", fontsize=9)

            for container in ax4.containers:
                ax4.bar_label(container, fmt="%.0f", fontsize=10)
            
            plt.tight_layout()
            st.pyplot(fig4)
            plt.close(fig4) 


        
        with col3:
            st.markdown("##### Estudiantes por situación académica")
            
            cant_estudiantes_por_variable_objetivo = df_filtered["Variable_Objetivo"].value_counts().reset_index()
            cant_estudiantes_por_variable_objetivo.columns = ['Variable_Objetivo', 'Conteo']
            
            
            fig5, ax5 = plt.subplots(figsize=(5, 5))
            ax5 = sns.barplot(
                x='Variable_Objetivo', 
                y='Conteo', 
                data=cant_estudiantes_por_variable_objetivo, 
                palette="viridis",
                ax=ax5
            )

           # ax5.set_title("Estudiantes por situación académica", fontsize=10)
            ax5.set_xlabel("Situación académica", fontsize=9)
            ax5.set_ylabel("Cantidad de estudiantes", fontsize=9)

            
            for container in ax5.containers:
                ax5.bar_label(container, fmt="%.0f", fontsize=10)
            
            plt.tight_layout()
            st.pyplot(fig5) 
            plt.close(fig5)




# ====== PESTAÑA 4: SITUACIÓN ACADÉMICA POR VARIABLES DEMOGRÁFICAS=====

elif char_type=="Situación académica por variables demográficas":
    st.sidebar.markdown("## Filtros")

    seleccion_estado_civil = st.sidebar.multiselect(
    "Estado Civil",
    options=datos["Estado Civil"].unique(),
    default=datos["Estado Civil"].unique(),
    )

    seleccion_genero= st.sidebar.multiselect(
    "Genero, , 1=Masculino; 0= Femenino",
    options=datos["Genero"].unique(),
    default=datos["Genero"].unique(),
    )

    seleccion_fuera_residencia= st.sidebar.multiselect(
    "Estudian fuera de su residencia, , 1=SI; 0= NO",
    options=datos["Genero"].unique(),
    default=datos["Genero"].unique(),
    )
   

    #datos_filtrados = datos[datos["Edad al momento de la inscripcion."] == edad_eleccion]
    datos_filtrados = datos[
     (datos["Estado Civil"].isin(seleccion_estado_civil)) & (datos["Genero"].isin(seleccion_genero))& (datos["Estudia fuera de su lugar de residencia"].isin(seleccion_fuera_residencia))
    ]

    #st.write(datos_filtrados)

    #st.metric("Estudiantes filtrados", len(datos_filtrados))


    # Métricas
    colA, colB, colC, colD = st.columns(4)
    total = len(datos_filtrados)
    pct_grad = datos_filtrados["Variable_Objetivo"].eq("Graduado").mean() * 100
    pct_des = datos_filtrados["Variable_Objetivo"].eq("Desertor").mean() * 100
    pct_enc = datos_filtrados["Variable_Objetivo"].eq("En curso").mean() * 100

    with colA:
        st.metric("Total estudiantes filtrados", f"{total:,}")
    with colB:
        st.metric("% Graduados", f"{pct_grad:.1f}%")
    with colC:
        st.metric("% Desertores", f"{pct_des:.1f}%")
    with colD:
        st.metric("% En curso", f"{pct_enc:.1f}%")

    
    
#GRAFICANDO GRAFICO SITUACION ACADÉMICA POR ESTADO CIVIL
 
# Fila 1: 3 gráficos
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Situación por Estado civil**")
        df_pivot = datos_filtrados.groupby(["Variable_Objetivo", "Estado Civil"]).size().unstack()
        df_long = df_pivot.reset_index().melt(
            id_vars="Variable_Objetivo", var_name="Estado Civil", value_name="Cantidad"
        )
        fig = px.bar(
            df_long,
            x="Estado Civil",
            y="Cantidad",
            color="Variable_Objetivo",
            barmode="group",
            text="Cantidad",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            height=300,
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), font=dict(size=12))
        st.plotly_chart(fig, use_container_width=True)

#GRAFICANDO GRAFICO SITUACION ACADÉMICA POR GÈNERO
    with col2:
        st.markdown("**Situación por Género**")
        df_pivot = (
            datos_filtrados.groupby(["Variable_Objetivo", "Genero"])
            .size()
            .unstack()
            .rename(columns={0: "Femenino", 1: "Masculino"})
        )
        fig, ax = plt.subplots(figsize=(4, 3))
        df_pivot.plot(
            kind="bar", ax=ax, stacked=True, color=["darkorchid", "royalblue"]
        )
        ax.set_xlabel("Situación académica", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.legend(fontsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
#GRAFICANDO GRAFICO SITUACION ACADÉMICA POR REGIÓN
    with col3:
        st.markdown("**Situación por Región**")
        df_pivot = datos_filtrados.groupby(["Variable_Objetivo", "Region"]).size().unstack()
        fig, ax = plt.subplots(figsize=(4, 3))
        df_pivot.plot(kind="bar", ax=ax, color=["gold", "green", "royalblue"])
        ax.set_xlabel("Situación académica", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.legend(fontsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

#Fila 2: 3 gráficas
    col4, col5, col6 = st.columns(3)

#GRAFICANDO GRAFICO SITUACION ACADÉMICA POR ESTUDIAN FUERA DE SU LUGAR DE RESIDENCIA

    #4  variable objetivo vs si estudian fuera de su lugar de residencia  0  no
    variableobjetivo_vs_estudian_fuera_lugar_residencia=datos_filtrados.groupby(["Variable_Objetivo","Estudia fuera de su lugar de residencia"]).size().unstack()
    variableobjetivo_vs_estudian_fuera_lugar_residencia=variableobjetivo_vs_estudian_fuera_lugar_residencia.rename(columns={0:"No",1:"Si"})
    with col4:
        st.write("Situación académica por estudian fuera de su lugar de residencia")
        titulobarravi4=variableobjetivo_vs_estudian_fuera_lugar_residencia.plot(kind="bar",xlabel="Situación académica actual y condición estudian y no fuera de su residencia",ylabel="Cantidad de estudiantes",color=["orangered", "lightseagreen"])
        for bar in titulobarravi4.containers:
            titulobarravi4.bar_label(bar, fmt="%.0f", fontsize=9)
        st.pyplot(plt)

#GRAFICANDO GRAFICO SITUACION ACADÉMICA POR RANGO DE EDAD AL MOMENTO DE LA INSCRIPCION
    with col5:
        st.markdown("**Situación académica por rango de edad**")
        bins = [17, 20, 24, 28, 32, 36, 40]
        labels = ["17-20", "21-24", "25-28", "29-32", "33-36", "36-40"]
        rango_edades = pd.cut(
            datos_filtrados["Edad al momento de la inscripcion."],
            bins=bins,
            labels=labels,
            include_lowest=True,
        )
        df_temp = pd.DataFrame(
            {
                "RANGO_EDAD": rango_edades,
                "Variable_Objetivo": datos["Variable_Objetivo"],
            }
        )
        df_rangos = (
            df_temp.groupby(["RANGO_EDAD", "Variable_Objetivo"], observed=True)
            .size()
            .reset_index(name="CANTIDAD")
        )

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
       

        for variable, datos_var in df_rangos.groupby("Variable_Objetivo"):
            for x, y in zip(datos_var["RANGO_EDAD"], datos_var["CANTIDAD"]):
                ax.text(
                    x, y + 0.8,              
                    str(int(y)),             
                    ha="center", va="bottom",
                    fontsize=6, color="black"
            )

        ax.set_xlabel("Rango de edad", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=6, rotation=45)
        ax.legend(fontsize=6)
        plt.tight_layout()

        st.pyplot(fig)
        plt.close()

# ====== PESTAÑA 5: SITUACIÓN ACADÉMICA POR VARIABLES ACADÉMICAS=====

elif char_type == "Situación académica por variables académicas":
    st.sidebar.markdown("### 🔍 Filtros")

    nota_ing = st.sidebar.slider(
        "Nota de ingreso",
        min_value=float(datos["Nota de ingreso"].min()),
        max_value=float(datos["Nota de ingreso"].max()),
        step=0.1,
        value=float(datos["Nota de ingreso"].min()),
    )

    datos_filtrados = datos[datos["Nota de ingreso"] == nota_ing]

    if datos_filtrados.empty:
       st.info(f"No hay registros para la nota {nota_ing:.1f}. Prueba otro valor.")
       st.stop()

    # Métricas
    colA, colB, colC, colD = st.columns(4)
    total = len(datos_filtrados)
    pct_grad = datos_filtrados["Variable_Objetivo"].eq("Graduado").mean() * 100
    pct_des = datos_filtrados["Variable_Objetivo"].eq("Desertor").mean() * 100
    pct_enc = datos_filtrados["Variable_Objetivo"].eq("En curso").mean() * 100

    with colA:
        st.metric("Total estudiantes", f"{total:,}")
    with colB:
        st.metric("% Graduados", f"{pct_grad:.1f}%")
    with colC:
        st.metric("% Desertores", f"{pct_des:.1f}%")
    with colD:
        st.metric("% En curso", f"{pct_enc:.1f}%")

    # Fila 1: 3 gráficos compactos
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("**Situación por Facultad**")
        df_pivot = datos_filtrados.groupby(["Facultad","Variable_Objetivo"]).size().unstack()

        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        df_pivot.plot(kind="bar", ax=ax, width=0.7, stacked=True)


        facultades = df_pivot.index.tolist()
        letras = [chr(65+i) for i in range(len(facultades))]
        ax.set_xticklabels(letras, rotation=0, fontsize=5)

        ax.set_xlabel("Facultad", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.legend(fontsize=5, loc="upper right")
        for c in ax.containers:
            ax.bar_label(c, fmt="%.0f", fontsize=5)

        plt.figtext(0.5, -0.12, "\n".join(f"{L}={F}" for L,F in zip(letras, facultades)),
                    ha="center", fontsize=5)

        plt.tight_layout(rect=[0, 0.05, 1, 1])
        st.pyplot(fig)
        plt.close()



    with c2:
        st.markdown("**Nivel educativo de ingreso**")

        tabla = pd.crosstab(
            datos_filtrados["Nivel_educativo_ingreso"],
            datos_filtrados["Variable_Objetivo"]
        )

        fig, ax = plt.subplots(figsize=(3.5, 2.05))
        tabla.plot(kind="barh", stacked=True, ax=ax)

        ax.set_xlabel("Cantidad de estudiantes", fontsize=7)
        ax.set_ylabel("Nivel educativo", fontsize=7)
        ax.tick_params(labelsize=8)
        ax.legend(fontsize=5, loc="upper right")

        romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        etiquetas_originales = tabla.index.tolist()
        ax.set_yticklabels(romanos[:len(etiquetas_originales)])

        leyenda_texto = "\n".join(
            [f"{romanos[i]} = {etiquetas_originales[i]}" for i in range(len(etiquetas_originales))]
        )
        plt.figtext(0.5, -0.2, leyenda_texto, ha="center", fontsize=5)

        for container in ax.containers:
            ax.bar_label(container, fmt="%.0f", fontsize=5)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

  


    with c3:
        st.markdown("**Número de Cursos aprobados (1er año)**")
        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        sns.countplot(
            data=datos_filtrados,
            x="Numero_cursos_aprobados_primer_año",
            hue="Variable_Objetivo",
            ax=ax,
        )
        ax.set_xlabel("Número de Cursos", fontsize=7)
        ax.set_ylabel("Cantidad de estudiantes", fontsize=7)
        ax.tick_params(labelsize=6)
        ax.legend(fontsize=5, loc="upper right")
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    c4, c5, c6 = st.columns(3) 



    with c4:
        st.markdown("**Número de Cursos aprobados (2do año)**")
        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        sns.countplot(
            data=datos_filtrados,
            x="Numero_cursos_aprobados_segundo_año",
            hue="Variable_Objetivo",
            ax=ax,
        )
        ax.set_xlabel("Número de Cursos", fontsize=7)
        ax.set_ylabel("Cantidad de estudiantes", fontsize=7)
        ax.tick_params(labelsize=6)
        ax.legend(fontsize=5, loc="upper right")
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    



    with c5:
        st.markdown("**Edad vs Cantidad de Desertores**")

        df_desertores = datos_filtrados[datos_filtrados["Variable_Objetivo"] == "Desertor"].copy()
        df_desertores_por_edad = (
            df_desertores.groupby("Edad al momento de la inscripcion.")["Variable_Objetivo"]
            .count()
            .reset_index(name="CANTIDAD_DESERTORES")
        )

        fig2, ax2 = plt.subplots(figsize=(5, 3.1))
        ax2.scatter(
            df_desertores_por_edad["Edad al momento de la inscripcion."],
            df_desertores_por_edad["CANTIDAD_DESERTORES"],
            color="red",
            s=20,
        )
        ax2.set_title("Edad vs Cantidad de Desertores", fontsize=10)
        ax2.set_xlabel("Edad al momento de la inscripción")
        ax2.set_ylabel("Cantidad de desertores")
        ax2.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()

        st.pyplot(fig2)
        plt.close(fig2)




    with c6:
        st.markdown("**Situación por Rango de nota al ingreso**")
        bins = [0, 5, 10, 15, 20]
        labels = ["0-5", "5-10", "10-15", "15-20"]
        datos_filtrados["Nota_de_ingreso_rango"] = pd.cut(
            datos_filtrados["Nota de ingreso"], bins=bins, labels=labels, right=False
        )
        df_pivot = (
            datos_filtrados.groupby(["Nota_de_ingreso_rango", "Variable_Objetivo"])
            .size()
            .unstack()
        )

        fig, ax = plt.subplots(figsize=(8, 5))
        df_pivot.plot(kind="bar", ax=ax)
        ax.set_xlabel("Rango de notas", fontsize=10)
        ax.set_ylabel("Cantidad de estudiantes", fontsize=10)
        ax.tick_params(labelsize=10)
        ax.legend(fontsize=10, loc="upper right")
        ax.set_xticklabels(ax.get_xticklabels(), fontsize=12, rotation=0) 
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=10)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()







#ruta de acceso +codigo streamlit
# streamlit run "C:\Users\thaty\OneDrive\Desktop\Proyecto_python_utec\proyecto_python.py"
#pip install streamlit pandas matplotlib numpy seaborn