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
