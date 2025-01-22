import pandas as pd
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import streamlit as st
import os
from utils.chart import create_chart
from quiz.full_quiz import ejecutar_quiz
from utils.show_trailers import mostrar_trailer
from utils.reports import generar_pdf
from utils.text_processing import analyze_dialogues, limpiar_subtitulos, normalizar_nombre
from data.constants import data, dream_words

st.set_page_config(page_title="Lynch en datos", layout="wide")


df = pd.DataFrame(data)

# ================== INTERFAZ STREAMLIT ==================
from data.constants import data
st.title("🎥 Lynch en datos")
st.markdown("---")

create_chart(data, df, st)

st.markdown("---")

st.header("🔍 Análisis de temáticas oníricas")
guiones_dir = "guiones"

if os.path.exists(guiones_dir):
    for pelicula in df["Película"]:
        with st.expander(f"🎞️ {pelicula}", expanded=False):
            nombre_archivo = normalizar_nombre(pelicula) + ".txt"
            archivo_guion = os.path.join(guiones_dir, nombre_archivo)

            mostrar_trailer(pelicula, st)

            if os.path.exists(archivo_guion):
                with open(archivo_guion, 'r', encoding='utf-8') as file:
                    texto = file.read()
                
                word_count, sentences_with_words = analyze_dialogues(texto, dream_words)
                
                if word_count:
                    cols = st.columns(3)
                    cols[0].metric("Palabras únicas", len(word_count))
                    cols[1].metric("Total de apariciones", sum(word_count.values()))
                    cols[2].metric("Palabra más frecuente", 
                                 value=f"{max(word_count, key=word_count.get).title()} ({word_count.most_common(1)[0][1]})")
                    
                    st.markdown("### 📌 Distribución detallada")
                    for word, count in word_count.most_common():
                        with st.container():
                            st.markdown(f"""
                            #### 🌟 **{word.capitalize()}**  
                            **Frecuencia:** {count} {'aparición' if count == 1 else 'apariciones'}  
                            **En contexto:**  
                            """)
                            
                            filtered_sentences = list(filter(lambda x: word in x[1], sentences_with_words))[:3]
                            for sentence, _ in filtered_sentences:
                                st.markdown(f"> *\"{sentence}\"*  ")

                            st.markdown("---")

                    if st.button("📄 Generar PDF",key=f"download_pdf_{pelicula}"):
                        pdf = generar_pdf(pelicula, df, word_count, sentences_with_words, df)
                        with open(f"reporte_{pelicula}.pdf", "rb") as f:
                            st.download_button("Descargar PDF", f, key=f"download_{pelicula}_button", file_name=f"reporte_{pelicula}.pdf")  
                            
                else:
                    st.warning("No se encontraron palabras clave en este guión")
            else:
                st.error(f"Archivo no encontrado: {nombre_archivo}")
else:
    st.error("⚠️ Directorio de guiones no disponible")

st.markdown("---")
st.header("🎬 Quiz Lynchiano")
st.caption("Demuestra tu conocimiento sobre el universo cinematográfico de David Lynch")
ejecutar_quiz()
st.markdown("---")
st.markdown("""
**Notas:**  
• Datos obtenidos de fuentes públicas  
• Análisis realizado con NLTK y Streamlit  
• Cifras basadas en reportes originales de estudios, no ajustadas por inflación
""")
