from data.constants import preguntas
import streamlit as st

@st.cache_data

def cargar_preguntas():
    return preguntas 