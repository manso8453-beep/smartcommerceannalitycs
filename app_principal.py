#Este modulo permite ensamblar el resto de componentes en la UI
import streamlit as st
import pandas as pd
#Importamos los componentes reutilizables como librerias locales
from componente_datos import IngestorDatos
from componente_prediccion import MotorPrediccion

#configuramos el nombre de la pagina de nuestra app web
st.set_page_config(page_title="Consola de Componentes Comerciales", layout="wide")
st.title("  Ensamblador de Componentes: Inteligencia de Negocio")

#instanciamos los componentes de forma local
ingestor = IngestorDatos()
predictor = MotorPrediccion(incremento_simulado= 0.20)

#inicializar el estado de la sesion(sesion state)
if 'datos_negocio' not in st.session_state:
    st.session_state.datos_negocio = pd.DataFrame()

# Todo de aqui en adelante se refiere al renderizado visual.
archivo_cargado = st.file_uploader("cargar archivo de ventas (CSV)", type="csv")

if archivo_cargado:
    try:
        #Usar componente de datos para cargar el estado de la sesio state.(En el estado de la memoria).
        st.session_state.datos_negocio = ingestor.cargar_datos(archivo_cargado)
        st.success("componente de datos: ingesta y validacion exitosas")
    except Exception as e:
        st.error(f"fallo de interfaz de datos: {e}")

#si hay dattos en la session, los componentes visuales e interactivos se activan.
if not st.session_state.datos_negocio.empty:
    col_tabla, col_prediccion = st.columns(2)

    with col_tabla:
        st.subheader("📋 Registro de ventas")
        st.dataframe(st.session_state.datos_negocio, width="stretch")

    with col_prediccion:
        st.subheader("🪩🔮 Prediccion del stock requerido")
        #Pasamos los datos limpios de un componente al otro, de forma directa.
        df_predicciones = predictor.predecir_demanda(st.session_state.datos_negocio)
        st.dataframe(df_predicciones, width="stretch")